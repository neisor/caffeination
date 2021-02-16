import pyautogui
import time
import sys

def caffeination(seconds):
    try:
        print('Caffeination started')
        print(f'Hotkey to prevent sleep will be pressed every {seconds} seconds...')
        print('Press CTRL + C to stop caffeination')
        while True:
            pyautogui.hotkey('ctrl')
            time.sleep(seconds)
    except KeyboardInterrupt:
        print('\nCaffeination stopped')
        sys.exit()

def print_help():
    print('How to use Caffeination:')
    print('  Run: python3 caffeination.py [seconds]')
    print('\nOptional run command (if you only have python and not python3):')
    print('  Run: python caffeination.py [seconds]')
    print('\n- the seconds parameter is not needed, but you can use it to determine')
    print('  your own time between one and the next key press in the background')
    print('  Default amount of seconds is 30')

if len(sys.argv) == 2:
    if 'help' in sys.argv[1] or sys.argv[1] == '-h':
        print_help()
        sys.exit()
    seconds = sys.argv[1]
elif len(sys.argv) > 2:
    print_help()
    sys.exit()
elif len(sys.argv) == 1:
    seconds = 30
    
if seconds is None:
    seconds = 30

try:
    seconds = int(seconds)
except:
    print('You must pass an integer! Try again...')
    print('\nYou can run Caffeination with --help flag to print the manual')
    sys.exit()

if __name__ == "__main__":
    caffeination(seconds)
