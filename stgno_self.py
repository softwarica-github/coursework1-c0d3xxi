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

logo_path="hide-layer.ico"

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
        
            #Window Theme (Dark Mode/Light Mode)
        def change_appearance_mode_event(new_appearance_mode: str):
                customtkinter.set_appearance_mode(new_appearance_mode)


        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(tab1, values=["Light", "Dark", "System"],command=change_appearance_mode_event, font=("Papyrus", 16, "bold"))
        appearance_mode_optionemenu.place(relx=0.75,rely=0.015)
        #default
        appearance_mode_optionemenu.set("Dark")
       
            

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

        

        #Buttons for Image Steg

        encode = customtkinter.CTkButton(tab2,text="Encrypt Image",command= lambda :self.encode_frame1(tabControl), font=("Papyrus", 16,"bold"))
        encode.place(relx=0.5,rely=0.405, anchor=CENTER)
        decode = customtkinter.CTkButton(tab2, text="Decrypt Image",command=lambda :self.decode_frame1(tabControl), font=("Papyrus", 16,"bold"))
        decode.place(relx=0.5,rely=0.505, anchor=CENTER)

        nav_homeIS = customtkinter.CTkButton(tab2 ,text="Home 🏘️",command= select_home,  font=("Papyrus", 18,"bold"))
        nav_homeIS.place(relx=0.87,rely=0.805, anchor=CENTER)
        
        #Buttons for Message Steg

        encode = customtkinter.CTkButton(tab3,text="Encrypt Message",command= lambda :self.encode_msg_frame1(tabControl), font=("Papyrus", 16,"bold"))
        encode.place(relx=0.5,rely=0.405, anchor=CENTER)
        decode = customtkinter.CTkButton(tab3, text="Decrypt Message",command=lambda :self.decode_msg_frame1(tabControl), font=("Papyrus", 16,"bold"))
        decode.place(relx=0.5,rely=0.505, anchor=CENTER)

        nav_homeAS = customtkinter.CTkButton(tab3 ,text="Home 🏘️",command= select_home, font=("Papyrus", 18,"bold"))
        nav_homeAS.place(relx=0.87,rely=0.805, anchor=CENTER)

        

        

###########################################################################################################################################################################################################################
# Loop back function to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)

    
    #GUI Image Encryption
    def encode_frame1(self,F):
        F.destroy()
        F2 = customtkinter.CTkFrame(root)
        F2.pack(fill=BOTH, expand=1)

        lab= customtkinter.CTkLabel(F2,text='Image Encryption', font=("Papyrus", 24,"bold"))
        lab.place(relx=0.5,rely=0.105, anchor=CENTER)

        label1= customtkinter.CTkLabel(F2,text='Select the image file in which you wish to ENCRYPT some text:', font=("Papyrus", 20,"bold"))
        label1.place(relx=0.5,rely=0.305, anchor=CENTER)


        button_bws = customtkinter.CTkButton(F2,text='Select Image File',command=lambda : self.encode_frame2(F2),font=("Papyrus", 20,"bold"))
        button_bws.place(relx=0.5,rely=0.505, anchor=CENTER)

        button_back = customtkinter.CTkButton(F2, text='Cancel', command= lambda : STEG.back(self,F2),font=("Papyrus", 20,"bold"))
        button_back.place(relx=0.5,rely=0.605, anchor=CENTER)


    #GUI Image Decryption
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = customtkinter.CTkFrame(root)
        d_f2.pack(fill=BOTH, expand=1)

        lab= customtkinter.CTkLabel(d_f2,text='Image Decryption', font=("Papyrus", 24,"bold"))
        lab.place(relx=0.5,rely=0.105, anchor=CENTER)

        label1 = customtkinter.CTkLabel(d_f2, text='Select the image containing hidden text which you wish to DECRYPT:',font=("Papyrus", 20,"bold"))
        label1.place(relx=0.5,rely=0.305, anchor=CENTER)

        button_bws = customtkinter.CTkButton(d_f2, text='Select Image File', command=lambda :self.decode_frame2(d_f2),font=("Papyrus", 20,"bold"))
        button_bws.place(relx=0.5,rely=0.505, anchor=CENTER)


        button_back = customtkinter.CTkButton(d_f2, text='Cancel', command=lambda : STEG.back(self,d_f2),font=("Papyrus", 20,"bold"))
        button_back.place(relx=0.5,rely=0.605, anchor=CENTER)



    #Function to encrypt image 
    def encode_frame2(self,e_F2):
        e_pg= customtkinter.CTkFrame(root)
        e_pg.pack(fill=BOTH, expand=1)

        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing!")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= customtkinter.CTkLabel(e_pg,text='Selected Image',font=("Papyrus", 20,"bold"))
            label3.place(relx=0.5,rely=0.1, anchor=CENTER)
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.place(relx=0.5,rely=0.3, anchor=CENTER)
            label2 = customtkinter.CTkLabel(e_pg, text='Enter the message',font=("Papyrus", 30,"bold"))
            label2.place(relx=0.5,rely=0.56, anchor=CENTER)
            text_a = Text(e_pg, width=50, height=10)
            text_a.place(relx=0.5,rely=0.7, anchor=CENTER)
            encode_button = customtkinter.CTkButton(e_pg, text='Cancel', command=lambda : STEG.back(self,e_pg),font=("Papyrus", 20,"bold"))
            data = text_a.get("1.0", "end-1c")
            button_back = customtkinter.CTkButton(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img), STEG.back(self,e_pg)],font=("Papyrus", 20,"bold"))
            button_back.place(relx=0.3,rely=0.90, anchor=CENTER)
            encode_button.place(relx=0.7,rely=0.90, anchor=CENTER)
            e_F2.destroy()





    #Function to decrypt image 
    def decode_frame2(self,d_F2):
        d_F3 = customtkinter.CTkFrame(root)
        d_F3.pack(fill=BOTH, expand=1)

        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing!")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= customtkinter.CTkLabel(d_F3,text='Selected Image :', font=("Papyrus", 20,"bold"))
            label4.place(relx=0.5,rely=0.1, anchor=CENTER)
            board = customtkinter.CTkLabel(d_F3, image=img)
            board.image = img
            board.place(relx=0.5,rely=0.3, anchor=CENTER)
            hidden_data = self.decode(my_img)
            label2 = customtkinter.CTkLabel(d_F3, text='The hidden data is :', font=("Papyrus", 20,"bold"))
            label2.place(relx=0.5,rely=0.56, anchor=CENTER)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.place(relx=0.5,rely=0.70, anchor=CENTER)
            button_back = customtkinter.CTkButton(d_F3, text='Cancel', command= lambda :self.frame_3(d_F3), font=("Papyrus", 20,"bold"))
            button_back.place(relx=0.5,rely=0.90, anchor=CENTER)
            d_F2.destroy()



    #Function to decrypt data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    #Function to generate data
    def generate_Data(self,data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    #Function to modify the pixels of image
    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    
    #Function to enter the data pixels in image
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Placing modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    
    #Function to enter hidden text
    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","You must enter some text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful!!\nThe file has been saved as a .png file in the same directory!\n")

    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


###############################################################################################################################################################################################################


#-----------------------------------Message steg---------------------------


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


root = customtkinter.CTk()
o = STEG()
o.main(root)
root.mainloop()
