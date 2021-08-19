from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
from PIL import Image, ImageTk 
import pymysql 
from tkinter.filedialog import askopenfile
import csv

class librarian_page:
    

    def __init__(self, root): 

        self.root = root
        self.root.title("Library Management System - Librarian's Panel")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #self.root.geometry('800x500+0+0')
        self.root.geometry(f'{screen_width}x{screen_height}+0+0')
        self.root.state('zoomed')

        self.root.config(bg='#EBF5FB')

        self.img= (Image.open("images\lms.png"))
        img_x, img_y = screen_width, screen_height - 50
        #img_x, img_y = 600, 400
        self.resized_image= self.img.resize((img_x, img_y), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(self.resized_image)        
        self.img_label = Label(self.root, image=self.new_image).place(x=0, y=0, relwidth=1, relheight=1)        

        frame1 = Frame(self.root, bg='#EBF5FB')
        frame1.place(x=40, y=40, width=img_x-60, height=img_y-80)

        title = Label(self.root, text='LIBRARIAN CONTROL PANEL', font=('Goudy old style', 20, 'bold',), bg='lightgray', fg='#088da5').place(x=450, y=20)

        ############################################################################################
        ############   BOOKS PANEL  ################################################################
        ############################################################################################
        
        frame2 = Frame(frame1, bg='lightgray')
        frame2.place(x=60, y=50, width=800, height=380)
        user_title = Label(frame1, text='BOOKS PANEL', font=('Goudy old style', 15, 'bold',), 
                         bg='blue', fg='white').place(x=70, y=40)
        button1 = Button(frame2, text='Add a Book', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', command=self.add_book).place(x=10, y=340)
        button2 = Button(frame2, text='Edit a Book', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5').place(x=120, y=340)
        button3 = Button(frame2, text='Delete a Book', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', command=self.delete_user_table).place(x=230, y=340)
        button4 = Button(frame2, text='Advance Search', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5').place(x=350, y=340)
        button5 = Button(frame2, text='Import Books', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', command=lambda:self.import_books()).place(x=480, y=340)
        button6 = Button(frame2, text='Export Books', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5').place(x=600, y=340)
        button7 = Button(frame2, text='R', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', command=self.fetch_user_table).place(x=720, y=340)


        frame2_sub = Frame(frame2, bd=4, relief=RIDGE, bg='white')
        frame2_sub.place(x=10, y=20, width=770, height=270)
        
        user_columns = ['SN', 'BOOK TITLE', 'BOOK CODE', 'TOTAL QTY', 'AVAILABLE QTY', 'DESCRIPTION', 
                           'AUTHOR', 'PUBLISHER', 'PRICE', 'CATEGORY', 'SUB_CATEGORY', 'CLASS', 'STREAM']
        scroll_x = Scrollbar(frame2_sub, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame2_sub, orient=VERTICAL)
        self.user_table = ttk.Treeview(frame2_sub, columns=user_columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)     
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)
        self.user_table.heading('SN', text='SL NO')
        self.user_table.heading('BOOK TITLE', text='TITLE OF THE BOOK')
        self.user_table.heading('BOOK CODE', text='BOOK ID/CODE')
        self.user_table.heading('TOTAL QTY', text='TOTAL QTY')
        self.user_table.heading('AVAILABLE QTY', text='AVAILABLE QTY')
        self.user_table.heading('DESCRIPTION', text='DESCRIPTION')
        self.user_table.heading('AUTHOR', text='AUTHOR')
        self.user_table.heading('PUBLISHER', text='PUBLISHER')
        self.user_table.heading('PRICE', text='PRICE')
        self.user_table.heading('CATEGORY', text='CATEGORY')
        self.user_table.heading('SUB_CATEGORY', text='SUB CATEGORY')
        self.user_table.heading('CLASS', text='CLASS')
        self.user_table.heading('STREAM', text='STREAM')
        self.user_table['show'] = 'headings'
        self.user_table.column('SN', width=50)
        self.user_table.column('BOOK TITLE', width=150)
        self.user_table.column('BOOK CODE', width=100)
        self.user_table.column('TOTAL QTY', width=80)
        self.user_table.column('AVAILABLE QTY', width=80)       
        self.user_table.column('DESCRIPTION', width=100)
        self.user_table.column('AUTHOR', width=150)
        self.user_table.column('PUBLISHER', width=100)
        self.user_table.column('PRICE', width=100)
        self.user_table.column('CATEGORY', width=100)
        self.user_table.column('SUB_CATEGORY', width=100)
        self.user_table.column('CLASS', width=100)
        self.user_table.column('STREAM', width=100)
        self.user_table.pack(fill=BOTH, expand=1) 
        self.fetch_user_table()
        
        frame2_sub2 = Frame(frame2, bg='#EBF5FB')
        frame2_sub2.place(x=10, y=290, width=770, height=40)
        
        frame2_sub2_title = Label(frame2_sub2 , text='Enter Book ID/CODE :', font=('Goudy old style', 13), 
                                  bg='#EBF5FB', fg='#088da5').place(x=5, y=5)
        frame2_sub2_entry = Entry(frame2_sub2 , text='', font=('Goudy old style', 13), 
                                  bg='white', width=12).place(x=175, y=5)
        frame2_sub2_button = Button(frame2_sub2, text='Search', font=('Goudy old style', 12, 'bold'), 
                                  bg='#EBF5FB', fg='#088da5', width=8, height=1 ).place(x=290, y=1)
        
        frame2_sub2_title2 = Label(frame2_sub2 , text='Enter Book Title :', font=('Goudy old style', 13), 
                                  bg='#EBF5FB', fg='#088da5').place(x=380, y=5)
        frame2_sub2_entry2 = Entry(frame2_sub2 , text='', font=('Goudy old style', 13), 
                                  bg='white', width=18).place(x=505, y=5)
        frame2_sub2_button2 = Button(frame2_sub2, text='Search', font=('Goudy old style', 12, 'bold'), 
                                  bg='#EBF5FB', fg='#088da5', width=8, height=1 ).place(x=675, y=1)


        ########################################################################################################### 
        ###################### LIBRARY STATISTICS #################################################################
        ###########################################################################################################
        
        self.no_of_books()
        
        frame4 = Frame(frame1, bg='lightgray')
        frame4.place(x=880, y=50, width=390, height=500)

        frame4_sub = Frame(frame4, bd=4, relief=RIDGE, bg='white')
        frame4_sub.place(x=10, y=20, width=360, height=470)    

        view_title = Label(frame1, text='LIBRARY STATISTICS', font=('Goudy old style', 15, 'bold',), 
                           bg='blue', fg='white').place(x=890, y=40)
        total_books = Label(frame4_sub, text='Total Nos of Books', font=('Goudy old style', 15, 'bold',), 
                           bg='#EBF5FB', fg='#088da5').place(x=100, y=20)
        tbc = Label(frame4_sub, text="00"+str(self.total_no_of_books), font=('Goudy old style', 15, 'bold',), 
                           bg='white', fg='blue').place(x=140, y=60)       
        issued_books = Label(frame4_sub, text='Nos of Books Issued', font=('Goudy old style', 15, 'bold',), 
                           bg='#EBF5FB', fg='#088da5').place(x=100, y=100)
        ibc = Label(frame4_sub, text="00"+str(self.total_books_issued), font=('Goudy old style', 15, 'bold',), 
                           bg='white', fg='green').place(x=140, y=140)
        overdue_books = Label(frame4_sub, text='Overdue Books to Return', font=('Goudy old style', 15, 'bold',), 
                           bg='#EBF5FB', fg='#088da5').place(x=80, y=180)
        obc = Label(frame4_sub, text='0085', font=('Goudy old style', 15, 'bold',), 
                           bg='white', fg='red').place(x=150, y=220)        
        ubn = Label(frame4_sub, text='Total Unique Books', font=('Goudy old style', 15, 'bold',), 
                           bg='#EBF5FB', fg='#088da5').place(x=100, y=260)
        ubn2 = Label(frame4_sub, text="00"+str(self.total_unique_books), font=('Goudy old style', 15, 'bold',), 
                           bg='white', fg='red').place(x=150, y=300)    
        ########################################################################################################### 
        ###################### BOOK ISSUE and SUB-PANELS###########################################################
        ###########################################################################################################
        
        
        frame5 = Frame(frame1, bg='lightgray')
        frame5.place(x=60, y=450, width=200, height=160)
        
        button1_f5 = Button(frame5, text='Issue Book', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=10)
        button2_f5 = Button(frame5, text='Retreive Book', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=60)
        button3_f5 = Button(frame5, text='Overdue Books', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=110)
        
        frame6 = Frame(frame1, bg='lightgray')
        frame6.place(x=300, y=450, width=200, height=160)
        
        button1_f6 = Button(frame6, text='Book Categories', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=10)
        button2_f6 = Button(frame6, text='Authors', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=60)
        button3_f6 = Button(frame6, text='Publishers', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=110)
        
        frame7 = Frame(frame1, bg='lightgray')
        frame7.place(x=540, y=450, width=200, height=160)
        
        button1_f7 = Button(frame7, text='Notifications', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=10)
        button2_f7 = Button(frame7, text='Fines', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=60)
        button3_f7 = Button(frame7, text='Students', font=('Goudy old style', 13, 'bold'), 
                         bg='white', fg='#088da5', width=12).place(x=20, y=110)

        ############################################################################################################
        ########################################   FUNCTIONS     ###################################################
        ############################################################################################################
    
    def add_book(self):    
        self.t = Toplevel(self.root)
        self.t.title('Libray Management System')

        self.t.geometry('780x600+200+30')        

        self.t.config(bg='lightgray')


        ab_frame1 = Frame(self.t, bg='#EBF5FB')
        ab_frame1.place(x=20, y=20, width=360, height=520)

        title = Label(self.t, text='ADD BOOK', font=('Goudy old style', 16, 'bold'), bg='white', fg='#088da5').place(x=140, y=4)

        save_button = Button(self.t, text='Save', width=10, command=self.save_button, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=520, y=550)
        cancel_button = Button(self.t, text='Cancel', width=10, command=self.self_close, font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=640, y=550)

        title = Label(ab_frame1, text='Title of the Book', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=25)
        self.text_first_name = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_first_name.place(x=20, y=55)

        title = Label(ab_frame1, text='Book Code/ID', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=85)
        self.text_last_name = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_last_name.place(x=20, y=115)

        title = Label(ab_frame1, text='Description', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=145)
        self.text_password = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_password.place(x=20, y=175)  

        title = Label(ab_frame1, text='Author of the Book', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=205)
        self.text_password = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_password.place(x=20, y=235)        

        title = Label(ab_frame1, text='Publisher Name', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=265)
        self.text_contact = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=35, borderwidth=2)
        self.text_contact.place(x=20, y=295)

        title = Label(ab_frame1, text='Price', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=325)
        self.text_email = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=15, borderwidth=2)
        self.text_email.place(x=20, y=355) 
        
        title = Label(ab_frame1, text='Quantity', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=200, y=325)
        self.text_email = Entry(ab_frame1, font=('times new roman', 13), bg='white', width=15, borderwidth=2)
        self.text_email.place(x=200, y=355)  

        user_type = Label(ab_frame1, text='Category of the Book', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=385)
        self.user_type_q = ttk.Combobox(ab_frame1, font=('Goudy old style', 15), state='readonly')
        self.user_type_q['value'] = ("Select", 'Arts', 'Science', 'Commerce', 'Vocational')
        self.user_type_q.place(x=20, y=415)
        self.user_type_q.current(0)

        user_type = Label(ab_frame1, text='Class', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=20, y=445)
        self.user_type_q = ttk.Combobox(ab_frame1, font=('Goudy old style', 15), state='readonly', width=12)
        self.user_type_q['value'] = ("Select", '+2', '+3', 'P.G.', 'BCA', 'MCA')
        self.user_type_q.place(x=20, y=475)
        self.user_type_q.current(0)

        user_type = Label(ab_frame1, text='Stream', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=190, y=445)
        self.user_type_q = ttk.Combobox(ab_frame1, font=('Goudy old style', 15), state='readonly', width=12)
        self.user_type_q['value'] = ("Select", 'Arts', 'Science', 'Commerce', 'Vocational')
        self.user_type_q.place(x=190, y=475)
        self.user_type_q.current(0) 

        ab_frame2 = Frame(self.t, bg='#EBF5FB')
        ab_frame2.place(x=400, y=20, width=360, height=520)

        title = Label(ab_frame2, text='*PICTURE OF THE BOOK*', font=('Goudy old style', 12, 'bold'), bg='#EBF5FB', fg='#088da5').place(x=70, y=25)
        button1 = Button(ab_frame2, text='<<', width=3, font=('Goudy old style', 13, 'bold'),bd=0, bg='#EBF5FB', fg='#088da5').place(x=10, y=200)
        button2 = Button(ab_frame2, text='>>', width=3, font=('Goudy old style', 13, 'bold'),bd=0, bg='#EBF5FB', fg='#088da5').place(x=310, y=200)

        self.frame2_sub = Frame(ab_frame2, bd=3, relief=RIDGE, bg='#EBF5FB')
        self.frame2_sub.place(x=45, y=50, width=265, height=370)

        ab_btn = Button(ab_frame2, text ='Browse', width=8, command = lambda:self.open_file()).place(x=260, y=440)
        btn_title = Label(ab_frame2, text='File:', font=('Goudy old style', 13, 'bold'), bg='#EBF5FB', 
                          fg='#088da5').place(x=40, y=440)

        self.ab_btn_entry = Entry(ab_frame2, font=('times new roman', 13), bg='white', width=20, borderwidth=2)
        self.ab_btn_entry.place(x=80, y=440)


    def self_close(self):
        self.t.destroy()

    def open_file(self):       

        book_img_file = askopenfile(mode ='r', filetypes =[('Image Files', ['*.jpg','*.png', '*.gif',])])       
        if book_img_file is not None:             
            print(book_img_file.name)
            self.ab_btn_entry.delete(0, END)
            self.ab_btn_entry.insert(0, book_img_file.name)
            self.book_img= (Image.open(book_img_file.name))
            book_img_width, book_img_height = self.book_img.size
            x = book_img_width/220
            y = book_img_height/x
            img_x, img_y = 220, int(y)
            self.resized_book_image= self.book_img.resize((img_x, img_y), Image.ANTIALIAS)
            self.new_book_image= ImageTk.PhotoImage(self.resized_book_image)        
            self.book_img_label = Label(self.frame2_sub, image=self.new_book_image).place(x=0, y=0, relwidth=1, relheight=1)        
            messagebox.showinfo("Success", "Image has been successfully imported", parent=self.t)

        else:
            messagebox.showerror("Error", "No file has been selected", parent=self.t)

    def save_button(self):
        messagebox.showerror("Hello", "You clicked save button", parent=self.root)
        
    def import_books(self):
        ib_user_columns = ['SN', 'BOOK TITLE', 'BOOK CODE', 'TOTAL QTY', 'AVAILABLE QTY', 'DESCRIPTION', 
                           'AUTHOR', 'PUBLISHER', 'PRICE', 'CATEGORY', 'SUB_CATEGORY', 'CLASS', 'STREAM']
        self.ib = Toplevel(self.root)
        self.ib.title('Import CSV file')
        self.ib.geometry('800x350+200+30')
        self.ib.config(bg='lightgray')
        ib_title = Label(self.ib, text='Preview of the File:', font=('Goudy old style', 16, 'bold'), bg='#EBF5FB', 
                      fg='#088da5').place(x=10, y=10)

        ib_frame2_sub = Frame(self.ib, bd=4, relief=RIDGE, bg='white')
        ib_frame2_sub.place(x=10, y=40, width=770, height=250)

        ib_scroll_x = Scrollbar(ib_frame2_sub, orient=HORIZONTAL)
        ib_scroll_y = Scrollbar(ib_frame2_sub, orient=VERTICAL)
        ib_user_table = ttk.Treeview(ib_frame2_sub, columns=ib_user_columns, xscrollcommand=ib_scroll_x.set, yscrollcommand=ib_scroll_y.set)     
        ib_scroll_x.pack(side=BOTTOM, fill=X)
        ib_scroll_y.pack(side=RIGHT, fill=Y)
        ib_scroll_x.config(command=ib_user_table.xview)
        ib_scroll_y.config(command=ib_user_table.yview)
        ib_user_table.heading('SN', text='SL NO')
        ib_user_table.heading('BOOK TITLE', text='TITLE OF THE BOOK')
        ib_user_table.heading('BOOK CODE', text='BOOK ID/CODE')
        ib_user_table.heading('TOTAL QTY', text='TOTAL QTY')
        ib_user_table.heading('AVAILABLE QTY', text='AVAILABLE QTY')
        ib_user_table.heading('DESCRIPTION', text='DESCRIPTION')
        ib_user_table.heading('AUTHOR', text='AUTHOR')
        ib_user_table.heading('PUBLISHER', text='PUBLISHER')
        ib_user_table.heading('PRICE', text='PRICE')
        ib_user_table.heading('CATEGORY', text='CATEGORY')
        ib_user_table.heading('SUB_CATEGORY', text='SUB CATEGORY')
        ib_user_table.heading('CLASS', text='CLASS')
        ib_user_table.heading('STREAM', text='STREAM')
        ib_user_table['show'] = 'headings'
        ib_user_table.column('SN', width=50)
        ib_user_table.column('BOOK TITLE', width=150)
        ib_user_table.column('BOOK CODE', width=100)
        ib_user_table.column('TOTAL QTY', width=80)
        ib_user_table.column('AVAILABLE QTY', width=80)       
        ib_user_table.column('DESCRIPTION', width=100)
        ib_user_table.column('AUTHOR', width=150)
        ib_user_table.column('PUBLISHER', width=100)
        ib_user_table.column('PRICE', width=100)
        ib_user_table.column('CATEGORY', width=100)
        ib_user_table.column('SUB_CATEGORY', width=100)
        ib_user_table.column('CLASS', width=100)
        ib_user_table.column('STREAM', width=100)
        ib_user_table.pack(fill=BOTH, expand=1) 

        btn_ib_frame2_sub2 = Button(self.ib, text='Import', font=('Goudy old style', 12, 'bold'), 
                              bg='#EBF5FB', fg='#088da5', width=8, height=1, command=self.import_to_db).place(x=575, y=300)

        btn2_ib_frame2_sub2 = Button(self.ib, text='Cancel', font=('Goudy old style', 12, 'bold'), 
                              bg='#EBF5FB', fg='#088da5', width=8, height=1, command=self.close_ib).place(x=675, y=300)
        
        self.rows = []
        book_csv_file = askopenfile(mode ='r', filetypes =[('csv files', ['*.csv'])])       
        if book_csv_file is not None:      
            with open(book_csv_file.name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')                            
                for row in csv_reader:
                    self.rows.append(row)                                    
                if self.rows[0] != ib_user_columns:
                    messagebox.showerror("Error", "This file can be Imported", parent=self.ib)
                else:
                    for row in self.rows[1:]:
                        ib_user_table.insert('', END, values=row)       
                    messagebox.showinfo("Success", "please check the data before Import", parent=self.ib)

            
    def import_to_db(self):
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("select COUNT(*) from books")
        for x in mycursor:
            sl_no = x[0]
            sl_no_add = int(int(sl_no) + 1)
            sl_no_addc = sl_no_add
        #for i in range(len(self.rows[1:])):
        for i in range(len(self.rows[1:])):
            mycursor.execute("select * from books where book_id=%s ",(self.rows[1:][i][2]))
            row_db = mycursor.fetchone()
            if row_db!=None:
                messagebox.showerror("Error", f"Entry already exist:\n Book Title - {self.rows[1:][i][1]}\n Book Code - {self.rows[1:][i][2]}", parent=self.ib)
            elif row_db==None:                
                row = self.rows[1:][i]
                val = (sl_no_addc,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]) 
                sql = "INSERT INTO books (sl_no, book_title, book_id, total_qty, available_qty, descr, author, publisher, price,category,sub_category,class,stream) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(sql, val)                
                mydb.commit()                
                sl_no_addc = sl_no_addc + 1
            else:
                pass
            #if mycursor.rowcount == 1:
            #messagebox.showinfo("Success", "User saved successfully", parent=self.t)
        mycursor.execute("select COUNT(*) from books")
        for x in mycursor:
            sl_no_new = x[0]
            sl_no_add_new = int(int(sl_no_new) + 1)
        added_books = sl_no_add_new - sl_no_add
        messagebox.showinfo("Success", f"No of Books added successfully: {added_books}", parent=self.ib)
        mycursor.close()
        #self.fetch_user_table()
        mydb.close()
        print(sl_no_add)
      
    def close_ib(self):
        self.ib.destroy()     
        
    def fetch_user_table(self):
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("select * from books")
        rows = mycursor.fetchall()
        if len(rows)!=0:
            self.user_table.delete(*self.user_table.get_children())
            for row in rows:
                    self.user_table.insert('', END, values=row)
            mydb.commit()
        if len(rows)==0:
            self.user_table.delete(*self.user_table.get_children())
        mycursor.close()
        mydb.close()
        
    def delete_user_table(self):
        cursor_row = self.user_table.focus()
        contents = self.user_table.item(cursor_row)
        row = contents["values"]        
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("delete from books where book_id=%s ",(row[2]))
        mydb.commit()
        mycursor.close()
        mydb.close()
        self.fetch_user_table()
    def no_of_books(self):
        mydb = pymysql.connect(host='localhost', user='lms_user', password='lms@123',database='lms_2')
        mycursor = mydb.cursor()
        mycursor.execute("select COUNT(*) from books")
        for x in mycursor:
            self.total_unique_books = x[0]
        
        mycursor.execute("SELECT total_qty FROM books")
        myresult = mycursor.fetchall()
        self.total_no_of_books = 0
        for x in myresult:
            self.total_no_of_books = self.total_no_of_books + x[0]
        
        mycursor.execute("SELECT available_qty FROM books")
        myresult2 = mycursor.fetchall()
        self.total_available_books = 0
        for x in myresult2:
            self.total_available_books = self.total_available_books + x[0]
        self.total_books_issued = self.total_no_of_books - self.total_available_books
        
        
root = Tk() 
obj = librarian_page(root) 
root.mainloop()
