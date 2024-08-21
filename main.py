from tkinter import *
from tkinter import ttk
import threading

root = Tk()
frame = ttk.Frame(root, padding = 10)

frame.grid()

ttk.Label(frame, text = "Hello World!").grid(column = 0, row = 0)
ttk.Button(frame, text = "Quit", command = root.destroy).grid(column = 1, row = 0)

root.geometry("200x200+" + str(1000) + "+" + str(500))

initial_position = root.geometry().split("+")
initial_x = int(initial_position[1])
initial_y = int(initial_position[2])

def vibrate_window_thread():
    render_loop()

def init_thread():
    t1 = threading.Thread(target = vibrate_window_thread)
    t1.start()


def render_loop(VALUE_TO_INC = 3, MIN = initial_x - 9, MAX = initial_x + 9):
    i = 1
    while True:
        current_position = root.geometry().split("+")
        current_x = int(current_position[1])

        if VALUE_TO_INC > 0:
            if current_x < MAX:
                root.geometry("200x200+" + str(current_x + VALUE_TO_INC) + "+" + str(initial_y))
                i += 1
            else:
                VALUE_TO_INC = VALUE_TO_INC * -1
                i = -1
    
        if VALUE_TO_INC < 0:
            if current_x > MIN:
                root.geometry("200x200+" + str(current_x + VALUE_TO_INC) + "+" + str(int(current_position[2])))
                i -= 1
            else:
                VALUE_TO_INC = VALUE_TO_INC * -1
                i = 1


init_thread()
root.mainloop()

