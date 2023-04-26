from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import Menu
from PIL import ImageTk, Image
from pathlib import Path
import sys, os

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from utils import *

class Window(Tk):

    WINDOWS = [
        "MAIN",
        "CONFIG",
        "ABOUT",
        "INIT",
        "ORDER",
        "CUSTOMER"
    ]

    # private root Tk
    # private canvas Canvas
    # private running Boolean
    def __init__(self, width: int, height: int, type:str, title:str, main:bool=True):
        super().__init__()

        self.geometry(str(width) + "x" + str(height) + "+50+50")
        self.title(title)
        self.type = type.upper()
        self.running = False
        self.resizable(False, False)
        # self.iconbitmap('icon.ico')
        if(main == True):
            self.config(background="grey")
            self.create_menu()
            self.add_welcome_text(width)
            self.add_image()
            self.create_button()
            self.protocol("WM_DELETE_WINDOW", self.close)
        else:
            # self.config(background="black")
            self.protocol("WM_DELETE_WINDOW", self.window_close)
    
    def redraw(self):
        self.update()
        self.update_idletasks()

    def window_close(self):
        if(self.type not in Window.WINDOWS):
            Window.WINDOWS.append(self.type)
            self.running = False
            self.destroy()

    def wait_for_close(self):
        self.running = True

        #continuously updates the windows
        while(self.running == True):
            self.redraw()
    
    def create_menu(self):
        #Optional menu
        menubar = Menu(self)
        self.config(menu=menubar)

        featured = Menu(menubar, tearoff=0)
        featured.add_command(label="Customer", command=self.set_customer_details)
        featured.add_command(label="Config", command=self.load_config)
        menubar.add_cascade(label="Featured", menu=featured)

        about = Menu(menubar)
        about.add_command(label="Github", command=self.load_about)
        menubar.add_cascade(label="About", menu=about, underline=0)

        menubar.add_separator()
        menubar.add_command(
            label='Exit',
            command=self.destroy
        )

    def create_button(self):
        button_start = Button(self, text='Start!', command=self.start_game, activebackground='black', activeforeground='grey', pady=10)
        button_reset = Button(self, text='Reset', command=self.reset_game, activebackground='black', activeforeground='grey', pady=10)
        button_close = Button(self, text='Close', command=self.close, activebackground='black', activeforeground='grey', pady=10)
        button_start.place(x=50, y=75)
        button_reset.place(x=200, y=75)
        button_close.place(x=350, y=75)

    def add_welcome_text(self, width):
        label = Label(self, text = "Welcome to Grocer Simulator :)", padx=10, pady=10, width=width)
        label.grid(column=0, row=0)
        label2 = Label(self, text = "Please visit the About", padx=10, pady=0, fg='red', bg='black', width=width)
        label.grid(column=1, row=1)
        label.config(font=("system-ui", 18))
        label.pack()
        label2.pack()
    
    def add_image(self):
        path = "shs.jpeg"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(master=self, image=img)
        panel.image = img
        panel.pack(side="bottom")

    def load_config(self):
        try:
            if("CONFIG" in Window.WINDOWS):
                Window.WINDOWS.remove("CONFIG")
                window = Window(300, 250, "config", "View Config Details", False)
                
                username = Label(window, text="Username:", padx=10, pady=10)
                Username = Label(window, text=Utils.readConfig("username"), padx=10, pady=10, fg="red")
                password = Label(window, text="Password:", padx=10, pady=10)
                Password = Label(window, text=Utils.readConfig("password"), padx=10, pady=10, fg="red")
                host = Label(window, text="Host:", padx=10, pady=10)
                Host = Label(window, text=Utils.readConfig("host"), padx=10, pady=10, fg="red")
                database = Label(window, text="Database:", padx=10, pady=10)
                Database = Label(window, text=Utils.readConfig("database"), padx=10, pady=10,fg="red")
                
                username.place(x=50, y=40)
                Username.place(x=150, y=40)
                password.place(x=50, y=80)
                Password.place(x=150, y=80)
                host.place(x=50, y=120)
                Host.place(x=150, y=120)
                database.place(x=50, y=160)
                Database.place(x=150, y=160)

                window.mainloop()
            else:
                raise Exception("Config window already exists, please close and try again")
        except Exception as error:
            #TODO use logger 'warn' as well
            print(error)
    
    def load_about(self):
        showinfo("Load About", "About will load shortly") 
    
    def start_game(self):
        showinfo("Init Game", "Game will load shortly") 

    def reset_game(self):
        showinfo("init Game", "Game will reset shortly")
    
    def set_customer_details(selt):
        try:
            if("CUSTOMER" in Window.WINDOWS):
                Window.WINDOWS.remove("CUSTOMER")
                window = Window(500, 500, "customer", "Register Customer", False)
                
                text = Label(window, text="Registration form", width=20, font=("bold", 20))
                text.place(x=120, y=10)

                first_name = Label(window, text="First Name", width=20, font=("bold", 10))
                first_name.place(x=70, y=80)

                first_name_field = Entry(window)
                first_name_field.place(x=240, y=80)

                last_name = Label(window, text="Last Name", width=20, font=("bold", 10))
                last_name.place(x=70, y=120)

                last_name_field = Entry(window)
                last_name_field.place(x=240, y=120)

                address1 = Label(window, text="Address 1", width=20, font=("bold", 10))
                address1.place(x=70, y=160)

                address1_field = Entry(window)
                address1_field.place(x=240, y=160)

                address2 = Label(window, text="Address 2", width=20, font=("bold", 10))
                address2.place(x=70, y=200)

                address2_field = Entry(window)
                address2_field.place(x=240, y=200)

                city = Label(window, text="City", width=20, font=("bold", 10))
                city.place(x=70, y=240)

                city_field = Entry(window)
                city_field.place(x=240, y=240)

                postal_code = Label(window, text="Postal Code", width=20, font=("bold", 10))
                postal_code.place(x=70, y=280)

                postal_code_field = Entry(window)
                postal_code_field.place(x=240, y=280)

                country = Label(window, text="Country", width=20, font=("bold", 10))
                country.place(x=70, y=320)

                country_field = Entry(window)
                country_field.place(x=240, y=320)

                #payment
                payment=Label(window, text="Payment", width=20,font=('bold',10))  
                payment.place(x=70,y=360)  
                vars1=IntVar()  
                Checkbutton(window,text="Cash Payment", variable = vars1).place(x=230,y=360)  
                
                vars2=IntVar()  
                Checkbutton(window,text="Bank Payment", variable=vars2).place(x=290, y=360)  

                btn = Button(window, text='Submit',width=20,bg='brown',fg='black')
                btn.place(x=140,y=400)

                window.wait_for_close()
            else:
                raise Exception("Customer window already exists, please close and try again")
        except Exception as error:
            #TODO use logger 'warn' as well
            print(error)

    def close(self):
        answer = askokcancel(
            title='Confirmation',
            message='Close Grocer Simulator?',
            icon=WARNING
        )

        #closes the application if 'Yes'
        if(answer):
            self.running = False

#Main function
def main():
    win = Window(460, 515, "main", "Grocer Simulator", True)
    win.wait_for_close()

main()