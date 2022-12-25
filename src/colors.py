from typing import Union

ENDC = '\033[0m'    

class FG:
    Black   = '\033[30m' 
    Red     = '\033[31m' 
    Green   = '\033[32m' 
    Yellow  = '\033[33m' 
    Blue    = '\033[34m' 
    Magenta = '\033[35m' 
    Cyan    = '\033[36m' 
    White   = '\033[37m' 
    Gray    = '\033[90m' 
    BrightRed   = '\033[91m' 
    BrightGreen    = '\033[92m' 
    BrightYellow   = '\033[93m' 
    BrightBlue = '\033[94m' 
    BrightMagenta  = '\033[95m' 
    BrightCyan = '\033[96m' 
    BrightWhite    = '\033[97m' 

class BG:
    Black      = '\033[40m'	
    Red    = '\033[41m'	
    Green      = '\033[42m'	
    Yellow     = '\033[43m'	
    Blue       = '\033[44m'	
    Magenta    = '\033[45m'	
    Cyan       = '\033[46m'	
    White      = '\033[47m'	
    Gray      = '\033[00m'	
    BrightRed     = '\033[01m'	
    BrightGreen   = '\033[02m'	
    BrightYellow      = '\033[03m'	
    BrightBlue    = '\033[04m'	
    BrightMagenta     = '\033[05m'	
    BrightCyan    = '\033[06m'	
    BrightWhite       = '\033[07m'	

def coloreds(*strings: Union[tuple[str, str, str], tuple[str, str], tuple[str]]):
    s = ''

    for string in strings:
        if len(string) == 3:
            s += colored(string[0], string[1], string[2])
        elif len(string) == 2:
            s += colored(string[0], string[1])
        else:
            s += colored(string[0])
    
    return s

def colored(text: str, fg: str = FG.White, bg: str = BG.Black):
    return fg + bg + text + ENDC

def printc(text: str, fg: str = FG.White, bg: str = BG.Black):
    print(colored(text, fg, bg), end='')

def printlnc(text: str, fg: str = FG.White, bg: str = BG.Black):
    print(colored(text, fg, bg))

def print_error(text: str):
    printlnc(text, BG.Red, FG.White)

def print_ok(text: str):
    printlnc(text, BG.Blue, FG.White)

if __name__ == '__main__':
    s1 = colored('This is a test', FG.Red, BG.Yellow)

    print(s1)
    printc('He', FG.Black, BG.White)
    printc('ll', FG.White, BG.Blue)
    printc('o!', FG.Red, BG.Green)
    print()
    printlnc('Hello world!', FG.Green, BG.Black)
    print(colored('Hello', FG.Red, BG.Yellow) + colored(' world!', FG.Yellow, BG.Red))
    print(coloreds(
        ('He', FG.Cyan),
        ('ll', FG.BrightMagenta),
        ('o w', FG.White),
        ('or', FG.BrightMagenta),
        ('ld!', FG.Cyan)
    ))