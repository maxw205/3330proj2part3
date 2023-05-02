import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
import sqlite3
import random


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, TablePage, Publisher, Book, BookCopies, Borrower, BookLoans):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Insert",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select your table", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=rows[0],
                           command=lambda: controller.show_frame("Publisher"))
        button1 = tk.Button(self, text=rows[1],
                           command=lambda: controller.show_frame("TablePage"))
        button2 = tk.Button(self, text=rows[2],
                           command=lambda: controller.show_frame("Borrower"))
        button3 = tk.Button(self, text=rows[3],
                           command=lambda: controller.show_frame("Book"))
        button4 = tk.Button(self, text=rows[4],
                           command=lambda: controller.show_frame("BookLoans"))
        button5 = tk.Button(self, text=rows[5],
                           command=lambda: controller.show_frame("BookCopies"))
        button6 = tk.Button(self, text=rows[6],
                           command=lambda: controller.show_frame("TablePage"))
        button.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()

class Publisher(tk.Frame):

    #Publisher_Name varchar(255) primary key,
    #Phone varchar(255),
    #Address varchar(255)

    def __init__(self, parent, controller):
        
        def submit():
            conn = sqlite3.connect('LMS.db')
            conn_cursor=conn.cursor()
            conn_cursor.execute("INSERT INTO PUBLISHER VALUES (:Publisher_Name, :Phone, :Address)",
                            {
                                'Publisher_Name': Publisher_Name.get(),
                                'Phone': Phone.get(),
                                'Address': Address.get()
                            })
            conn.commit()
            conn.close()
            print(Phone.get())
            
        def showValues():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT * FROM PUBLISHER")
            records = iq_cur.fetchall()
            print_records = ''
            for record in records:
                print_records+= str(record[0] + " " + record[1]+ " " + record[2] + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=9,column=0,columnspan=2)
            iq.close()
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Publisher Table", font=controller.title_font)
        label.grid(row = 0, column = 0, pady = 10)
        
        Publisher_Name_label = Label(self, text = 'Publisher Name')
        Publisher_Name_label.grid(row = 1, column = 0)
        Publisher_Name = Entry(self, width = 30)
        Publisher_Name.grid(row = 1, column = 1, padx = 30)
        
        Phone_Label = Label(self, text = 'Phone')
        Phone_Label.grid(row = 2, column = 0)
        Phone = Entry(self, width = 30)
        Phone.grid(row = 2, column = 1, padx = 30)
        
        Address_label = Label(self, text = 'Address')
        Address_label.grid(row = 3, column = 0)
        Address = Entry(self, width = 30)
        Address.grid(row = 3, column = 1, padx = 30)
        
        button = tk.Button(self, text="Insert Values", command=submit)
        button.grid(row = 4, column = 1, padx = 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 5, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Values", command=showValues)
        button.grid(row = 6, column = 1, padx = 30)

class Borrower(tk.Frame):

    def __init__(self, parent, controller):
        
        def submit():
            conn = sqlite3.connect('LMS.db')
            conn_cursor=conn.cursor()
            nullCard = 0
            hereCard_No = Card_No.get()
            if hereCard_No == '':
                hereCard_No = random.randrange(100000,999999)
                nullCard = 1
            conn_cursor.execute("INSERT INTO BORROWER VALUES (:Card_No, :Name, :Address, :Phone)",
                            {
                                'Card_No': hereCard_No,
                                'Name': Name.get(),
                                'Address': Address.get(),
                                'Phone': Phone.get(),
                            })
            conn.commit()
            conn.close()
            if nullCard == 1:
                cardNo = "Here is your generated card number:" + str(hereCard_No)
                label = Label(self,text=cardNo)
                label.grid(row=9,column=0,columnspan=2)
            print(Name.get())
            
        def showValues():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT * FROM BORROWER")
            records = iq_cur.fetchall()
            print_records = ''
            for record in records:
                print_records+= str(str(record[0]) + "|" + record[1]+ "|" + record[2] + "|" + record[3] + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=9,column=0,columnspan=2)
            iq.close()

        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Borrower Table", font=controller.title_font)
        label.grid(row = 0, column = 0, pady = 10)
        
        Card_No_Label = Label(self, text = 'Card No')
        Card_No_Label.grid(row = 1, column = 0)
        Card_No = Entry(self, width = 30)
        Card_No.grid(row = 1, column = 1, padx = 30)
        
        Name_Label = Label(self, text = 'Name')
        Name_Label.grid(row = 2, column = 0)
        Name = Entry(self, width = 30)
        Name.grid(row = 2, column = 1, padx = 30)
        
        Address_label = Label(self, text = 'Address')
        Address_label.grid(row = 3, column = 0)
        Address = Entry(self, width = 30)
        Address.grid(row = 3, column = 1, padx = 30)
        
        Phone_label = Label(self, text = 'Phone')
        Phone_label.grid(row = 4, column = 0)
        Phone = Entry(self, width = 30)
        Phone.grid(row = 4, column = 1, padx = 30)
        
        button = tk.Button(self, text="Insert Values", command=submit)
        button.grid(row = 5, column = 1, padx = 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 6, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Values", command=showValues)
        button.grid(row = 7, column = 1, padx = 30)

class Book(tk.Frame):

    #Publisher_Name varchar(255) primary key,
    #Phone varchar(255),
    #Address varchar(255)

    def __init__(self, parent, controller):
        
        def submit():
            conn = sqlite3.connect('LMS.db')
            conn_cursor=conn.cursor()
            conn_cursor.execute("INSERT INTO BOOK VALUES (:Book_Id, :Title, :Publisher_Title)",
                            {
                                'Book_Id': Book_Id.get(),
                                'Title': Title.get(),
                                'Publisher_Title': Publisher_Title.get()
                            })
            conn.commit()
            conn.close()
            print(Title.get())
            
        def showValues():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT * FROM BOOK")
            records = iq_cur.fetchall()
            print_records = ''
            for record in records:
                print_records+= str(str(record[0]) + "|" + record[1]+ "|" + record[2] + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=9,column=0,columnspan=2)
            iq.close()
        
        def query4():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT count(Book_Id), Branch_Id FROM BOOK_LOANS NATURAL JOIN BOOK WHERE Title = (:Title) GROUP BY Branch_Id",
                           {
                               'Title': Title.get()
                           })
            records = iq_cur.fetchall()
            print_records = 'No Of Copies|BranchId\n'
            for record in records:
                print_records+= str(str(record[0]) + "|" + str(record[1]) + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=9,column=0,columnspan=2)
            iq.close()
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Book Table", font=controller.title_font)
        label.grid(row = 0, column = 0, pady = 10)
        
        Book_Id_Label = Label(self, text = 'Book ID')
        Book_Id_Label.grid(row = 1, column = 0)
        Book_Id = Entry(self, width = 30)
        Book_Id.grid(row = 1, column = 1, padx = 30)
        
        Title_Label = Label(self, text = 'Title')
        Title_Label.grid(row = 2, column = 0)
        Title = Entry(self, width = 30)
        Title.grid(row = 2, column = 1, padx = 30)
        
        Publisher_Title_label = Label(self, text = 'Publisher Title')
        Publisher_Title_label.grid(row = 3, column = 0)
        Publisher_Title = Entry(self, width = 30)
        Publisher_Title.grid(row = 3, column = 1, padx = 30)
        
        button = tk.Button(self, text="Insert Values", command=submit)
        button.grid(row = 4, column = 1, padx = 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 5, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Values", command=showValues)
        button.grid(row = 6, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Loaned Amount From Title", command=query4)
        button.grid(row = 7, column = 1, padx = 30)
        
class BookLoans(tk.Frame):

    #Publisher_Name varchar(255) primary key,
    #Phone varchar(255),
    #Address varchar(255)

    def __init__(self, parent, controller):
        
        def submit():
            conn = sqlite3.connect('LMS.db')
            conn_cursor=conn.cursor()
            conn_cursor.execute("INSERT INTO BOOK_LOANS VALUES (:Book_Id, :Branch_Id, :Card_No, :Date_Out, :Due_Date, :Returned_date)",
                            {
                                'Book_Id': Book_Id.get(),
                                'Branch_Id': Branch_Id.get(),
                                'Card_No': Card_No.get(),
                                'Date_Out': Date_Out.get(),
                                'Due_Date': Due_Date.get(),
                                'Returned_date': Returned_date.get()
                            })
            conn_cursor.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies-1 WHERE Book_Id = :Book_Id",
                                {
                                    'Book_Id': Book_Id.get(),
                                })
            conn.commit()
            conn.close()
            print(Due_Date.get())
            
        def showValues():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT * FROM BOOK_LOANS")
            records = iq_cur.fetchall()
            print_records = 'Book_Id|Branch_Id|Card_No|Date_Out|Due_Date|Returned_Date|Late?\n'
            for record in records:
                print_records+= str(str(record[0]) + "|" + str(record[1])+ "|" + str(record[2]) + "|" + record[3] + "|" + record[4] + "|" + record[5] + "|" + str(record[6]) + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=11,column=0,columnspan=2)
            iq.close()
            
        def showLate():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT *, julianday(Returned_date) - julianday(Due_Date) FROM BOOK_LOANS WHERE (julianday(Returned_date) - julianday(Due_Date)) > 0 ")
            records = iq_cur.fetchall()
            print_records = 'Book_Id|Branch_Id|Card_No|Date_Out|Due_Date|Returned_Date|Late?|Days_Late\n'
            for record in records:
                print_records+= str(str(record[0]) + "|" + str(record[1])+ "|" + str(record[2]) + "|" + record[3] + "|" + record[4] + "|" + record[5] +"|" + str(record[6]) + "|" + str(record[7]) + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=13,column=0,columnspan=2)
            iq.close()
        
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Book Table", font=controller.title_font)
        label.grid(row = 0, column = 0, pady = 10)
        
        Book_Id_Label = Label(self, text = 'Book ID')
        Book_Id_Label.grid(row = 1, column = 0)
        Book_Id = Entry(self, width = 30)
        Book_Id.grid(row = 1, column = 1, padx = 30)
        
        Branch_Id_Label = Label(self, text = 'Branch ID')
        Branch_Id_Label.grid(row = 2, column = 0)
        Branch_Id = Entry(self, width = 30)
        Branch_Id.grid(row = 2, column = 1, padx = 30)
        
        Card_No_label = Label(self, text = 'Card Number')
        Card_No_label.grid(row = 3, column = 0)
        Card_No = Entry(self, width = 30)
        Card_No.grid(row = 3, column = 1, padx = 30)
        
        Date_Out_label = Label(self, text = 'Date Out')
        Date_Out_label.grid(row = 4, column = 0)
        Date_Out = Entry(self, width = 30)
        Date_Out.grid(row = 4, column = 1, padx = 30)
        
        Due_Date_label = Label(self, text = 'Due Date')
        Due_Date_label.grid(row = 5, column = 0)
        Due_Date = Entry(self, width = 30)
        Due_Date.grid(row = 5, column = 1, padx = 30)
        
        Returned_date_label = Label(self, text = 'Returned Date')
        Returned_date_label.grid(row = 6, column = 0)
        Returned_date = Entry(self, width = 30)
        Returned_date.grid(row = 6, column = 1, padx = 30)
        
        Returned_date_label = Label(self, text = 'Late')
        Returned_date_label.grid(row = 6, column = 0)
        Returned_date = Entry(self, width = 30)
        Returned_date.grid(row = 7, column = 1, padx = 30)
        
        button = tk.Button(self, text="Insert Values", command=submit)
        button.grid(row = 8, column = 1, padx = 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 9, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Values", command=showValues)
        button.grid(row = 10, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Late Book Loan Data and days late", command=showLate)
        button.grid(row = 12, column = 1, padx = 30)
        
        
class BookCopies(tk.Frame):

    #Publisher_Name varchar(255) primary key,
    #Phone varchar(255),
    #Address varchar(255)

    def __init__(self, parent, controller):
        
        def submit():
            conn = sqlite3.connect('LMS.db')
            conn_cursor=conn.cursor()
            conn_cursor.execute("INSERT INTO BOOK_COPIES VALUES (:Book_Id, :Branch_Id, :No_Of_Copies)",
                            {
                                'Book_Id': Book_Id.get(),
                                'Branch_Id': Branch_Id.get(),
                                'No_Of_Copies': No_Of_Copies.get()
                            })
            conn.commit()
            conn.close()
            print(Branch_Id.get())
            
        def showValues():
            iq = sqlite3.connect('LMS.db')
            iq_cur = iq.cursor()
            iq_cur.execute("SELECT * FROM BOOK_COPIES")
            records = iq_cur.fetchall()
            print_records = 'Book ID|Branch ID|No of Copies\n'
            for record in records:
                print_records+= str(str(record[0]) + "|" + str(record[1])+ "|" + str(record[2]) + "\n")
                
            iq_label = Label(self,text=print_records)
            iq_label.grid(row=9,column=0,columnspan=2)
            iq.close()
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Book Table", font=controller.title_font)
        label.grid(row = 0, column = 0, pady = 10)
        
        Book_Id_Label = Label(self, text = 'Book ID')
        Book_Id_Label.grid(row = 1, column = 0)
        Book_Id = Entry(self, width = 30)
        Book_Id.grid(row = 1, column = 1, padx = 30)
        
        Branch_Id_Label = Label(self, text = 'Branch ID')
        Branch_Id_Label.grid(row = 2, column = 0)
        Branch_Id = Entry(self, width = 30)
        Branch_Id.grid(row = 2, column = 1, padx = 30)
        
        No_Of_Copies_label = Label(self, text = 'No of Copies')
        No_Of_Copies_label.grid(row = 3, column = 0)
        No_Of_Copies = Entry(self, width = 30)
        No_Of_Copies.grid(row = 3, column = 1, padx = 30)
        
        button = tk.Button(self, text="Insert Values", command=submit)
        button.grid(row = 4, column = 1, padx = 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 5, column = 1, padx = 30)
        
        button = tk.Button(self, text="Show Values", command=showValues)
        button.grid(row = 6, column = 1, padx = 30)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class TablePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pick your table", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        print(rows)



if __name__ == "__main__":
    con = sqlite3.connect('LMS.db')
    cursor = con.cursor()
    sql_query = """SELECT name FROM sqlite_master
    WHERE type='table';"""
    rows = cursor.execute(sql_query).fetchall()
    con.close()
        
    
    app = SampleApp()
    app.mainloop()