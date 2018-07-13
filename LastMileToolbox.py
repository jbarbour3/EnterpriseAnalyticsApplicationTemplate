

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class LastMileToolbox:
    def __init__(self, root):
        self.root = root
        self.apply_defaults()
        self.win = self.build_frame()
        self.top = self.build_top(self.win)
        self.middle = self.build_middle(self.win)
        self.bottom = self.build_bottom(self.win)
        self.draw_map()

    def apply_defaults(self):
        self.root.geometry('{0}x{1}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.state('zoomed')
        self.root.title("Default Title")
        self.header = ("Verdana", 8)
        self.header2 = ("Verdana", 5)
        self.bg1 = "PaleGreen1"
        self.bg2 = "silver"
        self.bg3 = "grey"

    def build_frame(self):
        win = Frame(self.root, bg=self.bg1)
        win.pack(expand=True, fill=BOTH, pady=2, padx=2)
        return win

    def build_top(self, aFrame):
        top = Frame(aFrame)
        top.pack(fill=X)

        for i in range(10):
            Button(top, text="Button{0}".format(i)).pack(side=LEFT)
        return top

    def build_middle(self, aFrame):
        middle = Frame(aFrame, bg=self.bg3)
        middle.pack(expand=True,fill=BOTH)
        #Label(middle, text="Default Label").pack()
        return middle

    def build_bottom(self, aFrame):
        bottom = Frame(aFrame)
        bottom.pack(side=BOTTOM,fill=X)
        Label(bottom, text="Default Label").pack()
        return bottom

if __name__ == "__main__":          #this runs the app when we run the .py file from command line

    root = Tk()
    app = LastMileToolbox(root)
    app.root.mainloop()
