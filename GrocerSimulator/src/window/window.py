from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import Menu
from PIL import ImageTk, Image
from pathlib import Path
from toplevel import *
import sys, os
import webbrowser

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from utils import *
from database.dbUtils import *
from api.sageone import *
from api.wooCom import *
from groceryOrder import *
from customer import *
from address import *
from bankPayment import *
from cashPayment import *
from bank import *
from groceryList import *
from product import *

PROD_TITLE_X_POS = 0
PROD_CODE_X_POS = 165
PROD_PRICE_X_POS = 295
PROD_QTY_X_POS = 390
TOTAL_X_POS = 350
AMNT_PAID_X_POS = 350
INCREMENTOR = 40

CODE_X_POS = 20
TITLE_X_POS = 200
PRICE_X_POS = 580
QTY_X_POS = 710
VENDOR_X_POS = 790
AMOUNT_BUY_X_POS = 970

WEBPAGE = 'https://github.com/Keenan-Faure/Boot-Dev'

class Window(Tk):

    Customer = {
        "first_name": "",
        "last_name": "",
        "address1": "",
        "address2": "",
        "city": "",
        "postal_code": "",
        "country": "",
        "payment": {
            "payment_response": None
        }
    }
    
    Products = []

    def __init__(self, width: int, height: int, type:str, title:str):
        super().__init__()

        self.geometry(str(width) + "x" + str(height) + "+50+50")
        self.title(title)
        self.type = type.upper()
        self.running = False
        self.resizable(False, False)
        # self.iconbitmap('icon.ico')
        self.config(background="grey")
        self.create_menu()
        self.add_welcome_text(width)
        self.add_image()
        self.create_button()
        self.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.update()
        self.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while(self.running == True):
            self.redraw()
    
    def close_main(self):
        if(self.type not in TopLevel.WINDOWS):
            TopLevel.WINDOWS.append(self.type)
            self.running = False
            self.destroy()
    
    def create_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        featured = Menu(menubar, tearoff=0)
        featured.add_command(label="Customer", command=self.set_customer_details)
        featured.add_command(label="Config", command=self.load_config)
        menubar.add_cascade(label="Featured", menu=featured)

        about = Menu(menubar, tearoff=0)
        about.add_command(label="Prerequisite", command=self.open_setup)
        menubar.add_cascade(label="About", menu=about, underline=0)

        menubar.add_separator()
        menubar.add_command(
            label='Exit',
            command=self.destroy
        )

    def create_button(self):
        button_start = Button(self, text='Start!', command=self.start_game, activebackground='black', activeforeground='grey', pady=10)
        # button_reset = Button(self, text='Reset', command=self.reset_game, activebackground='black', activeforeground='grey', pady=10)
        button_close = Button(self, text='Close', command=self.close, activebackground='black', activeforeground='grey', pady=10)
        button_start.place(x=50, y=75)
        # button_reset.place(x=200, y=75)
        button_close.place(x=350, y=75)

    def add_welcome_text(self, width):
        label = Label(self, text = "Welcome to Grocer Simulator :)", padx=10, pady=10, width=width)
        label.grid(column=0, row=0)
        label2 = Label(self, text = "Please visit Featured", padx=10, pady=0, fg='red', bg='black', width=width)
        label.grid(column=1, row=1)
        label.config(font=("system-ui", 18))
        label.pack()
        label2.pack()
    
    def add_image(self):
        path = CUR_DIR / "window/shs.jpeg"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(master=self, image=img)
        panel.image = img
        panel.pack(side="bottom")

    def open_setup(self):
        try:
            if("ABOUT" in TopLevel.WINDOWS):
                TopLevel.WINDOWS.remove("ABOUT")
                window_setup = TopLevel("about")
                window_setup.geometry("600x250")
                window_setup.running = False
                window_setup.resizable = (False, False)
                window_setup.title("View prerequisites")
                
                text = Label(window_setup, text="Prerequisites", width=20, font=("bold", 20))
                text.place(x=160, y=0)

                setup_1 = Label(window_setup, text="Install Pip3 and Python", width=20, font=("bold", 10))
                setup_1.place(x=70, y=40)

                setup_15_entry = Entry(window_setup, width=25)
                setup_15_entry.insert(0, "sudo apt install python3")
                setup_15_entry.place(x=240, y=40)

                setup_1_entry = Entry(window_setup, width=25)
                setup_1_entry.insert(0, "sudo apt-get install python3-pip")
                setup_1_entry.place(x=240, y=80)

                setup_2 = Label(window_setup, text="Install Pillow", width=20, font=("bold", 10))
                setup_2.place(x=70, y=120)

                setup_2_entry = Entry(window_setup, width=25)
                setup_2_entry.insert(0, "sudo pip3 install Pillow")
                setup_2_entry.place(x=240, y=120)

                setup_3 = Label(window_setup, text="Install Requests", width=20, font=("bold", 10))
                setup_3.place(x=70, y=160)

                setup_3_entry = Entry(window_setup, width=25)
                setup_3_entry.insert(0, "sudo pip3 install requests")
                setup_3_entry.place(x=240, y=160)

                setup_4 = Label(window_setup, text="Instal MySQL Connector", width=20, font=("bold", 10))
                setup_4.place(x=70, y=160)

                setup_4_entry= Entry(window_setup, width=25)
                setup_4_entry.insert(0, "sudo pip3 install mysql-connector-python")
                setup_4_entry.place(x=240, y=160)

                window_setup.mainloop()
            else:
                raise Exception("About window already exists, please close and try again")
        except Exception as error:
            Utils.logger('warn', error)

    def load_config(self):
        try:
            if("CONFIG" in TopLevel.WINDOWS):
                TopLevel.WINDOWS.remove("CONFIG")
                window = TopLevel("config")
                window.geometry("300x250")
                window.running = False
                window.resizable = (False, False)
                window.title("View Config Details")
                
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
            Utils.logger('warn', error)
    """
    Starts the game
    """
    def start_game(self):
        try:
            if("MAIN" in TopLevel.WINDOWS):                    
                TopLevel.WINDOWS.remove("MAIN")
                window = TopLevel("main")
                window.geometry("1050x700")
                window.running = False
                window.resizable = (False, False)
                window.title("Grocer Simulator | Browse Products")

                OrderLineItems = []

                Window.Customer = Utils.import_data()

                def print_receipt(change: float, groceryList: list, totalCost: float):
                    try:
                        if("RECEIPT" in TopLevel.WINDOWS):
                            TopLevel.WINDOWS.remove("RECEIPT")
                            window = TopLevel("receipt")
                            window.geometry("486x500")
                            window.running = False
                            window.resizable = (False, False)
                            window.title("Order Receipt")
                            
                            Label(
                                window, 
                                text="Thank you for shopping with Universal Store ＼(٥⁀▽⁀ )／",
                                padx=20,
                                pady=20,
                                font=("bold", 15),
                                fg='red',
                                bg='black',
                                width=46
                            ).place(x=0, y=0)

                            Label(
                                window, 
                                text="Universal Store Tel no: 087 888 9878",
                                padx=15,
                                pady=10,
                                fg='grey',
                                width=23
                            ).place(x=0,y=65)

                            Label(
                                window, 
                                text="14 Montrose Plain Cape Town",
                                padx=0,
                                pady=10,
                                fg='grey',
                                width=23
                            ).place(x=0,y=105)

                            Label(
                                window, 
                                text="South Africa 7790",
                                padx=15,
                                pady=10,
                                fg='grey',
                                width=26
                            ).place(x=230,y=105)
                            
                            Label(
                                window,
                                text="Title",
                                padx=10,
                                pady=10,
                                width=20,
                                font=("bold", 10),
                                background="grey"
                            ).place(x=PROD_TITLE_X_POS, y=150)

                            Label(
                                window,
                                text="Code",
                                padx=10,
                                pady=10,
                                width=15,
                                font=("bold", 10),
                                background="grey"
                            ).place(x=PROD_CODE_X_POS, y=150)

                            Label(
                                window,
                                text="Price",
                                padx=10,
                                pady=10,
                                width=10,
                                font=("bold", 10),
                                background="grey"
                            ).place(x=PROD_PRICE_X_POS, y=150)

                            Label(
                                window,
                                text="Qty",
                                padx=10,
                                pady=10,
                                width=10,
                                font=("bold", 10),
                                background="grey"
                            ).place(x=PROD_QTY_X_POS, y=150)

                            for i in range(len(groceryList)):
                                Label(
                                    window,
                                    text=groceryList[i].get_title(),
                                    padx=10,
                                    pady=10,
                                    width=20,
                                    font=("bold", 10),
                                    background="grey"
                                ).place(x=PROD_TITLE_X_POS, y=(150+((i+1)*INCREMENTOR)))

                                Label(
                                    window,
                                    text=groceryList[i].get_code(),
                                    padx=10,
                                    pady=10,
                                    width=15,
                                    font=("bold", 10),
                                    background="grey"
                                ).place(x=PROD_CODE_X_POS, y=(150+((i+1)*INCREMENTOR)))

                                Label(
                                    window,
                                    text=groceryList[i].get_price(),
                                    padx=10,
                                    pady=10,
                                    width=10,
                                    font=("bold", 10),
                                    background="grey"
                                ).place(x=PROD_PRICE_X_POS, y=(150+((i+1)*INCREMENTOR)))

                                Label(
                                    window,
                                    text=groceryList[i].get_qty(),
                                    padx=10,
                                    pady=10,
                                    width=10,
                                    font=("bold", 10),
                                    background="grey"
                                ).place(x=PROD_QTY_X_POS, y=(150+((i+1)*INCREMENTOR)))

                            Label(
                                window,
                                text="Total: " + str(round(totalCost, 2)),
                                padx=10,
                                pady=10,
                                width=15,
                                font=("bold", 10)
                            ).place(x=TOTAL_X_POS, y=(200+((i+1)*INCREMENTOR)))

                            Label(
                                window,
                                text="Paid: " + str(round(totalCost, 2)),
                                padx=10,
                                pady=10,
                                width=15,
                                font=("bold", 10)
                            ).place(x=AMNT_PAID_X_POS, y=(250+((i+1)*INCREMENTOR)))

                            Label(
                                window,
                                text="Remaining: " + str(round(change, 2)),
                                padx=10,
                                pady=10,
                                width=20,
                                font=("bold", 10)
                            ).place(x=AMNT_PAID_X_POS, y=(300+((i+1)*INCREMENTOR)))

                            Label(
                                window,
                                text="Please Keep your Slip as Proof of Payment",
                                padx=10,
                                pady=10,
                                width=46,
                                font=("bold", 15)
                            ).place(x=0, y=(350+((i+1)*INCREMENTOR)))

                            Label(
                                window,
                                text="You were helped by AI-0209",
                                padx=10,
                                pady=10,
                                width=46,
                                font=("bold", 15)
                            ).place(x=0, y=(400+((i+1)*INCREMENTOR)))

                            window.mainloop()
                        else:
                            raise Exception("Config window already exists, please close and try again")
                    except Exception as error:
                        Utils.logger('warn', error)

                def create_order_view():
                    line_items = GroceryList([])
                    for line_item in OrderLineItems:
                        product = Product(
                            line_item[0].cget("text"),
                            line_item[1].cget("text"),
                            line_item[2].get(),
                            line_item[3].cget("text"),
                            line_item[4].cget("text")
                        )
                        line_items.add_product(product)
                    try:
                        PaymentMethod = None
                        address = Address(
                            Window.Customer["address1"],
                            Window.Customer["address2"],
                            Window.Customer["city"],
                            Window.Customer["postal_code"],
                            Window.Customer["country"]
                        )

                        if(Window.Customer["payment"]["payment_response"] == 1):
                            PaymentMethod = CashPayment(
                                Window.Customer["payment"]["amount"],
                                Window.Customer["payment"]["cash_owner"]
                            )
                        elif(Window.Customer["payment"]["payment_response"] == 2):
                            bank = Bank(
                                Window.Customer["payment"]["bank_name"],
                                Window.Customer["payment"]["branch_id"],
                                Window.Customer["payment"]["telephone_number"]
                            )
                            PaymentMethod = BankPayment(
                                Window.Customer["payment"]["amount"],
                                bank
                            )
                        else:
                            raise Exception("Customer details not setup")
                        customer = Customer(
                            Window.Customer["first_name"],
                            Window.Customer["last_name"],
                            address,
                            PaymentMethod
                        )
                        order = GroceryOrder(customer, line_items)
                        order_results = order.orderConfirm(Window.Products)
                        if(len(order_results[0]) > 0):
                            for j in range(len(order_results[0])):
                                for i in range(len(Window.Products)):
                                    if(order_results[0][j].get_code() == Window.Products[i].get_code()):
                                        deduct_qty = Window.Products[i].get_qty() - order_results[0][j].get_qty()
                                        Window.Products[i].set_qty(int(deduct_qty))

                        Window.Customer["payment"]["amount"] = float(
                            Window.Customer["payment"]["amount"]) - float(order_results[1])
                        
                        Utils.export_data(Window.Customer)
                        data = {}
                        data["grocer_products"] = []
                        for product in Window.Products:
                            data["grocer_products"].append(vars(product))
                        Utils.export_product_data(data)
                        window.window_close()

                        print_receipt(Window.Customer["payment"]["amount"], order_results[0], order_results[1])

                    except KeyError as error:
                        showinfo("Order Error", "Key '" + str(error) + "' not found. Please setup your customer")
                    except Exception as error:
                        showinfo("Order Error", str(error))
                landing_label = Label(
                    window,
                    text = "Available Products | " + str(round(Window.Customer["payment"]["amount"], 2)),
                    padx=10,
                    pady=10,
                    width=115,
                    background="green"
                )
                
                landing_label.place(x=10, y=10)

                code_header = Label(
                    window,
                    text="Code",
                    padx=10,
                    pady=10,
                    width=15,
                    font=("bold", 15),
                    background="grey"
                )
                code_header.place(x=CODE_X_POS, y=70)

                title_header = Label(
                    window,
                    text="Title",
                    padx=10,
                    pady=10,
                    width=35,
                    font=("bold", 15),
                    background="grey"
                )
                title_header.place(x=TITLE_X_POS, y=70)

                price_header = Label(
                    window,
                    text="Price",
                    padx=10,
                    pady=10,
                    width=10,
                    font=("bold", 15),
                    background="grey"
                )
                price_header.place(x=PRICE_X_POS, y=70)

                qty_header = Label(
                    window,
                    text="Quantity",
                    padx=10,
                    pady=10,
                    width=5,
                    font=("bold", 15),
                    background="grey"
                )
                qty_header.place(x=QTY_X_POS, y=70)

                vendor_header = Label(
                    window,
                    text="Brand",
                    padx=10,
                    pady=10,
                    width=15,
                    font=("bold", 15),
                    background="grey"
                )
                vendor_header.place(x=VENDOR_X_POS, y=70)

                buyable_header = Label(
                    window,
                    text="Amount",
                    padx=10,
                    pady=10,
                    width=5,
                    font=("bold", 14),
                    background="grey"
                )
                buyable_header.place(x=AMOUNT_BUY_X_POS, y=70)

                import_data = Utils.import_product_data()["grocer_products"]

                if(import_data == []):
                    wooProducts = WooCommerce.GET()
                    sageProducts = SageOne.GET()
                    internalProducts = DbUtils.GET()
                    Window.Products = wooProducts + sageProducts + internalProducts
                else:
                    Window.Products = []
                    for product_obj in import_data:
                        product = Product(
                            product_obj["code"],
                            product_obj["title"],
                            product_obj["qty"],
                            product_obj["price"],
                            product_obj["vendor"]
                        )
                        Window.Products.append(product)

                color = "grey"
                for i in range(len(Window.Products)):
                    if(Window.Products[i].get_vendor() == "MySQL Shoppers"):
                        color = "magenta"
                    elif(Window.Products[i].get_vendor() == "SageOne Market"):
                        color = "white"
                    else:
                        color = "grey"

                    code = Label(
                        window,
                        text=Window.Products[i].get_code(),
                        padx=10,
                        pady=2,
                        width=15,
                        font=("bold", 15),
                        background="grey"
                    )
                    code.place(x=CODE_X_POS, y=130 + (30 * i))

                    title = Label(
                        window,
                        text=Window.Products[i].get_title(),
                        padx=10, pady=2,
                        width=35,
                        font=("bold", 15),
                        background="grey"
                    )
                    title.place(x=TITLE_X_POS, y=130 + (30 * i))

                    price = Label(
                        window,
                        text=Window.Products[i].get_price(),
                        padx=10,
                        pady=2,
                        width=10,
                        font=("bold", 15),
                        background="grey"
                    )
                    price.place(x=PRICE_X_POS, y=130 + (30 * i))
                    if(Window.Products[i].get_qty() <= 0):
                        qty = Label(
                            window,
                            text=Window.Products[i].get_qty(),
                            padx=10,
                            pady=2,
                            width=5,
                            font=("bold", 15),
                            background="red"
                            )
                        qty.place(x=QTY_X_POS, y=130 + (30 * i))
                    else:
                        qty = Label(
                            window,
                            text=Window.Products[i].get_qty(),
                            padx=10,
                            pady=2,
                            width=5,
                            font=("bold", 15),
                            background="grey"
                            )
                        qty.place(x=QTY_X_POS, y=130 + (30 * i))

                    vendor = Label(
                        window,
                        text=Window.Products[i].get_vendor(),
                        padx=10,
                        pady=2,
                        width=15,
                        font=("bold", 15),
                        background=color,
                    )
                    vendor.place(x=VENDOR_X_POS, y=130 + (30 * i))

                    submit = Entry(
                        window,
                        width=7,
                    )

                    submit.place(x=AMOUNT_BUY_X_POS, y=130 + (30 * i))
                    line_item = [code, title, submit, price, vendor]
                    OrderLineItems.append(line_item)

                if(i == len(Window.Products)-1):
                    btn = Button(
                        window,
                        text='Place Order!',
                        width=25,
                        pady=5,
                        padx=5,
                        bg='brown',
                        fg='black',
                        command=create_order_view
                    )
                    btn.place(x=420,y=((i*30)+200))
                window.mainloop()
            else:
                showinfo("Error", "Main window already exists, please close and try again")
                raise Exception("Main window already exists, please close and try again")
        except Exception as error:
            Utils.logger('warn', error)
    
    def reset_game(self):
        showinfo("Grocer Simulator", "Game has successfully been reset")
    
    def set_customer_details(selt):
        try:
            if("CUSTOMER" in TopLevel.WINDOWS):
                TopLevel.WINDOWS.remove("CUSTOMER")
                window_main = TopLevel("customer")
                window_main.geometry("500x500")
                window_main.running = False
                window_main.resizable = (False, False)
                window_main.title("Grocer Simulator | Customer setup")
                
                text = Label(window_main, text="Registration form", width=20, font=("bold", 20))
                text.place(x=80, y=10)
   
                first_name = Label(window_main, text="First Name", width=20, font=("bold", 10))
                first_name.place(x=70, y=80)

                first_name_field = Entry(window_main)
                first_name_field.place(x=240, y=80)

                last_name = Label(window_main, text="Last Name", width=20, font=("bold", 10))
                last_name.place(x=70, y=120)

                last_name_field = Entry(window_main)
                last_name_field.place(x=240, y=120)

                address1 = Label(window_main, text="Address 1", width=20, font=("bold", 10))
                address1.place(x=70, y=160)

                address1_field = Entry(window_main)
                address1_field.place(x=240, y=160)

                address2 = Label(window_main, text="Address 2", width=20, font=("bold", 10))
                address2.place(x=70, y=200)

                address2_field = Entry(window_main)
                address2_field.place(x=240, y=200)

                city = Label(window_main, text="City", width=20, font=("bold", 10))
                city.place(x=70, y=240)

                city_field = Entry(window_main)
                city_field.place(x=240, y=240)

                postal_code = Label(window_main, text="Postal Code", width=20, font=("bold", 10))
                postal_code.place(x=70, y=280)

                postal_code_field = Entry(window_main)
                postal_code_field.place(x=240, y=280)

                country = Label(window_main, text="Country", width=20, font=("bold", 10))
                country.place(x=70, y=320)

                country_field = Entry(window_main)
                country_field.place(x=240, y=320)

                def get_payment():
                    Window.Customer["payment"]["payment_response"] = int(radio.get())

                payment=Label(window_main, text="Payment", width=20,font=('bold',10))
                payment.place(x=70,y=360)
                radio=IntVar()

                Radiobutton(
                    window_main,
                    text="Cash Payment",
                    variable=radio,
                    value=1,
                    command=get_payment
                ).place(x=230,y=360)  
                
                Radiobutton(
                    window_main,
                    text="Bank Payment",
                    variable=radio,
                    value=2,
                    command=get_payment
                ).place(x=290, y=360)

                def get_content():
                    Window.Customer["first_name"] = first_name_field.get()
                    Window.Customer["last_name"] = last_name_field.get()
                    Window.Customer["address1"] = address1_field.get()
                    Window.Customer["address2"] = address2_field.get()
                    Window.Customer["city"] = city_field.get()
                    Window.Customer["postal_code"] = postal_code_field.get()
                    Window.Customer["country"] = country_field.get()

                    try:
                        if(Window.Customer["payment"]["payment_response"] != None 
                        and Window.Customer["payment"]["payment_response"] in [1,2]):
                            if(Window.Customer["payment"]["payment_response"] == 1 and "PAYMENT" in TopLevel.WINDOWS):
                                TopLevel.WINDOWS.remove("PAYMENT")
                                window = TopLevel("payment")
                                window.geometry("500x250")
                                window.running = False
                                window.resizable = (False, False)
                                window.title("Grocer Simulator | Payment Details")

                                text = Label(window, text="Confirm Cash Payment Details", width=25, font=("bold", 15))
                                text.place(x=120, y=10)

                                cash_owner = Label(window, text="Cash Owner", width=20, font=("bold", 10))
                                cash_owner.place(x=70, y=80)

                                cash_owner_field = Entry(window)
                                cash_owner_field.place(x=240, y=80)

                                cash_amount = Label(window, text="Amount (R)", width=20, font=("bold", 10))
                                cash_amount.place(x=70, y=120)

                                cash_amount_field = Entry(window)
                                cash_amount_field.place(x=240, y=120)

                                def get_cash_payment():
                                    Window.Customer["payment"]["cash_owner"] = cash_owner_field.get()
                                    Window.Customer["payment"]["amount"] = float(cash_amount_field.get())
                                    Utils.export_data(Window.Customer)
                                    window_main.window_close()
                                    window.window_close()
                                    showinfo("Customer Registration Data", "Data has been recorded") 

                                btn = Button(
                                    window,
                                    text='Submit',
                                    width=20,
                                    bg='brown',
                                    fg='black',
                                    command=get_cash_payment
                                )
                                btn.place(x=140,y=160)
                                window.wait_for_close()

                            elif(Window.Customer["payment"]["payment_response"] == 2 and "PAYMENT" in TopLevel.WINDOWS):
                                TopLevel.WINDOWS.remove("PAYMENT")
                                window = TopLevel("payment")
                                window.geometry("500x350")
                                window.running = False
                                window.resizable = (False, False)
                                window.title("Grocer Simulator | Payment Details")

                                text = Label(window, text="Confirm Bank Payment Details", width=25, font=("bold", 15))
                                text.place(x=120, y=10)

                                bank_name = Label(window, text="Bank Name", width=20, font=("bold", 10))
                                bank_name.place(x=70, y=80)

                                bank_name_field = Entry(window)
                                bank_name_field.place(x=240, y=80)

                                branch_id = Label(window, text="Branch ID", width=20, font=("bold", 10))
                                branch_id.place(x=70, y=120)

                                branch_id_field = Entry(window)
                                branch_id_field.place(x=240, y=120)

                                telephone_number = Label(window, text="Telephone Number", width=20, font=("bold", 10))
                                telephone_number.place(x=70, y=160)

                                telephone_number_field = Entry(window)
                                telephone_number_field.place(x=240, y=160)

                                amount = Label(window, text="Amount (R)", width=20, font=("bold", 10))
                                amount.place(x=70, y=200)

                                amount_field = Entry(window)
                                amount_field.place(x=240, y=200)

                                def get_bank_payment():
                                    Window.Customer["payment"]["bank_name"] = bank_name_field.get()
                                    Window.Customer["payment"]["branch_id"] = branch_id_field.get()
                                    Window.Customer["payment"]["telephone_number"] = telephone_number_field.get()
                                    Window.Customer["payment"]["amount"] = amount_field.get()
                                    Utils.export_data(Window.Customer)
                                    window.window_close()
                                    window_main.window_close()
                                    showinfo("Customer Registration Data", "Data has been recorded")

                                btn = Button(
                                    window,
                                    text='Submit',
                                    width=20,
                                    bg='brown',
                                    fg='black',
                                    command=get_bank_payment
                                )
                                btn.place(x=140,y=240)
                                window.wait_for_close()

                    except Exception as error:
                        Utils.logger('warn', error)

                btn = Button(window_main, text='Submit',width=20,bg='brown',fg='black', command=get_content)
                btn.place(x=140,y=400)
                window_main.wait_for_close()

            else:
                raise Exception("Customer window already exists, please close and try again")
            
        except Exception as error:
            Utils.logger('warn', error)

    """
    Closes the application if 'Yes'
    """
    def close(self):
        answer = askokcancel(
            title='Confirmation',
            message='Close Grocer Simulator?',
            icon=WARNING
        )
        if(answer):
            self.running = False
    """
    Opens the Webpage defined
    in WEBBPAGE
    """
    def open_web(self):
        webbrowser.open(WEBPAGE, new=0)  