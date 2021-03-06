
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


        ### Frame creation
        self.staticFrame = tk.Frame(self)

        ### Labels
        self.label1 = tk.Label(self.staticFrame, width=10, padx=27, pady=5, text="First Name:", anchor="nw")
        self.label2 = tk.Label(self.staticFrame, width=10, padx=27, pady=5, text="Last Name:", anchor="nw")
        self.label3 = tk.Label(self.staticFrame, width=10, padx=27, pady=5, text="Branch:", anchor="nw")
        self.label4 = tk.Label(self.staticFrame, width=10, padx=27, pady=5, text="Start Date:", anchor="nw")
        self.label5 = tk.Label(self.staticFrame, width=10, padx=27, pady=5, text="Position/Title:", anchor="nw")


        ### Packing
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()



        ### Frame creation
        self.userFrame = tk.Frame(self)


        ### Text Boxes
        ###     If there are future additions here, you have to add them to
        ###     the function 'def createDbPreview' array as well

        self.tFirstName = tk.Text(self.userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tFirstName.bind("<Tab>", self.focus_next_widget)
        self.tFirstName.bind("<Shift-Tab>", self.focus_last_widget)


        self.tLastName = tk.Text(self.userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tLastName.bind("<Tab>", self.focus_next_widget)
        self.tLastName.bind("<Shift-Tab>", self.focus_last_widget)


        self.tBranch = tk.Text(self.userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tBranch.bind("<Tab>", self.focus_next_widget)
        self.tBranch.bind("<Shift-Tab>", self.focus_last_widget)


        self.tStartDate = tk.Text(self.userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tStartDate.bind("<Tab>", self.focus_next_widget)
        self.tStartDate.bind("<Shift-Tab>", self.focus_last_widget)


        self.tPosition = tk.Text(self.userFrame, font=("Helvetica", 10), width=30, height=1, bg="white", fg="black")
        self.tPosition.bind("<Tab>", self.focus_next_widget)
        self.tPosition.bind("<Shift-Tab>", self.focus_last_widget)


        ### Button(s)
        self.bSubmit = tk.Button(self.userFrame, width=15, text="Submit for Review", relief=RAISED,
                                    command = lambda: self.add_trainee())


        ### Packing
        self.tFirstName.pack(anchor="w", pady=2, ipady=2)
        self.tLastName.pack(anchor="w", pady=2, ipady=2)
        self.tBranch.pack(anchor="w", pady=2, ipady=2)
        self.tStartDate.pack(anchor="w", pady=2, ipady=2)
        self.tPosition.pack(anchor="w", pady=2, ipady=2)
        self.bSubmit.pack(anchor="e")


        ### Frame creation ###
        self.displayFrame = tk.Frame(self)


        ### Labels (created with empty text; text will be filled with user entry from
        ###         above tFirstName, tLastName, tBranch, tStartDate, tPosition)

        self.lFirstName = tk.Label(self.displayFrame, font=("calibri", 14, 'bold', 'italic'), text="")
        self.lLastName = tk.Label(self.displayFrame, font=("calibri", 14, 'bold', 'italic'), text="")
        self.lPosition = tk.Label(self.displayFrame, font=("Helvetica", 10), text="")
        self.lBranch = tk.Label(self.displayFrame, font=("Helvetica", 10), text="")
        self.lHireDate = tk.Label(self.displayFrame, font=("Helvetica", 10), text="")

        ### Button
        self.bAddTrainee = tk.Button(self.userFrame, width=8, text="Submit", relief=RAISED)
        self.bAddTrainee.bind('<ButtonRelease-1>', self.createLabel)


        ### Packing
        self.lHireDate.pack(side=BOTTOM, anchor="w")
        self.lBranch.pack(side=BOTTOM, anchor="w")
        self.lPosition.pack(side=BOTTOM, anchor="w")
        self.lFirstName.pack(side=LEFT, anchor="w")        
        self.lLastName.pack(side=LEFT, anchor="w", ipady=1)




        ### Frame creation ###
        self.testFrame = tk.Frame(self, highlightbackground="black", highlightthickness=1)

        self.label1 = tk.Label(self.testFrame, text="THIS IS")
        self.label2 = tk.Label(self.testFrame, text="testFrame")

        self.label1.pack()
        self.label2.pack()



        ### FRAME PACKING
        self.displayFrame.pack(side=BOTTOM, pady=70, padx=25, anchor="w")
        self.staticFrame.pack(side=LEFT, anchor="nw")
        self.userFrame.pack(side=LEFT, anchor="nw")
        self.testFrame.pack(side=BOTTOM)



    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return("break")



    def focus_last_widget(self, event):
        event.widget.tk_focusPrev().focus()
        return("break")


        ### TO DO ###
    def createLabel(self, event=None):
        pass


        ### TO DO: Priority 1 ###
    def createDbPreview(self, array):
        pass



    def add_trainee(self):

        ### Variables

        firstName = self.tFirstName.get(1.0,END).strip()
        lastName = self.tLastName.get(1.0,END).strip()
        branch = self.tBranch.get(1.0,END).strip()
        startDate = self.tStartDate.get(1.0,END).strip()
        position = self.tPosition.get(1.0,END).strip()


        ### ALL above variables should be included in THIS array;
        ### Current count: 5
        self.user_Input = []


        for info in (firstName, lastName, branch, startDate, position):

            if len(self.user_Input) < 5:
                self.user_Input.append(info)
                pass
            else:
                print("No data entered in a user entry field")

        self.createDbPreview(self.user_Input)




if __name__ == "__main__":
    app = BellBankLMS()
    app.mainloop()