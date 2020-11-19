import tkinter as tk
import threading
import sys
import time

buttons = []
lights = []
thread = None

class App(tk.Frame):
    def __init__(self, lobj, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.lobj = lobj
        self.bs = []
        self.fs = []
        self.lights = {}
        self.create_widgets()
        self.running = True
        self.process()

    def quit(self):
        self.running = False
        time.sleep(1)
        super().quit()


    def process(self):
        for pin, strip in self.lobj.items():
            for i, col in enumerate(strip):
                self.lights[pin][i]["fg"] = "#{:02x}{:02x}{:02x}".format(col[0], col[1], col[2])
        if self.running:
            self.master.after(50, self.process)

    def create_widgets(self):
        for b in buttons:
            bt = tk.Button(self)
            bt["text"] = "Button @pin{}".format(b[0])
            bt["command"] = lambda: b[1](b[0])
            bt.pack(side="top")
            self.bs.append(bt)
        for l in lights:
            frame = tk.Frame(self)
            frame['borderwidth'] = 2
            frame['relief'] = "solid"
            frame.pack(side="top")
            l1 = tk.Label(frame, text="leds@pin{}".format(l.pin))
            l1.pack(side="left")
            self.lights[l.pin] = []
            for p in range(l.num):
                lab = tk.Label(frame, text='\u25CF'.format(p))
                lab.pack(side="left")
                self.lights[l.pin].append(lab)
            self.fs.append(frame)

lobj = {}

def render_thread():
    global lobj
    root = tk.Tk()
    root.title("Neopixel Simulator")
    root.option_add('*Font', 'Sans 18')
    app = App(lobj, master=root)
    app.mainloop()
    print("")
    print("")
    print("Ignore errors below here:")
    print("-------------------------")
    print("")

def render(pixels):
    global thread, lobj
    if thread is None:
        thread = threading.Thread(target=render_thread)
        thread.start()

    lobj[pixels.pin] = pixels.lights
    #print("Render:")
    #print(lights)
    #print(buttons)
    if not thread.is_alive():
        sys.exit(0)
