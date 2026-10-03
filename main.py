import tkinter as tk
import pyautogui
import time
import threading


def start_():
    cont = content.get()
    spam_cycle = int(loop.get()) # No: of times to spam
    time.sleep(5)
    global spam
    spam = True
    for i in range(spam_cycle):
        if spam == True:
            for j in cont:
                if spam == False:
                    break
                else:
                    pyautogui.write(j)
                    pyautogui.press('enter', interval= 0.1)


def stop_():
    global spam
    spam = False


def app():
    window = tk.Tk()  # Defines the Window
    window.title("Spam Machine")
    window.geometry("600x500+400+100")  # Window Size + Where it appears on screen

    # Labels
    lcontent = tk.Label(text= "Text: ")
    lrange = tk.Label(text= "Repeat: ")

    # Label Place
    lcontent.place(x= 100, y= 125)
    lrange.place(x= 100, y= 175)

    # Entry
    global content
    global loop
    content = tk.Entry(width = 50)
    loop = tk.Entry(width = 50)

    # Entry Place
    content.place(x= 167, y= 125)
    loop.place(x= 167, y= 175)

    # Creating Threads
    start_spam = threading.Thread(target= start_)
    stop_spam = threading.Thread(target= stop_)

    # Buttons
    start = tk.Button(text="Start Typing", command= start_spam.start)
    stop = tk.Button(text="Stop Typing", command= stop_spam.start)

    # Button Place
    start.place(x= 150, y= 300)
    stop.place(x= 400, y= 300)

    window.mainloop()  # Keeps the window running

app()

