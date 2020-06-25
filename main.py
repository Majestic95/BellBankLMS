import tkinter as tk
from tkinter import *
import importlib
import main_screen as home

def main():

	root = tk.Tk()
	app = home.main_menu(root)


	## Title and size of screen (root.resizable(0,0) means it cannot be resized by UI)
	root.title('Bell Bank: Learning Management Software')
	root.geometry("450x450")
	root.resizable(0, 0)


	root.mainloop()

if __name__ == '__main__':
	main()