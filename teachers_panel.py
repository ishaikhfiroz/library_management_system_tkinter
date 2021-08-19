#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql 

class login_page:
    
    def __init__(self, root): 
              
        self.root = root
        self.root.title('Lecturer Panel')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #self.root.geometry('800x500+0+0')
        self.root.geometry(f'{screen_width}x{screen_height}+0+0')
        self.root.state('zoomed')

        self.root.config(bg='white')

        self.img= (Image.open("images\lms.png"))
        img_x, img_y = screen_width, screen_height - 50
        #img_x, img_y = 600, 400
        self.resized_image= self.img.resize((img_x, img_y), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(self.resized_image)        
        self.img_label = Label(self.root, image=self.new_image).place(x=0, y=0, relwidth=1, relheight=1)        

        frame1 = Frame(self.root, bg='white')
        frame1.place(x=40, y=40, width=img_x-60, height=img_y-80)
       
        title = Label(self.root, text='LECTURER CONTROL PANEL', font=('Goudy old style', 20, 'bold',), bg='lightgray', fg='#088da5').place(x=450, y=20)
        #login_id = Label(frame1, text='User ID', font=('Goudy old style', 15, 'bold'), bg='white', fg='#088da5').place(x=50, y=80)
        #self.text_login_id = Entry(frame1, font=('times new roman', 15), bg='lightgray', width=22, borderwidth=2)
        #self.text_login_id.place(x=50, y=110)
        '''
        login_pw = Label(frame1, text='Password', font=('Goudy old style', 15, 'bold'), bg='white', fg='#088da5').place(x=50, y=150)
        self.text_login_pw = Entry(frame1, font=('times new roman', 15), bg='lightgray' , width=22, borderwidth=2,show="*")
        self.text_login_pw.place(x=50, y=180)

        user_type = Label(frame1, text='User Type', font=('Goudy old style', 15, 'bold'), bg='white', fg='#088da5').place(x=50, y=220)
        self.user_type_q = ttk.Combobox(frame1, font=('Goudy old style', 15), state='readonly')
        self.user_type_q['value'] = ("Select", 'Librarian', 'Teacher', 'Administrator')
        self.user_type_q.place(x=50, y=250)
        self.user_type_q.current(0)

        self.blue_button = ImageTk.PhotoImage(file = 'login.png')
        login_button = Button(frame1, image=self.blue_button, bd=0, command=self.login_func).place(x=80, y=300)

        forget_pw = Button(frame1, text='Forget Password ?', font=('Goudy old style', 13), bg='white', fg='#088da5', bd=0).place(x=105, y=380)
        '''
    
    def login_func(self):
        pass
        
root = Tk()
obj = login_page(root)
root.mainloop()
                 


# In[ ]:




