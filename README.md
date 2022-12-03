# Game Deals

Script for fetching game deals from r/GameDeals

## Usage

You can run `py src/main.py` with the `--help` flag to see an help screen, by default this will fetch the deals from www.reddit.com/r/GameDeals and print all available deals (free games, promo codes and discounts).

## Building with pyinstaller

Install pyinstaller

```
pip install pyinstaller
```

Create a bundled app

```
./install.sh
```

You can find the output file inside the `dist` folder.

## Running script on start-up with 

#### Windows

1. Add the executable file to your PATH.
2. Press `Win + R` on your keyboard
3. Type shell:startup
4. Create a .bat file 

```bash
gamedeals # ... Optional arguments
pause
```

#### Linxu

`// TODO`

#### MacOS

`// TODO`