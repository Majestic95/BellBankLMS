from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk


### Here is where you can list the functions
### for events, functions, loops, etc.




## __init__ settings

prog = Tk()
menu = Menu(prog)


# IMAGE/LOGO PROCESSING
BellLogo = Image.open('bell1.png')
BellLogo = BellLogo.resize((85, 85), Image.ANTIALIAS)
renderedLogo = ImageTk.PhotoImage(BellLogo)


# TITLE
prog.title('Bell Bank: Learning Management')


# window size set at 400 x 400, non-resizable by user
prog.geometry("450x450")


# window style (pulled from https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style)
style = ttk.Style()
style.configure("BW.TLabel", foreground="blue", background="white")

prog.config(menu=menu)
filemenu = Menu(menu)


#######################
### Widget Creation ###
#######################


### Buttons

TrainingButton = Button(text="Training", foreground="blue", font="bold")
TrainingButton.place(relx=0.07, rely=0.26, anchor=W)


QuizzesButton = Button(text="Quizzes", foreground="blue", font="bold")
QuizzesButton.place(relx=0.07, rely=0.46, anchor=W)


TrainerButton = Button(text="Courses", foreground="blue", font="bold")
TrainerButton.place(relx=0.065, rely=0.66, anchor=W)



### Labels

# Bell Bank img logo
LogoLabel = ttk.Label(image=renderedLogo)
LogoLabel.place(relx=0.025, rely=.1, anchor=W)


TrainingLabel = ttk.Label(prog, text="Training To-Do, Scheduling, etc.", foreground="blue", background="gray")
TrainingLabel.place(relx=0.3, rely=0.26, anchor=W)


QuizzesLabel = ttk.Label(prog, text="Quiz Scores, Performance, etc.", foreground="blue", background="gray")
QuizzesLabel.place(relx=0.3, rely=0.46, anchor=W)
TrainerButton

TrainerLabel = ttk.Label(prog, text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="gray")
TrainerLabel.place(relx=0.3, rely=0.66, anchor=W)


# Cascade creation
## TO DO: top toolbar expansion

menu.add_cascade(label="File", menu=filemenu)

mainloop()