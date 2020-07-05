
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
import importlib

from PIL import *
from PIL import Image
from PIL import ImageTk


### Current To=Do Helpful Links

### https://www.tutorialspoint.com/python/tk_pack.htm
### https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter


class BellBankLMS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")

        self.title('Bell Bank: Learning Management Software')
        self.geometry("450x450")
        self.resizable(0, 0)


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (pMenu, pTraining, pQuizzes, pMgmt):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("pMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class pMenu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller


        BellLogo = Image.open('bell1.png')
        BellLogo = BellLogo.resize((85, 85), Image.ANTIALIAS)

        renderedLogo = ImageTk.PhotoImage(BellLogo)
        LogoLabel = tk.Label(image=renderedLogo)
        LogoLabel.pack()


        label = tk.Label(self, text="Bell Bank: Learning Management Software", font=controller.title_font, background="blue", foreground="white")
        label.pack(side="top")

        button1 = tk.Button(self, text="Training",
                            command=lambda: controller.show_frame("pTraining"))
        button2 = tk.Button(self, text="Quizzes",
                            command=lambda: controller.show_frame("pQuizzes"))
        button3 = tk.Button(self, text="Management",
                            command=lambda: controller.show_frame("pMgmt"))
        button1.pack()
        button2.pack()
        button3.pack()


class pTraining(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Training To-Do, Scheduling, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("pMenu"))
        button.pack()


class pQuizzes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("pMenu"))
        button.pack()


class pMgmt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("pMenu"))
        button.pack()


if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()
