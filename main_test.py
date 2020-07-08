
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
        for F in (page_Menu, page_Training, page_Quizzes, page_Mgmt, page_Roster):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("page_Menu")

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            # frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class page_Menu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller


        ### This code is not working currently // It displays Bell Bank logo

        # BellLogo = Image.open('bell1.png')
        # BellLogo = BellLogo.resize((85, 85), Image.ANTIALIAS)

        # renderedLogo = ImageTk.PhotoImage(BellLogo)
        # LogoLabel = tk.Label(image=renderedLogo)
        # LogoLabel.pack()


        label = tk.Label(self, text="Bell Bank: Learning Management Software", font=controller.title_font, background="blue", foreground="white")
        label.pack(side="top")

        button1 = tk.Button(self, text="Training",
                            command=lambda: controller.show_frame("page_Training"))
        button2 = tk.Button(self, text="Quizzes",
                            command=lambda: controller.show_frame("page_Quizzes"))
        button3 = tk.Button(self, text="Management",
                            command=lambda: controller.show_frame("page_Mgmt"))
        button1.pack(expand=1)
        button2.pack(expand=1)
        button3.pack(expand=1)


class page_Training(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Training To-Do, Scheduling, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        button.pack()


class page_Quizzes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        button.pack()


class page_Mgmt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        button1 = tk.Button(self, text="Training Classes/Rosters", 
                            command=lambda: controller.show_frame("page_Roster"))
        button.pack()
        button1.pack()


class page_Roster(tk.Frame):

    def __init__(self, parent, controller, trainees=None):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        if not trainees:
            self.trainees = []
        else:
            self.trainees = trainees

        trainee1 = tk.Label(self, text="---Add Trainee Here---", bg="lightgrey", fg="blue", pady=10)

        self.trainees.append(trainee1)

        for trainees in self.trainees:
            trainees.pack(side="top", fill="x")

        self.trainee_create = tk.Text(self, height=3, bg="white", fg="black")

        self.trainee_create.pack(side="bottom", fill="x")
        self.trainee_create.focus_set()

        self.trainee_create.bind("<Return>", self.add_trainee)

        self.color_schemes = [{"bg": "lightgrey", "fg": "blue"}, {"bg": "grey", "fg": "white"}]


    def add_trainee(self, event=None):
        trainee_name = self.trainee_create.get(1.0,END).strip()

        if len(trainee_name) > 0:
            new_trainee = tk.Label(self, text=trainee_name, pady=10)

            _, trainee_style_choice = divmod(len(self.trainees), 2)

            my_scheme_choice = self.color_schemes[trainee_style_choice]

            # new_trainee_configure(bg=my_scheme_choice["bg"])
            # new_trainee_configure(fg=my_scheme_choice["fg"])

            new_trainee.pack(side="top", fill="x")

            self.trainees.append(new_trainee)

        self.trainee_create.delete(1.0, END)


if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()