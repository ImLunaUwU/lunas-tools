# Script created by ImLunaUwU

import tkinter as tk
import subprocess

def install_dependencies():
    subprocess.call(['pip', 'install', 'keyboard'])

try:
    import keyboard
except ImportError:
    install_dependencies()
    import keyboard

def press_key(key):
    keyboard.send(key)

def right_click_with_delay(button, key, countdown, original_text):
    if countdown > 0:
        button.config(text=f"Rec mode ({countdown})")
        button.after(1000, lambda: right_click_with_delay(button, key, countdown - 1, original_text))
    else:
        button.config(text=original_text)
        press_key(key)
        button.config(state="normal")

def click_animation(button, key):
    if button.cget("text") == "Pressed":
        return
    
    original_bg = button.cget("bg")
    original_text = button.cget("text")
    button.config(bg="gray", text="Pressed", state="disabled")
    press_key(key)
    button.update()
    
    button.after(5000, lambda: button.config(bg=original_bg, text=original_text, state="normal"))


root = tk.Tk()
root.title("ClipKey")
root.configure(bg='#326f78')
root.geometry("360x90")
root.resizable(False, False)
root.attributes("-topmost", True)

buttons = [
    {"text": "15 sec", "key": "f13"},
    {"text": "1 min", "key": "f14"},
    {"text": "2 min", "key": "f15"},
    {"text": "5 min", "key": "f16"}
]

for button_info in buttons:
    original_text = button_info["text"]
    button = tk.Button(root, text=original_text, command=lambda key=button_info["key"]: press_key(button_info["key"]), width=10, height=4, bg="#444444", fg="white")
    button.bind("<ButtonPress-1>", lambda event, button=button, key=button_info["key"]: click_animation(button, key))
    button.bind("<ButtonPress-3>", lambda event, button=button, key=button_info["key"], original_text=original_text: right_click_with_delay(button, key, 5, original_text))
    button.pack(side="left", padx=5, pady=5)

root.mainloop()
