from tkinter import * 
import random

root = Tk()

root.title("PasswordGen")

root.geometry("400x100")



def Password():

		win = Toplevel()

		win.title("Password")


		entireKey =('1','2','3','4','4','5','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','n','m',)

		figure1 = random.choice(entireKey)
		figure2 = random.choice(entireKey)
		figure3 = random.choice(entireKey)
		figure4 = random.choice(entireKey)
		figure5 = random.choice(entireKey)
		figure6 = random.choice(entireKey)
		figure7 = random.choice(entireKey)
		figure8 = random.choice(entireKey)

		label = Label(win, text = "Your Password is: " + figure1+figure2+figure3+figure4+figure5+figure6+figure7+figure8 )
		label.pack()


text = Label(root, text = " Press The button to Generate a Password ")
text.pack()


buton = Button(root, text = "Press Here!", command = Password)
buton.pack()


wall = PhotoImage(file = "lg.png")
wallL = Label(root, image = wall)
wallL.pack()


root.mainloop()
