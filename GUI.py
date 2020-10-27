from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class StudentSoft:
    def __init__(self, root):

        self.root = root
        self.root['background']='grey'
        self.title = Label(self.root, text="Student Management System", bg='black', fg='white', bd=10, relief=GROOVE,
                           font=("times new roman", 40, 'bold'))
        self.title.pack(side=TOP, fill=X)

        # ========Varialbe===

        self.namevar = StringVar()
        self.contactvar = StringVar()
        self.rollvar = StringVar()
        self.addressvar = StringVar()
        self.dobvarvar = StringVar()
        self.emailvar = StringVar()
        self.gendervar = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        # ========Manage Frame
        self.Manage_Frame = Frame(self.root, height=600, width=450, relief=RIDGE, bg='grey')
        self.Manage_Frame.place(x=20, y=100)
        self.Manage_Frame.grid_propagate(False)
        self.m_title = Label(self.Manage_Frame, font=('times new Roman', 20, 'bold underline'), text="Manage Students")
        self.m_title.grid(row=0, columnspan=2, pady=20)
        self.lbl_roll = Label(self.Manage_Frame, text="Roll Number", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_roll.grid(row=1, column=0, pady=10, padx=10)
        # =========================entry field
        self.entry_roll = Entry(self.Manage_Frame, width=20, font=('times new roman', 15), textvariable=self.rollvar)
        self.entry_roll.grid(row=1, column=1, pady=10, padx=20)
        self.lbl_Name = Label(self.Manage_Frame, text="Name", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_Name.grid(row=2, column=0, pady=10, padx=10, sticky=W)
        self.entry_Name = Entry(self.Manage_Frame, width=20, font=('times new roman', 15), textvariable=self.namevar)
        self.entry_Name.grid(row=2, column=1, pady=10, padx=10)
        self.lbl_email = Label(self.Manage_Frame, text="Email", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_email.grid(row=3, column=0, pady=10, padx=10, sticky=W)
        self.entry_email = Entry(self.Manage_Frame, width=20, font=('times new roman', 15), textvariable=self.emailvar)
        self.entry_email.grid(row=3, column=1, pady=10, padx=10)
        self.lbl_gender = Label(self.Manage_Frame, text='Gender', font=('times new roman', 15, 'bold'), fg='black')
        self.lbl_gender.grid(row=4, column=0, pady=10, padx=10, sticky=W)
        self.combo_gender = ttk.Combobox(self.Manage_Frame, font=('times new Roman', 13, 'bold'),
                                         values=('Male', 'Female', 'Other'), state='readonly',
                                         textvariable=self.gendervar)
        self.combo_gender.grid(row=4, column=1)

        self.lbl_contact = Label(self.Manage_Frame, text="Contanct", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_contact.grid(row=5, column=0, pady=10, padx=10, sticky=W)
        self.entry_contact = Entry(self.Manage_Frame, width=20, font=('times new roman', 15),
                                   textvariable=self.contactvar)
        self.entry_contact.grid(row=5, column=1, pady=10, padx=10)
        self.lbl_dob = Label(self.Manage_Frame, text="D.O.B", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_dob.grid(row=6, column=0, pady=10, padx=10, sticky=W)
        self.entry_dob = Entry(self.Manage_Frame, width=20, font=('times new roman', 15), textvariable=self.dobvarvar)
        self.entry_dob.grid(row=6, column=1, pady=10, padx=10)
        self.lbl_address = Label(self.Manage_Frame, text="Address", fg='black', font=('times new roman', 15, 'bold'))
        self.lbl_address.grid(row=7, column=0, pady=10, padx=10, sticky=W)
        self.txt_address = Text(self.Manage_Frame, height=5, width=20, bd=10)
        self.txt_address.grid(row=7, column=1, padx=30)
        # =========ButtonFrame
        self.butt_frame = Frame(self.Manage_Frame, bg='grey', height=2)
        self.butt_frame.place(x=20, y=500, width=350)
        self.buADD = Button(self.butt_frame, text='ADD', height=2, width=5, command=self.add_student)
        self.buADD.grid(row=0, column=0, padx=20)
        self.buUPP = Button(self.butt_frame, text='Update', height=2, width=5,command=self.update_v)
        self.buUPP.grid(row=0, column=1, padx=20)
        self.buDEL = Button(self.butt_frame, text='Delete', height=2, width=5,command=self.delete_data)
        self.buDEL.grid(row=0, column=2, padx=20)
        self.buCL = Button(self.butt_frame, text='Clear', height=2, width=5,command=self.clear)
        self.buCL.grid(row=0, column=3, padx=20)

        # =======Detail Frame

        self.Detail_Frame = Frame(self.root, height=550, width=820, relief=RIDGE, bg='grey')
        self.Detail_Frame.place(x=500, y=100)
        self.Detail_Frame.grid_propagate(False)
        self.lbl_search = Label(self.Detail_Frame, text='Search By', font=('times new Roman', 30, 'bold'), fg='Black',
                                bg='grey')
        self.lbl_search.grid(row=0, column=0, pady=10, padx=20)

        self.combo_search = ttk.Combobox(self.Detail_Frame, width=10, font=('times new roman', 10, 'bold'),
                                         values=('Name', 'Roll_no', 'Contact'), state='readonly', textvariable=self.search_by)
        self.combo_search.grid(row=0, column=1, pady=10, padx=20)
        self.search_entry = Entry(self.Detail_Frame,textvariable=self.search_txt, font=('times new Roman', 15))
        self.search_entry.grid(row=0, column=3, pady=10, padx=20)

        self.ser_butt1 = Button(self.Detail_Frame, text='SEARCH', width=10,command=self.search).grid(row=0, column=4, pady=10, padx=10)
        self.ser_butt2 = Button(self.Detail_Frame, text='Show ALL', width=10,command=self.fetch_data).grid(row=0, column=5, pady=10, padx=10)
        # ===============Table Frame
        self.table_frame = Frame(self.Detail_Frame, bg='white', height=500, width=400)
        self.table_frame.place(x=10, y=70, width=800, height=455)
        self.scrollx = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scrolly = Scrollbar(self.table_frame, orient=VERTICAL)
        self.studenttable = ttk.Treeview(self.table_frame,
                                         column=('Roll no', 'Name', 'Gender', 'Contact', 'Email', 'dob', 'Address'),
                                         xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set,
                                         show='headings')
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.config(command=self.studenttable.xview)
        self.scrolly.config(command=self.studenttable.yview)
        self.studenttable.heading('Roll no', text='Roll no')
        self.studenttable.heading('Name', text='Name')
        self.studenttable.heading('Gender', text='Gender')
        self.studenttable.heading('Contact', text='Contact')
        self.studenttable.heading('Email', text='Email')
        self.studenttable.heading('dob', text='Address')
        self.studenttable.heading('Address', text='DOB')
        self.studenttable.column('Roll no', width=50)
        self.studenttable.column('Name', width=100)
        self.studenttable.column('Gender', width=100)
        self.studenttable.column('Contact', width=100)
        self.studenttable.column('Email', width=100)
        self.studenttable.column('dob', width=100)
        self.studenttable.column('Address', width=100)
        self.studenttable.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.studenttable.bind('<ButtonRelease-1>',self.get_cursor)

    def add_student(self):
        if self.namevar.get()=="" or self.rollvar.get=="" or self.txt_address.get('1.0',END)=="" or self.gendervar.get()=="" or self.contactvar.get()=="" or self.dobvarvar.get=="" or self.emailvar.get()=="":
            messagebox.showerror('ERROR','All Feilds are required')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='stm')
                cur = con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.rollvar.get(), self.namevar.get(), self.gendervar.get(), self.contactvar.get(),
                    self.emailvar.get(),
                    self.txt_address.get('1.0', END), self.dobvarvar.get()))
                con.commit()
                self.fetch_data()
                con.close()
                self.clear()
                messagebox.showinfo('Success', 'Records are added sucessfuly')
            except pymysql.err.IntegrityError:
                messagebox.showerror("Sorry","This Roll no is already exist")




    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', database='stm')
        cur = con.cursor()
        cur.execute('select * from students')
        rows = cur.fetchall()
        if len(rows)==0:
            messagebox.showerror("Sorry","No Data Found")
        if len(rows) != 0:
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('', END, values=row)
            con.commit()
        con.close()
    def clear(self):
        self.addressvar.set(' ')
        self.txt_address.delete('1.0',END)
        self.dobvarvar.set(' ')
        self.namevar.set(' ')
        self.emailvar.set(' ')
        self.rollvar.set(' ')
        self.contactvar.set(' ')
        self.gendervar.set(' ')
    def get_cursor(self,ev):
        cursor=self.studenttable.focus()
        content=self.studenttable.item(cursor)
        row=content['values']
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[5])
        self.dobvarvar.set(row[6])
        self.namevar.set(row[1])
        self.emailvar.set(row[4])
        self.rollvar.set(row[0])
        self.contactvar.set(row[3])
        self.gendervar.set(row[2])
    def update_v(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('UPDATE students SET name=%s,gender=%s,contact=%s,email=%s,address=%s,dob=%s WHERE roll_no=%s' , (self.namevar.get(), self.gendervar.get(), self.contactvar.get(), self.emailvar.get(),
        self.txt_address.get('1.0',END),self.dobvarvar.get(),self.rollvar.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute('DELETE FROM students WHERE roll_no=%s',(self.rollvar.get()))
        con.commit()
        self.fetch_data()
        self.clear()
    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE "+(self.search_by.get())+" = '"+(self.search_txt.get())+"';")
        rows = cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("Sorry","Not Found")
        else:
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('',END,values=row)
            con.commit()
        con.close()





root = Tk()
root.title("Student Management System")
root.geometry("1350x700")
root.propagate(0)
root.wm_iconbitmap("education.ico")
obj = StudentSoft(root)
root.mainloop()
