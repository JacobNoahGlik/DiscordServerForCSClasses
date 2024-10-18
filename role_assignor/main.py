import sys
import os
import time
try:
    import pyautogui
except:
    print('pyautogui could not be imported, run `pip install pyautogui`')
    exit()
from typing import Optional, List

def send_to_keyboard(message: str, sleep_time:float=0.1) -> None:
    pyautogui.write(message)
    time.sleep(sleep_time)
    pyautogui.write('\n')
    time.sleep(0.1)

def read_file(filename) -> Optional[str]:
    if not os.path.exists(filename):
        return None
    return open(filename, 'r').read()

def main(filename:str):
    lines = read_file(filename)
    if not lines:
        print(f"Error: File '{filename}' does not exist or is empty.")
        return
    first:     bool = True
    num_lines: int  = lines.count('\n')
    for i, line in enumerate(lines.split('\n')):
        if line in ['', ' ', '\t']:
            continue
        if line == 'DO NOT RUN':
            print('this file should not be run')
            exit()
        if first: # first
            send_to_keyboard(line, sleep_time=0.2)
            time.sleep(0.4)
            first = False
        elif i == num_lines: # last
            time.sleep(0.2)
            send_to_keyboard(line, sleep_time=1.2)
        elif line[0] == ':': # role
            send_to_keyboard(line, sleep_time=0.2)
            if '@' in line: # if newline required to continue
                send_to_keyboard('')
            time.sleep(0.4)
        elif line[0] == '#': # chanel name needs extra newline
            send_to_keyboard(line)
            time.sleep(0.1)
            send_to_keyboard('')
            time.sleep(0.5)
        else:
            send_to_keyboard(line, sleep_time=0.4)
            time.sleep(0.25)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python keyboard_sender.py <filename>")
        print("Usage: python keyboard_sender.py <filename_1> <filename_2> ... <filename_n>")
        sys.exit(1)
    files: List[str] = sys.argv[1:]
    print(f'executing {len(files)} files')
    print('3', end='\r')
    time.sleep(1)
    print('2', end='\r')
    time.sleep(1)
    print('1', end='\r')
    time.sleep(1)
    for filename in files:
        print(f'running {filename} ...')
        main(filename)

