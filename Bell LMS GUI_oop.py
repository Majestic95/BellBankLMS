### Object Oriented Approach to GUI Design
### Austin Noyes
### June 19th, 2020

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk


class Menu(ttk.Frame): ...
class trainingPage(ttk.Frame): ...
class quizzesPage(ttk.Frame): ...
class mgmtPage(ttk.Frame): ...


class MainApplication(ttk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.menu = Menu(self)
		self.training_page = trainingPage(self)
		self.quizzes_page = quizzesPage(self)
		self.mgmt_page = mgmtPage(self)

		## GUI ##


if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()