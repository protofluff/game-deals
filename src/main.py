from datetime import datetime
from colors import BG, FG, ENDC, coloreds, printlnc, print_error, print_ok, colored
from config import AUTHOR, VERSION, APP_ID, REDDIT_AUTHOR
import requests
from argparse import ArgumentParser
import re
from json import loads as load_json
from deal import Deal

HEADERS = {
    'User-Agent': f'shell:{APP_ID}:{VERSION} (by /u/{REDDIT_AUTHOR})',
    'Content-Type': 'application/json'
}
TITLE_RGX = re.compile(r'(^\[.+?\])')
FREE_RGX = re.compile(r'\bfree\b', re.I)
PROMO_RGX = re.compile(r'(promo code )(.+?)\b', re.I)
URLS = [
    'https://www.reddit.com/r/GameDeals/',
    'https://www.reddit.com/r/GameDeals/new/',
    'https://www.reddit.com/r/GameDeals/hot/'
]

args = ArgumentParser()
args.add_argument('-f', '--free', action='store_true', help='Show free deals', required=False)
args.add_argument('-p', '--promo', action='store_true', help='Show deals with promo codes', required=False)
args.add_argument('-o', '--others', action='store_true', help='Show other deals', required=False)
args.add_argument('-u', '--urls', help='Url list, default to urls.txt', type=str, required=False)
args.add_argument('-v', '--version', action='store_true', help='Prints the current version', required=False)
args.add_argument('-d', '--debug', action='store_true', help='Runs the program in debug mode (this is meant for testing only)', required=False)
# args.add_argument('-l', '--log', action='store_true', help='Save the output to a text file', required=False)
# args.add_argument('-L', '--log-all', action='store_true', help='Save the output to a text file, all items included', required=False)
args = args.parse_args()

def sub(source: str, replacements: dict[re.Pattern, str]):
    result = source

    for pattern, replacement in replacements.items():
        result = re.sub(pattern, replacement, result)

    return result

def style_row(deal: Deal):
    date = datetime.fromtimestamp(deal.time).strftime('%d/%m/%Y')
    text = sub(deal.title, {
        TITLE_RGX: coloreds(
            ('\\1', FG.Green, BG.Black),
            (f' ({date})', FG.Yellow)
        ),
        FREE_RGX: colored('FREE', BG.Red, FG.White),
        PROMO_RGX: coloreds(
            ('\\1', FG.Magenta),
            ('\\2', BG.Magenta, FG.White)
        )
    })

    return text

def print_deals(deals: list[Deal], title: str):
    print()
    printlnc(title, FG.Blue)
    print()

    for deal in sort_by_store(deals):
        print(style_row(deal))

def sort_by_store(deals: list[Deal]) -> list[Deal]:
    return sorted(deals, key=lambda x: (TITLE_RGX.search(x.title)[0], -x.time))

def main():
    if args.version:
        print(VERSION)
        exit(0)

    if args.urls:
        urls = open(args.urls, 'r').read().splitlines()
    else:
        urls = URLS

    deals = []

    if not urls:
        print_error('urls.txt is empty')
        exit(1)

    printlnc(f' --- GameDeals v{VERSION} by {AUTHOR} --- ', FG.White, BG.Magenta)
    print()

    for url in urls:
        try:
            if args.debug:
                with open('./src/dummy.json', 'r', encoding='utf-8') as f:
                    response = load_json(f.read())
            else:
                response = requests.get(url + '.json?limit=100', headers=HEADERS).json()

            print_ok(f'Fetched {url}')

            if response['kind'] and response['kind'] == 'Listing':
                if response['data'] and response['data']['children'] and len(response['data']['children']) > 0:
                    for post in response['data']['children']:
                        if post['data'] and post['kind'] and post['kind'] == 't3':
                            data = post['data']
                            title = data['title']
                            time = data['created']
                            source = data['url']
                            deal = Deal(title, time, source)
                            deals.append(deal)
                else:
                    print_error('Post list is empty')
            else:
                print_error(f'Not a reddit URL')
        except Exception:
            print_error(f'Cannot fetch {url}')

    deals = set(deals)
    free_deals = list(filter(lambda x: re.search(FREE_RGX, x.title), deals))
    promo_codes = list(filter(lambda x: re.search(PROMO_RGX, x.title), deals))
    deals = deals - set(free_deals) - set(promo_codes)
    show_all = not args.free and not args.promo and not args.others

    if free_deals and (show_all or args.free):
        print_deals(free_deals, 'Free deals')

    if promo_codes and (show_all or args.promo):
        print_deals(promo_codes, 'Promo codes')

    if deals and (show_all or args.others):
        print_deals(deals, 'Other deals')

if __name__ == '__main__':
    main()