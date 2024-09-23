import tkinter as tk
import pyautogui

def press_key_with_combo(key):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('shift')
    pyautogui.press(key)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('ctrl')

def right_click_with_delay(button, key, countdown, original_text):
    if countdown > 0:
        button.config(text=f"Rec mode ({countdown})")
        button.after(1000, lambda: right_click_with_delay(button, key, countdown - 1, original_text))
    else:
        button.config(text=original_text)
        press_key_with_combo(key)
        button.config(state="normal")

def click_animation(button, key):
    if button.cget("text") == "Pressed":
        return
    original_bg = button.cget("bg")
    original_text = button.cget("text")
    button.config(bg="gray", text="Pressed", state="disabled")
    press_key_with_combo(key)
    button.update()
    button.after(5000, lambda: button.config(bg=original_bg, text=original_text, state="normal"))

root = tk.Tk()
root.title("ClipKey")
root.configure(bg='#326f78')
root.geometry("360x90")
root.resizable(False, False)
root.attributes("-topmost", True)

buttons = [
    {"text": "15 sec", "key": "f1"},
    {"text": "1 min", "key": "f2"},
    {"text": "2 min", "key": "f3"},
    {"text": "5 min", "key": "f4"}
]

for button_info in buttons:
    original_text = button_info["text"]
    key = button_info["key"]
    button = tk.Button(root, text=original_text, command=lambda key=key: press_key_with_combo(key), width=10, height=4, bg="#444444", fg="white")
    button.bind("<ButtonPress-1>", lambda event, button=button, key=key: click_animation(button, key))
    button.bind("<ButtonPress-3>", lambda event, button=button, key=key, original_text=original_text: right_click_with_delay(button, key, 5, original_text))
    button.pack(side="left", padx=5, pady=5)

root.mainloop()
