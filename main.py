import tkinter as tk
from tkinter import *
import importlib
import main_screen as home

from PIL import *
from PIL import Image
from PIL import ImageTk

def main():

	root = tk.Tk()
	app = home.main_menu(root)


	### Bell Bank img logo
	BellLogo = Image.open('bell1.png')
	BellLogo = BellLogo.resize((85, 85), Image.ANTIALIAS)

	renderedLogo = ImageTk.PhotoImage(BellLogo)
	LogoLabel = tk.Label(image=renderedLogo)
	LogoLabel.place(relx=0.025, rely=.132, anchor=W)


	## Title and size of screen (root.resizable(0,0) means it cannot be resized by UI)
	root.title('Bell Bank: Learning Management Software')
	root.geometry("450x450")
	root.resizable(0, 0)


	root.mainloop()

if __name__ == '__main__':
	main()