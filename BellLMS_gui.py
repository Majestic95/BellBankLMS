from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk

######################################
### Functions & events for program ###
######################################

# Training menu selected
def training_menu(event):
	for widg in MenuWidgets:
		widg.place_forget()

	
# Quizzes menu selected
def quizzes_menu(event):
	for widg in MenuWidgets:
		widg.place_forget()


def OpenFile():
	name = askopenfilename()
	print(name)


# Trainer menu selected
def trainer_menu(event):
	for widg in MenuWidgets:
		widg.place_forget()



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
prog.resizable(0, 0)


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
TrainingButton.place(bordermode=OUTSIDE, relx=0.07, rely=0.31, anchor=W)
TrainingButton.bind('<ButtonRelease-1>', training_menu)


QuizzesButton = Button(text="Quizzes", foreground="blue", font="bold")
QuizzesButton.place(bordermode=OUTSIDE, relx=0.07, rely=0.51, anchor=W)
QuizzesButton.bind('<ButtonRelease-1>', quizzes_menu)


TrainerButton = Button(text="Management", foreground="blue", font="bold")
TrainerButton.place(bordermode=OUTSIDE, relx=0.038, rely=0.71, anchor=W)
TrainerButton.bind('<ButtonRelease-1>', trainer_menu)


### Labels

# Bell Bank img logo
LogoLabel = ttk.Label(image=renderedLogo)
LogoLabel.place(relx=0.025, rely=.1, anchor=W)


TrainingLabel = ttk.Label(prog, text="Training To-Do, Scheduling, etc.", foreground="blue", background="lightgray")
TrainingLabel.place(relx=0.35, rely=0.29)


QuizzesLabel = ttk.Label(prog, text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
QuizzesLabel.place(relx=0.35, rely=0.49)


TrainerLabel = ttk.Label(prog, text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="lightgray")
TrainerLabel.place(relx=0.35, rely=0.69)


### Array created to hold all menu widgets, for hiding/unhiding menu on button-clicks
MenuWidgets = [TrainingButton, QuizzesButton, TrainerButton, TrainingLabel, QuizzesLabel, TrainerLabel]


# Cascade creation
## TO DO: top toolbar expansion

menu.add_cascade(label="File", menu=filemenu)
menu.add_command(label="Open...", command=OpenFile)

mainloop()

