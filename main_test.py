
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
import tkinter.messagebox as msg
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
        button.pack(expand=1)


class page_Quizzes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        button.pack(expand=1)


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

        button1.pack(expand=1)
        button.pack(expand=1)


class page_Roster(tk.Frame):

    def __init__(self, parent, controller, trainees=None):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        if not trainees:
            self.trainees = []
        else:
            self.trainees = trainees


        self.trainees_canvas = tk.Canvas(self)

        self.trainees_frame = tk.Frame(self.trainees_canvas)
        self.text_frame = tk.Frame(self)

        self.trainee_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")


        self.scrollbar = tk.Scrollbar(self.trainees_canvas, orient="vertical", command=self.
            trainees_canvas.yview)

        self.trainees_canvas.configure(yscrollcommand=self.scrollbar.set)


        self.trainees_canvas.pack(side="top", fill="both", expand=1)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas_frame = self.trainees_canvas.create_window((0, 0), window=self.trainees_frame, anchor="n")

        self.trainee_create.pack(side="bottom", fill="x")
        self.text_frame.pack(side="bottom", fill="x")
        self.trainee_create.focus_set()



        trainee1 = tk.Label(self, text="---Add Trainee Here---", bg="lightgrey", fg="blue", pady=10)
        trainee1.bind("<Button-1>", self.remove_trainee)

        self.trainees.append(trainee1)

        for trainees in self.trainees:
            trainees.pack(side="top", fill="x")


        self.trainee_create.bind("<Return>", self.add_trainee)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.bind("<Configure>", self.trainee_width)


        self.color_schemes = [{"bg": "lightgrey", "fg": "blue"}, {"bg": "grey", "fg": "blue"}]


    def add_trainee(self, event=None):
        trainee_name = self.trainee_create.get(1.0,END).strip()

        if len(trainee_name) > 0:
            new_trainee = tk.Label(self, text=trainee_name)
            self.set_trainee_color(len(self.trainees), new_trainee)

            new_trainee.bind("<Button-1>", self.remove_trainee)
            new_trainee.pack(side="top", fill="x")

            self.trainees.append(new_trainee)

        self.trainee_create.delete(1.0, END)
        self.trainee_create.mark_set("<Insert>", "1.0")


    def remove_trainee(self, event):
        trainee = event.widget
        if msg.askyesno("Confirm Deletion", "Delete " + trainee.cget("text") + "?"):
            self.trainees.remove(event.widget)
            event.widget.destroy()
            self.recolor_trainees()


    def recolor_trainees(self):
        for index, trainee in enumerate(self.trainees):
            self.set_trainee_color(index, trainee)


    def set_trainee_color(self, position, trainee):
        _, trainee_style_choice = divmod(position, 2)

        my_scheme_choice = self.color_schemes[trainee_style_choice]

        trainee.configure(bg=my_scheme_choice["bg"])
        trainee.configure(fg=my_scheme_choice["fg"])


    def on_frame_configure(self, event=None):
        self.trainees_canvas.configure(scrollregion=self.trainees_canvas.bbox("all"))


    def trainee_width(self, event):
        canvas_width = event.width
        self.trainees_canvas.itemconfig(self.canvas_frame, width = canvas_width)


    def mouse_scroll(self, event):
        if event.delta:
            self.trainees_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

                self.trainees_canvas.yview_scroll(move, "units")



if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()