import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name= 'C:/python/python/screenshot img/{}.png'.format(name)
    time.sleep(5)
    img= pyautogui.screenshot(name)
    img.show()

root= tk.Tk()
Frame = tk.Frame(root)
Frame.pack()

button=tk.Button(
    Frame,
    text="take screenshot",
    command = screenshot)

button.pack(side=tk.LEFT)
close= tk.Button(
    Frame,
    text='quit',
    command=quit)
close.pack(side=tk.BOTTOM)

root.mainloop()