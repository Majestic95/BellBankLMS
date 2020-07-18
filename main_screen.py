
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
        self.subtitle_font = tkfont.Font(family='Helvetica', size=12, weight="bold")

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
        label = tk.Label(self, text="Training To-Do, Scheduling, etc.", font=controller.subtitle_font, foreground="blue", background="lightgray")
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
        label = tk.Label(self, text="Quiz Scores, Performance, etc.", font=controller.subtitle_font, foreground="blue", background="lightgray")
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
        label = tk.Label(self, text="Trainer Admin: Course, Roster and Training Mgmt", font=controller.subtitle_font, foreground="blue", background="lightgray")
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
        label = tk.Label(self, text="Roster Management", font=controller.subtitle_font, foreground="blue", background="lightgray")
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


        ### TODO: Does this need to exist? Investigate
        if not trainees:
            self.trainees = []
        else:
            self.trainees = trainees


        ### Title Label
        label = tk.Label(self, text="Creating a Training Class", font=controller.subtitle_font,
                            foreground="blue", background="lightgray")
        label.pack(side="top", fill="x", ipady=3)


        ### Frame creation (for organization)
        staticFrame = tk.Frame(self)
        staticFrame.pack(side="left", anchor="nw", pady=10)



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
        userFrame = tk.Frame(self)
        userFrame.pack(side=LEFT, anchor="nw", pady=10, ipadx=50)



        ### Text Boxes
        self.tFirstName = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tFirstName.bind("<Tab>", self.focus_next_widget)
        self.tFirstName.bind("<Shift-Tab>", self.focus_last_widget)


        self.tLastName = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tLastName.bind("<Tab>", self.focus_next_widget)
        self.tLastName.bind("<Shift-Tab>", self.focus_last_widget)


        self.tBranch = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tBranch.bind("<Tab>", self.focus_next_widget)
        self.tBranch.bind("<Shift-Tab>", self.focus_last_widget)


        self.tStartDate = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tStartDate.bind("<Tab>", self.focus_next_widget)
        self.tStartDate.bind("<Shift-Tab>", self.focus_last_widget)


        self.tPosition = tk.Text(userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tPosition.bind("<Tab>", self.focus_next_widget)
        self.tPosition.bind("<Shift-Tab>", self.focus_last_widget)



        ### Frame creation
        self.displayFrame = tk.Frame(self)
        self.displayFrame.pack(side=LEFT, anchor="n")


        ### Button(s)
        self.bSubmit = tk.Button(userFrame, width=8, text="Submit", relief=RAISED)
        self.bSubmit.bind('<ButtonRelease-1>', self.add_trainee)



        ### Packing
        self.tFirstName.pack(anchor="w", pady=2, ipady=2)
        self.tLastName.pack(anchor="w", pady=2, ipady=2)
        self.tBranch.pack(anchor="w", pady=2, ipady=2)
        self.tStartDate.pack(anchor="w", pady=2, ipady=2)
        self.tPosition.pack(anchor="w", pady=2, ipady=2)
        self.bSubmit.pack(anchor="e", padx=20)



    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return("break")



    def focus_last_widget(self, event):
        event.widget.tk_focusPrev().focus()
        return("break")



    def createLabel(self, trainee_info):
        label = tk.Label(self.displayFrame, text=trainee_info, foreground="blue", background="lightgray", font=("Helvetica", 10))
        label.pack(side=BOTTOM)



    def add_trainee(self, event=None):

        ### Variables

        firstName = self.tFirstName
        lastName = self.tLastName
        branch = self.tBranch
        startDate = self.tStartDate
        position = self.tPosition


        ### ALL above variables should be included in THIS for-loop;
        ### Current count: 5

        for info in (firstName, lastName, branch, startDate, position):

            if len(info.get(1.0,END).strip()) > 0:
                self.createLabel(info)
                print(info)
            else:
                errorLabel = tk.Label(userFrame, text='{} is empty or has an invalid character.'.format(info), font="arial",
                    bg="lightgray", fg="blue")
                errorLabel.pack()





if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()