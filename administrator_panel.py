from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql 

class admin_page:
    
    def __init__(self, root): 
              
        self.root = root
        self.root.title('Administrator Panel')

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

        frame1 = Frame(self.root, bg='#EBF5FB')
        frame1.place(x=40, y=40, width=img_x-60, height=img_y-80)
        
        title = Label(self.root, text='ADMINISTRATOR CONTROL PANEL', font=('Goudy old style', 20, 'bold',), bg='lightgray', fg='#088da5').place(x=450, y=20)

        
        ############################################################################################
        frame2 = Frame(frame1, bg='lightgray')
        frame2.place(x=60, y=70, width=700, height=230)
        user_title = Label(frame1, text='USERS PANEL', font=('Goudy old style', 15, 'bold',), bg='blue', fg='white').place(x=70, y=60)
        button1 = Button(frame2, text='Add User', font=('Goudy old style', 13, 'bold'), bg='white', 
                         fg='#088da5', command=self.add_user).place(x=10, y=190)
        button2 = Button(frame2, text='Edit User', font=('Goudy old style', 13, 'bold'), bg='white', fg='#088da5').place(x=100, y=190)
        button3 = Button(frame2, text='Delete User', font=('Goudy old style', 13, 'bold'), bg='white', 
                         fg='#088da5', command=self.delete_user_table).place(x=190, y=190)

        frame2_sub = Frame(frame2, bd=4, relief=RIDGE, bg='white')
        frame2_sub.place(x=10, y=20, width=670, height=170)
        
        user_columns = ('SN', 'FIRST_NAME', 'LAST_NAME', 'CONTACT', 'EMAIL_ID', 'USERNAME', 'PASSWORD', 'USER_TYPE')
        scroll_x = Scrollbar(frame2_sub, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame2_sub, orient=VERTICAL)
        self.user_table = ttk.Treeview(frame2_sub, columns=user_columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)     
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)
        self.user_table.heading('SN', text='SL NO')
        self.user_table.heading('FIRST_NAME', text='FIRST NAME')
        self.user_table.heading('LAST_NAME', text='LAST NAME')
        self.user_table.heading('CONTACT', text='CONTACT')
        self.user_table.heading('EMAIL_ID', text='EMAIL ID')
        self.user_table.heading('USERNAME', text='USERNAME')
        self.user_table.heading('PASSWORD', text='PASSWORD')
        self.user_table.heading('USER_TYPE', text='USER TYPE')
        self.user_table['show'] = 'headings'
        self.user_table.column('SN', width=50)
        self.user_table.column('FIRST_NAME', width=100)
        self.user_table.column('LAST_NAME', width=100)
        self.user_table.column('CONTACT', width=100)
        self.user_table.column('EMAIL_ID', width=150)
        self.user_table.column('USERNAME', width=100)
        self.user_table.column('PASSWORD', width=100)
        self.user_table.column('USER_TYPE', width=100)
        self.user_table.pack(fill=BOTH, expand=1)
        self.fetch_user_table()
            
        ###########################################################################################################    
            
        frame3 = Frame(frame1, bg='lightgray')
        frame3.place(x=60, y=340, width=700, height=230)        
        students_title = Label(frame1, text='STUDENTS PANEL', font=('Goudy old style', 15, 'bold',), bg='blue', fg='white').place(x=70, y=330)
        button4 = Button(frame3, text='Add Student', font=('Goudy old style', 13, 'bold'), 
                         command=self.add_student, bg='white', fg='#088da5').place(x=10, y=190)
        button5 = Button(frame3, text='Edit Student', font=('Goudy old style', 13, 'bold'), bg='white', fg='#088da5').place(x=120, y=190)
        button6 = Button(frame3, text='Delete Student', font=('Goudy old style', 13, 'bold'), bg='white', fg='#088da5').place(x=230, y=190)
        button7 = Button(frame3, text='Import Students', font=('Goudy old style', 13, 'bold'), bg='white', fg='#088da5').place(x=360, y=190)
        button7 = Button(frame3, text='Search Student', font=('Goudy old style', 13, 'bold'), bg='white', fg='#088da5').place(x=500, y=190)

        frame3_sub = Frame(frame3, bd=4, relief=RIDGE, bg='white')
        frame3_sub.place(x=10, y=20, width=670, height=170)
            
        
        student_columns = ('SN', 'ROLL_NO', 'FIRST_NAME', 'LAST_NAME','CLASS', 'CONTACT', 'EMAIL_ID')
        scroll_x2 = Scrollbar(frame3_sub, orient=HORIZONTAL)
        scroll_y2 = Scrollbar(frame3_sub, orient=VERTICAL)
        student_table = ttk.Treeview(frame3_sub, columns=student_columns, xscrollcommand=scroll_x2.set, yscrollcommand=scroll_y2.set)     
        scroll_x2.pack(side=BOTTOM, fill=X)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_x2.config(command=student_table.xview)
        scroll_y2.config(command=student_table.yview)
        student_table.heading('SN', text='SL NO')
        student_table.heading('ROLL_NO', text='ROLL NO')
        student_table.heading('FIRST_NAME', text='FIRST NAME')
        student_table.heading('LAST_NAME', text='LAST NAME')
        student_table.heading('CLASS', text='CLASS')
        student_table.heading('CONTACT', text='CONTACT')
        student_table.heading('EMAIL_ID', text='EMAIL ID')        
        student_table['show'] = 'headings'
        student_table.column('SN', width=50)
        student_table.column('ROLL_NO', width=100)        
        student_table.column('FIRST_NAME', width=100)
        student_table.column('LAST_NAME', width=100)
        student_table.column('CLASS', width=100)
        student_table.column('CONTACT', width=100)
        student_table.column('EMAIL_ID', width=150)         
        student_table.pack(fill=BOTH, expand=1)         
            
     
        ############################################################################################################
           
        
        frame4 = Frame(frame1, bg='lightgray')
        frame4.place(x=840, y=70, width=400, height=500)
        view_title = Label(frame1, text='REAL TIME STATISTICS', font=('Goudy old style', 15, 'bold',), bg='blue', fg='white').place(x=850, y=60)
        
        frame4_sub = Frame(frame4, bd=4, relief=RIDGE, bg='white')
        frame4_sub.place(x=10, y=20, width=370, height=470)    
        
    def login_func(self):
        pass
    
    def add_user(self):
        self.t = Toplevel(self.root)       
        self.t.title('Libray Management System')
        self.t.geometry('400x550+300+100') 

        self.t.config(bg='lightgray')
        
        frame1 = Frame(self.t, bg='#EBF5FB')
        frame1.place(x=20, y=20, width=360, height=470)

        title = Label(self.t, text='ADD USER', font=('Goudy old style', 16, 'bold'), bg='white', fg='#088da5').place(x=140, y=4)
        
        save_button = Button(self.t, text='Save', width=10, command=self.add_user_save_func, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=120, y=500)
        cancel_button = Button(self.t, text='Cancel', width=10, command=self.self_close, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=240, y=500)

        title = Label(frame1, text='First Name', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=25)
        self.text_first_name = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_first_name.place(x=20, y=55)
        
        title = Label(frame1, text='Last Name', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=85)
        self.text_last_name = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_last_name.place(x=20, y=115)
        
        title = Label(frame1, text='Contact No', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=145)
        self.text_contact = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_contact.place(x=20, y=175)
        
        title = Label(frame1, text='Email ID', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=205)
        self.text_email = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_email.place(x=20, y=235)
        
        title = Label(frame1, text='Username', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=265)
        self.text_username = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_username.place(x=20, y=295)
        
        title = Label(frame1, text='Password', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=325)
        self.text_password = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_password.place(x=20, y=355)
        
        user_type = Label(frame1, text='User Type', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=385)
        self.user_type_q = ttk.Combobox(frame1, font=('Goudy old style', 15), state='readonly')
        self.user_type_q['value'] = ("Select", 'Librarian', 'Teacher', 'Administrator')
        self.user_type_q.place(x=20, y=415)
        self.user_type_q.current(0)
            
        
    def add_student(self):
        self.t = Toplevel(self.root)
        self.t.title('Libray Management System')

        self.t.geometry('400x550+300+100')        

        self.t.config(bg='lightgray')

        
        frame1 = Frame(self.t, bg='#EBF5FB')
        frame1.place(x=20, y=20, width=360, height=470)

        title = Label(self.t, text='ADD STUDENT', font=('Goudy old style', 16, 'bold'), bg='white', fg='#088da5').place(x=140, y=4)
        
        save_button = Button(self.t, text='Save', width=10, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=120, y=500)
        cancel_button = Button(self.t, text='Cancel', width=10, command=self.self_close, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=240, y=500)

        title = Label(frame1, text='First Name', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=25)
        self.text_first_name = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_first_name.place(x=20, y=55)
        
        title = Label(frame1, text='Last Name', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=85)
        self.text_last_name = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_last_name.place(x=20, y=115)
        
        user_type = Label(frame1, text='Class', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=145)
        self.user_type_q = ttk.Combobox(frame1, font=('Goudy old style', 15), state='readonly')
        self.user_type_q['value'] = ("Select", '+2', '+3', 'P.G.', 'BCA', 'MCA')
        self.user_type_q.place(x=20, y=175)
        self.user_type_q.current(0)
        
        user_type = Label(frame1, text='Stream', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=205)
        self.user_type_q = ttk.Combobox(frame1, font=('Goudy old style', 15), state='readonly')
        self.user_type_q['value'] = ("Select", 'Arts', 'Science', 'Commerce', 'Vocational')
        self.user_type_q.place(x=20, y=235)
        self.user_type_q.current(0)                
              
        title = Label(frame1, text='Roll No', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=265)
        self.text_password = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_password.place(x=20, y=295)        
        
        title = Label(frame1, text='Contact No', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=325)
        self.text_contact = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_contact.place(x=20, y=355)
        
        title = Label(frame1, text='Email ID', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=385)
        self.text_email = Entry(frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_email.place(x=20, y=415)

    def add_user_save_func(self):
        comboval = ['Librarian', 'Teacher', 'Administrator']
        if self.text_first_name.get() == "":
            messagebox.showerror("Error", "Please enter First Name", parent=self.t) 
        
        elif self.text_last_name.get() == "":
            messagebox.showerror("Error", "Please enter Last Name", parent=self.t) 
            
        elif self.text_contact.get() == "" :
            messagebox.showerror("Error", "Please enter the Contact No", parent=self.t)      
              
        elif self.text_username.get() == "" :
            messagebox.showerror("Error", "Please enter Username", parent=self.t)      
        
        elif self.text_password.get() == "" :
            messagebox.showerror("Error", "Please enter Password", parent=self.t)         
       
        elif self.user_type_q.get() not in comboval:
            messagebox.showerror("Error", "please select the 'User Type'", parent=self.t)
            
        else:
            try:
                mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
                mycursor = mydb.cursor()
                mycursor.execute("select COUNT(*) from user_list")
                for x in mycursor:
                    sl_no = x[0]
                sl_no_add = int(int(sl_no) + 1)
                print(sl_no_add)
                mycursor.execute("select * from user_list where username=%s ",(self.text_username.get()))
                row = mycursor.fetchone()                
                if row==None:
                    val = (sl_no_add, self.text_first_name.get(), self.text_last_name.get(), self.text_contact.get(), self.text_email.get(), self.text_username.get(), self.text_password.get(), self.user_type_q.get()) 
                    sql = "INSERT INTO user_list (sl_no, first_name, last_name, contact, email_id, username, password, user_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    print(val)
                    mycursor.execute(sql, val)                
                    mydb.commit()
                    if mycursor.rowcount == 1:
                        messagebox.showinfo("Success", "User saved successfully", parent=self.t)
                    mycursor.close()
                    self.fetch_user_table()
                    mydb.close()
                    print(sl_no_add)
                else:                                      
                    messagebox.showerror("Error", "Enter a different Username", parent=self.t)
         
            except Exception as es:
                messagebox.showerror("Error", f"The Error due to: {str(es)}", parent=self.t)   
        
        
        
    def self_close(self):
        self.t.destroy()
        
    def fetch_user_table(self):
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("select * from user_list")
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.user_table.delete(*self.user_table.get_children())
            for row in rows:
                    self.user_table.insert('', END, values=row)
            mydb.commit()
        mycursor.close()
        mydb.close()
        
    def delete_user_table(self):
        cursor_row = self.user_table.focus()
        contents = self.user_table.item(cursor_row)
        row = contents["values"]        
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("delete from user_list where username=%s ",(row[5]))
        mydb.commit()
        mycursor.close()
        mydb.close()
        self.fetch_user_table()
        
root = Tk()
obj = admin_page(root)
root.mainloop()

