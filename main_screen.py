
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
import importlib

# from PIL import *
# from PIL import Image
# from PIL import ImageTk


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
        for F in (page_Menu, page_Training, page_Quizzes, page_Mgmt, page_Roster,
                    page_addClass):
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


        ### Title label
        label = tk.Label(self, text="Bell Bank: Learning Management Software", font=controller.title_font, background="blue", foreground="white")
        label.pack(side="top")

        ### Page button(s)
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

        ### Title label
        label = tk.Label(self, text="Training To-Do, Scheduling, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3, pady=10)

        ### Page button(s)
        menuButton = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        menuButton.pack()



class page_Quizzes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ### Title label        
        label = tk.Label(self, text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3, pady=10)

        ### Page button(s)
        menuButton = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        menuButton.pack()



class page_Mgmt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ### Title label
        label = tk.Label(self, text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3, pady=10)

        ### Page button(s)
        menuButton = tk.Button(self, text="Menu",
                           command=lambda: controller.show_frame("page_Menu"))
        button1 = tk.Button(self, text="Training Classes/Rosters", 
                            command=lambda: controller.show_frame("page_Roster"))

        button1.pack()
        menuButton.pack()



class page_Roster(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ### Title label
        label = tk.Label(self, text="Roster Management", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3, pady=10)

        ### Page button(s)
        button1 = tk.Button(self, text="Add Training Class",
                            command=lambda: controller.show_frame("page_addClass"))
        button2 = tk.Button(self, text="WIP: Edit Training Class",
                            command=lambda: controller.show_frame("page_Menu"))
        button3 = tk.Button(self, text="Long-Term WIP: Reports/Logs",
                            command=lambda: controller.show_frame("page_Menu"))
        button1.pack(expand=1)
        button2.pack(expand=1)
        button3.pack(expand=1)



class page_addClass(tk.Frame):

    def __init__(self, parent, controller, trainees=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        if not trainees:
            self.trainees = []
        else:
            self.trainees = trainees


        ### Title Label
        label = tk.Label(self, text="Creating a Training Class", foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3)


        ### Frame creation (for organization)
        staticFrame = tk.Frame(self, width=50, height=200, bg="blue")
        staticFrame.pack(side=LEFT, anchor="nw", pady=10)



        ### Labels
        label1 = tk.Label(staticFrame, width=10, padx=27, pady=5, text="First Name:", anchor="w")
        label2 = tk.Label(staticFrame, width=10, padx=27, pady=5, text="Last Name:", anchor="w")
        label3 = tk.Label(staticFrame, width=10, padx=27, pady=5, text="Branch:", anchor="w")
        label4 = tk.Label(staticFrame, width=10, padx=27, pady=5, text="Start Date:", anchor="w")
        label5 = tk.Label(staticFrame, width=10, padx=27, pady=5, text="Position/Title:", anchor="w")

        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()



        ### Frame creation
        userFrame = tk.Frame(self, width=230, height=150)
        userFrame.pack(side=LEFT, anchor="nw", pady=10)


        ### Text Boxes
        tFirstName = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        tLastName = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        tBranch = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        tStartDate = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        tPosition = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")

        tFirstName.pack(pady=2, ipady=2)
        tLastName.pack(pady=2, ipady=2)
        tBranch.pack(pady=2, ipady=2)
        tStartDate.pack(pady=2, ipady=2)
        tPosition.pack(pady=2, ipady=2)



if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()