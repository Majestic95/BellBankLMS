### Object Oriented Approach to GUI Design
### Austin Noyes
### June 19th, 2020


### https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly


import tkinter as tk
from tkinter import *


### Main Menu class
class main_menu:

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



	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.frame.pack()


		### Buttons

		TrainingButton = tk.Button(text="Training", foreground="blue", font="bold")
		TrainingButton.place(bordermode=OUTSIDE, relx=0.07, rely=0.31, anchor=W)
		TrainingButton.bind('<ButtonRelease-1>', training_menu)

		QuizzesButton = tk.Button(text="Quizzes", foreground="blue", font="bold")
		QuizzesButton.place(bordermode=OUTSIDE, relx=0.07, rely=0.51, anchor=W)
		QuizzesButton.bind('<ButtonRelease-1>', training_menu)


		TrainerButton = tk.Button(text="Management", foreground="blue", font="bold")
		TrainerButton.place(bordermode=OUTSIDE, relx=0.038, rely=0.71, anchor=W)
		TrainerButton.bind('<ButtonRelease-1>', training_menu)


		### Labels

		TrainingLabel = tk.Label(text="Training To-Do, Scheduling, etc.", foreground="blue", background="lightgray")
		TrainingLabel.place(relx=0.35, rely=0.29)


		QuizzesLabel = tk.Label(text="Quiz Scores, Performance, etc.", foreground="blue", background="lightgray")
		QuizzesLabel.place(relx=0.35, rely=0.49)


		TrainerLabel = tk.Label(text="Trainer Admin: Course, Roster and Training Mgmt", foreground="blue", background="lightgray")
		TrainerLabel.place(relx=0.35, rely=0.69)



class training_menu:
	pass
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
		self.quitButton.pack()
		self.frame.pack()

	def close_windows(self):
		self.master.destroy()