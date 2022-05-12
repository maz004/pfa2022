import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import check_camera
from PIL import ImageTk, Image 
import Capture_Image
import Recognize
import mysqlhdb
import os

class App:
    
    def __init__(self, root):
        #setting title
        root.title("Gestion d'Absence")
        
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_613=tk.Button(root)
        GButton_613["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=10)
        GButton_613["font"] = ft
        GButton_613["fg"] = "#000000"
        GButton_613["justify"] = "center"
        GButton_613["text"] = "Enregistrer un Etudiant"
        GButton_613.place(x=220,y=80,width=176,height=33)
        GButton_613["command"] = self.GButton_613_command

        GButton_199=tk.Button(root)
        GButton_199["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=10)
        GButton_199["font"] = ft
        GButton_199["fg"] = "#000000"
        GButton_199["justify"] = "center"
        GButton_199["text"] = "Train Picture"
        GButton_199.place(x=220,y=140,width=174,height=30)
        GButton_199["command"] = self.GButton_199_command

        GButton_305=tk.Button(root)
        GButton_305["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Effectuer la presence"
        GButton_305.place(x=220,y=200,width=172,height=30)
        GButton_305["command"] = self.GButton_305_command

        GButton_945=tk.Button(root)
        GButton_945["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_945["font"] = ft
        GButton_945["fg"] = "#000000"
        GButton_945["justify"] = "center"
        GButton_945["text"] = "Envoyer la presence"
        GButton_945.place(x=210,y=270,width=191,height=30)
        GButton_945["command"] = self.GButton_945_command

        GButton_384=tk.Button(root)
        GButton_384["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_384["font"] = ft
        GButton_384["fg"] = "#000000"
        GButton_384["justify"] = "center"
        GButton_384["text"] = "Envoyer la presence par mail"
        GButton_384.place(x=210,y=310,width=191,height=30)
        GButton_384["command"] = self.GButton_384_command

        GLabel_438=tk.Label(root)
        GLabel_438["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times',size=23)
        GLabel_438["font"] = ft
        GLabel_438["fg"] = "#333333"
        GLabel_438["justify"] = "center"
        GLabel_438["text"] = "Gestion d'absence pour les etudiants de l'Ensaj"
        GLabel_438.place(x=0,y=20,width=597,height=30)

       
    def GButton_613_command(self):
        Capture_Image.takeImages()


    def GButton_199_command(self):
        print("command")


    def GButton_305_command(self):
        Recognize.recognize_attendence()


    def GButton_945_command(self):
        mysqlhdb.sendit()


    def GButton_384_command(self):
        os.system("python3 automail.py")

if __name__ == "__main__":
    root = tk.Tk()
    bg_img = 'background.jpeg'
    img =Image.open(bg_img)
    bg = ImageTk.PhotoImage(img)
    root.geometry("650x450")
    # Add image
    label = Label(root, image=bg)
    label.place(x = 0,y = 0)

    app = App(root)
    
    root.mainloop()
