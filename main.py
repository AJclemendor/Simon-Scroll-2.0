import threading
import pyautogui
import tkinter as tk


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        dec = tk.Button(self.root, text="Decrease speed", command=decrease)
        dec.pack()
        inc = tk.Button(self.root, text="Increase speed", command=increase)
        inc.pack()
        set_to_zero = tk.Button(self.root, text="Turn Off", command=zero)
        set_to_zero.pack()
        reset_to_def = tk.Button(self.root, text="Set To Default", command=reset)
        reset_to_def.pack()
        stop_first_state = tk.Button(self.root, text="Stop At Bottom", command=stop_count)
        stop_first_state.pack()
        start_again = tk.Button(self.root, text="Re-Calibrate", command=re_config)
        start_again.pack()
        add_room = tk.Button(self.root, text="Add page space", command=add_space)
        add_room.pack()
        remove_room = tk.Button(self.root, text="Remove Space", command=remove_space)
        remove_room.pack()
        label = tk.Label(self.root, text="Test")
        label.pack()

        self.root.mainloop()


global speed
speed = -5
app = App()
print("testing")


def add_space():
    global counter
    counter += 10


def remove_space():
    global counter
    counter -= 10


def increase():
    global speed
    global counter
    if abs(speed) > speed:
        speed -= 5
        counter -= 22
    else:
        speed += 5
        counter -= 22


def decrease():
    global speed
    global counter

    test_speed = speed - 5
    if test_speed > 0 and speed > 0:
        speed -= 5
        counter += 22
    else:
        test_speed = speed + 5
        if speed < 0 and test_speed < 0:
            speed += 5
            counter += 22


def reset():
    global speed
    global final_counter
    global counter
    counter = final_counter
    if abs(speed) == speed:
        speed = 1
    else:
        speed = -1


def zero():
    global speed
    speed = 0


def stop_count():
    global speed
    global scroll_down
    speed = speed * -1
    scroll_down = False


def re_config():
    global Continue_Func
    global scroll_down
    global counter
    global speed
    speed = -5
    Continue_Func = False
    counter = 0
    scroll_down = True
    pyautogui.time.sleep(5)


for i in range(10000):
    print(i)

Continue_Func = True
speed = -5
sleepTime = 0
pages = 1
scroll_down = True
pyautogui.time.sleep(5)
i = 0
counter = 0
final_counter = 0

while True:
    while scroll_down:
        pyautogui.scroll(int(speed))
        pyautogui.time.sleep(int(sleepTime))
        print(counter)
        counter += 1
        final_counter = counter
    Continue_Func = True
    while Continue_Func:
        pyautogui.scroll(int(speed))
        pyautogui.time.sleep(int(sleepTime))
        print((str(i)) + " I letter" + (str(counter)) + " vs counter")
        i += 1
        if i >= counter + 25:
            i = 0
            if speed < 0:
                speed = abs(speed)
            else:
                speed = speed * -1
