#AMT Machine whit Multiple window in python
import tkinter as tk                # ספרייה של חלומונות מרובים
import time


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
#הגדרת פונט לתוכנית
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}     
        for F in (StartPage, MenuPage, WithdrowPage,DepositPage,BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")     # מה יהיה הדף הראשון שלנו שיוצג בהרצת התוכנית

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#26004d')   #רקע של התפריט
        self.controller = controller
        self.controller.title("מערכת הפעלה של כספומט קוונטי")   #כותרת ראשית של התוכנה
        self.controller.state('zoomed')   #פונקציה שתגרום לחלון להיפתח במלואו
        self.controller.iconphoto(False,
        tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/quantum-computing.png'))    #שינוי אייקון בחלון של התוכנית
        #נשים לב ששינינו את את הקו הנטוי מ \ ל / כי פייתון לא מזהה קו נטוי סוגר רק פותח
        
        headin_label=tk.Label(self, text="Quantum ATM" , font=('orbitron',45,'bold'), 
                              foreground='white', background="#26004d")   #שער ראשי של התפריט + רקע+ בחירת פונט מיוחד + כותרת
        headin_label.pack(pady=25) #הפרדה של מרווח של הכותרת הראשית 

        #שכבת צבע נוספת סיסמא
        spce_label= tk.Label(self, height=4, bg='#26004d')
        spce_label.pack()

        password_label=tk.Label(self, text= 'Enter your password',
                                 font=('orbitron', 13) ,bg ='#26004d',
                                 fg='white')
        password_label.pack(pady=10)

        #קופסאת הכנסת קוד
        my_password=tk.StringVar()
        password_entry_box=tk.Entry(self,
                                    textvariable=my_password,
                                    font=('orbitron',12),
                                    width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)
        
        def handle_focs_in(_):
            password_entry_box.configure(fg='black',show='*')
            
        password_entry_box.bind('<FocusIn>', handle_focs_in)

        #כפתור כניסה
        def check_password():
            if my_password.get()== '123':     #הסיסמא עצמה
                my_password.set('')   #פונקציה שלא תשאיר לנו את הסיסמא על הדף- למען ביטחון מידע
                incorrect_password_label['text']=''
                controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text']='Incorrect Password'
        enter_button=tk.Button(self,
                               text='Enter',
                               command=check_password,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        enter_button.pack(pady=10)

        #סיסמא שגוייה
        incorrect_password_label=tk.Label(self,
                                          text='',
                                          font=('orbitron',13),
                                          fg='red',
                                          bg='#1a0033',
                                          anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)

        #אייקונים שנתמכים בתוכנה
        bottom_frame=tk.Frame(self, relief='raised',borderwidth=3,height=50)
        bottom_frame.pack(fill='x' , side='bottom')
        #visa icon
        visa_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/visa32.PNG')
        visa_lable=tk.Label(bottom_frame,image=visa_photo)
        visa_lable.pack(side='left')
        visa_lable.image= visa_photo
        #mastercard icon
        mastercard_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/mastercard.PNG')
        mastercard_lable=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_lable.pack(side='left')
        mastercard_lable.image= mastercard_photo
        # american-express icon
        americanexpress_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/americanexpress.PNG')
        americanexpress_lable=tk.Label(bottom_frame,image=americanexpress_photo)
        americanexpress_lable.pack(side='left')
        americanexpress_lable.image= americanexpress_photo
        #bitcoin icon
        bitcoin_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/bitcoin.PNG')
        bitcoin_lable=tk.Label(bottom_frame,image=bitcoin_photo)
        bitcoin_lable.pack(side='left')
        bitcoin_lable.image= bitcoin_photo
        #paypal icon
        paypal_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/paypal.PNG')
        paypal_lable=tk.Label(bottom_frame,image=paypal_photo)
        paypal_lable.pack(side='left')
        paypal_lable.image= paypal_photo

        #הצגת שעון
        def tick():
            current_time=time.strftime('%I:%M:%S %p'+'   '+'%A').lstrip('0').replace('0','')    #A שם מלא של יום /a שם קיצור של יום
            time_label.config(text=current_time)
            time_label.after(200,tick)    #עדכון שעות כל 2ms
            
        time_label=tk.Label(bottom_frame , font=('orbitron', 12))
        time_label.pack(side= 'right')
        tick()

#דף ראשי
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#26004d')
        self.controller = controller

        headin_label=tk.Label(self, text="Quantum ATM" , font=('orbitron',45,'bold'), 
                              foreground='white', background='#26004d')   #שער ראשי של התפריט + רקע+ בחירת פונט מיוחד + כותרת
        headin_label.pack(pady=25) #הפרדה של מרווח של הכותרת הראשית 

        #תת כותרת של התפריט הראשי
        main_menu_label=tk.Label(self,
                                 text='Main Menu',
                                 font=('orbitron', 13),
                                 fg='white',
                                 bg='#26004d')
        main_menu_label.pack()

        #כותרת - תווית בחירה
        selection_label=tk.Label(self,
                                 text='Please make a selection',
                                 font=('orbitron', 13),
                                 fg='white',
                                 bg='#26004d',
                                 anchor='w')
        selection_label.pack(fill='x')

        #שכבת צבע על הכפתורים בתוך התוכנית הראשית
        button_frame=tk.Frame(self, bg='#1a0033')
        button_frame.pack(fill='both' , expand=True)
        
        #כפתור Withdraw
        def withdraw():
            controller.show_frame('WithdrowPage')
        withdraw_button=tk.Button(button_frame,
                                text='Withdraw',
                                command=withdraw,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        #כפתור Deposit
        def Deposit():
            controller.show_frame('DepositPage')
        deposit_button=tk.Button(button_frame,
                                text='Deposit',
                                command=Deposit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        #כפתור Balance
        def Balance():
            controller.show_frame('BalancePage')
        balance_button=tk.Button(button_frame,
                                text='Balance',
                                command=Balance,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        balance_button.grid(row=2, column=0, pady=5)

        #כפתור EXIT
        def exit():
            controller.show_frame('StartPage')
        exit_button=tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=3, column=0, pady=5)

        #אייקונים שנתמכים בתוכנה
        bottom_frame=tk.Frame(self, relief='raised',borderwidth=3,height=50)
        bottom_frame.pack(fill='x' , side='bottom')
        #visa icon
        visa_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/visa32.PNG')
        visa_lable=tk.Label(bottom_frame,image=visa_photo)
        visa_lable.pack(side='left')
        visa_lable.image= visa_photo
        #mastercard icon
        mastercard_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/mastercard.PNG')
        mastercard_lable=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_lable.pack(side='left')
        mastercard_lable.image= mastercard_photo
        # american-express icon
        americanexpress_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/americanexpress.PNG')
        americanexpress_lable=tk.Label(bottom_frame,image=americanexpress_photo)
        americanexpress_lable.pack(side='left')
        americanexpress_lable.image= americanexpress_photo
        #bitcoin icon
        bitcoin_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/bitcoin.PNG')
        bitcoin_lable=tk.Label(bottom_frame,image=bitcoin_photo)
        bitcoin_lable.pack(side='left')
        bitcoin_lable.image= bitcoin_photo
        #paypal icon
        paypal_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/paypal.PNG')
        paypal_lable=tk.Label(bottom_frame,image=paypal_photo)
        paypal_lable.pack(side='left')
        paypal_lable.image= paypal_photo

        #הצגת שעון
        def tick():
            current_time=time.strftime('%I:%M:%S %p'+'   '+'%A').lstrip('0').replace('0','')    #A שם מלא של יום /a שם קיצור של יום
            time_label.config(text=current_time)
            time_label.after(200,tick)    #עדכון שעות כל 2ms
            
        time_label=tk.Label(bottom_frame , font=('orbitron', 12))
        time_label.pack(side= 'right')
        tick()


#עמוד משיכת מזומנים
class WithdrowPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#26004d')
        self.controller = controller

        headin_label=tk.Label(self,
                              text="Quantum ATM" ,
                              font=('orbitron',45,
                              'bold'), 
                              foreground='white', background='#26004d')   #שער ראשי של התפריט + רקע+ בחירת פונט מיוחד + כותרת
        headin_label.pack(pady=25) #הפרדה של מרווח של הכותרת הראשית 

        #תת כותרת של התפריט הראשי
        choose_amount_label=tk.Label(self,
                                 text='Choose the amount you want to withdrow',
                                 font=('orbitron', 13),
                                 fg='white',
                                 bg='#26004d')
        choose_amount_label.pack()

        #שכבת צבע על הכפתורים בתוך התוכנית משיכת מזומנים
        button_frame=tk.Frame(self, bg='#1a0033')
        button_frame.pack(fill='both' , expand=True)
        
        #אייקונים שנתמכים בתוכנה
        bottom_frame=tk.Frame(self, relief='raised',borderwidth=3,height=50)
        bottom_frame.pack(fill='x' , side='bottom')

        #visa icon
        visa_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/visa32.PNG')
        visa_lable=tk.Label(bottom_frame,image=visa_photo)
        visa_lable.pack(side='left')
        visa_lable.image= visa_photo
        #mastercard icon
        mastercard_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/mastercard.PNG')
        mastercard_lable=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_lable.pack(side='left')
        mastercard_lable.image= mastercard_photo
        # american-express icon
        americanexpress_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/americanexpress.PNG')
        americanexpress_lable=tk.Label(bottom_frame,image=americanexpress_photo)
        americanexpress_lable.pack(side='left')
        americanexpress_lable.image= americanexpress_photo
        #bitcoin icon
        bitcoin_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/bitcoin.PNG')
        bitcoin_lable=tk.Label(bottom_frame,image=bitcoin_photo)
        bitcoin_lable.pack(side='left')
        bitcoin_lable.image= bitcoin_photo
        #paypal icon
        paypal_photo=tk.PhotoImage(file='C:/Users/Gal Oz/Projects/ATM/paypal.PNG')
        paypal_lable=tk.Label(bottom_frame,image=paypal_photo)
        paypal_lable.pack(side='left')
        paypal_lable.image= paypal_photo

        #הצגת שעון
        def tick():
            current_time=time.strftime('%I:%M:%S %p'+'   '+'%A').lstrip('0').replace('0','')    #A שם מלא של יום /a שם קיצור של יום
            time_label.config(text=current_time)
            time_label.after(200,tick)    #עדכון שעות כל 2ms
            
        time_label=tk.Label(bottom_frame , font=('orbitron', 12))
        time_label.pack(side= 'right')
        tick()


#עמוד הפקדה
class DepositPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

#עמוד מאזן כספים
class BalancePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()