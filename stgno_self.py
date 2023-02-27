import csv
import datetime
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from turtle import bgcolor, bgpic
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
import customtkinter

#Customization Themes
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

from sqlalchemy import extract

logo_path="./steg/hide-layer.ico"

class STEG():
    
    output_image_size = 0

    def main(self, root):
        root.title('STEG TOOLS by Parth Dhungana')
        root.geometry('800x600')
        root.iconbitmap(logo_path)
        root.resizable(width =False, height=False)
        root.config(bg = 'white')
        # frame = Frame(root,bg='black')
        # frame.pack(fill=BOTH, expand=1)

        tabControl = ttk.Notebook(root)
        tabControl.pack()
        
        #footer:

        lbl_CR=customtkinter.CTkLabel(root, text="Copyright © 2023   Parth Dhungana, All Rights Reserved.",font=("Papyrus", 16,"bold"), width=200)
        lbl_CR.place(relx=0.5,rely=0.980,anchor=CENTER)

        def select_IS():
            tabControl.select(1)

        def select_MS():
            tabControl.select(2)

        def select_home():
            tabControl.select(0)


        tab1 = customtkinter.CTkFrame(tabControl, width=800, height=600)#, bg="black")
        tab2 = customtkinter.CTkFrame(tabControl, width=800, height=600)
        tab3 = customtkinter.CTkFrame(tabControl, width=800, height=600)

        tab1.pack(fill="both", expand=1)
        tab2.pack(fill="both", expand=1)
        tab3.pack(fill="both", expand=1)


        tabControl.add(tab1, text='Home 🏘️')
        tabControl.add(tab2, text='Image Stegnography 📷')
        tabControl.add(tab3, text='Message Stegnography 📨')

        H_label1=customtkinter.CTkLabel(tab1, text='Home 🏘️',font=("Papyrus", 27,"bold"))#,bg="black", fg="#F7FF06")
        H_label1.place(relx=0.5,rely=0.065, anchor=CENTER)

        IS_label1=customtkinter.CTkLabel(tab2, text='Image Stegnography 📷',font=("Papyrus", 27,"bold"))#,bg="black", fg="#F7FF06")
        IS_label1.place(relx=0.5,rely=0.065, anchor=CENTER)

        MS_label1=customtkinter.CTkLabel(tab3, text='Message Stegnography 📨',font=("Papyrus", 27,"bold"))#,bg="black", fg="#F7FF06")
        MS_label1.place(relx=0.5,rely=0.065, anchor=CENTER)
        
       
            

        #Buttons for Home

        nav_IS = customtkinter.CTkButton(tab1,text="Image Stegnography 📷",command= select_IS, font=("Papyrus", 18,"bold"))
        nav_IS.place(relx=0.22,rely=0.805, anchor=CENTER)
        
        nav_MS = customtkinter.CTkButton(tab1,text="Message Stegnography 📨",command= select_MS, font=("Papyrus", 18,"bold"))
        nav_MS.place(relx=0.235,rely=0.905, anchor=CENTER)
        
       

        #Exit buttons for all tabs

        nav_exit = customtkinter.CTkButton(tab1 ,text="Exit",command= exit, font=("Papyrus", 18,"bold"))
        nav_exit.place(relx=0.87,rely=0.905, anchor=CENTER)
        
        nav_exit1 = customtkinter.CTkButton(tab2 ,text="Exit",command= exit, font=("Papyrus", 18,"bold"))
        nav_exit1.place(relx=0.87,rely=0.905, anchor=CENTER)

        nav_exit2 = customtkinter.CTkButton(tab3 ,text="Exit",command= exit, font=("Papyrus", 18,"bold"))
        nav_exit2.place(relx=0.87,rely=0.905, anchor=CENTER)

    

        


root = customtkinter.CTk()
o = STEG()
o.main(root)
root.mainloop()
