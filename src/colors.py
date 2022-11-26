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

def printc(text: str, c1: str = BG.Black, c2: str = FG.White):
    print(c1 + c2 + text + ENDC, end='')

def printlnc(text: str, c1: str = BG.Black, c2: str = FG.White):
    print(c1 + c2 + text + ENDC)

def print_error(text: str):
    printlnc(text, BG.Red, FG.White)

def print_ok(text: str):
    printlnc(text, BG.Blue, FG.White)