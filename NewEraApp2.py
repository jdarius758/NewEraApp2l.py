from tkinter import *
import tkinter.messagebox
import mysql.connector



def database():
    con = mysql.connector.connect(host='localhost', port='3306', username='root', password='1234', database='phone')
    m = con.cursor()
    m.execute('INSERT INTO phoneinfo (phone_name,phone_service,phone_price,phone_brand,phone_model) VALUES (%s,%s,%s,%s,%s)',(name.get(),service.get(),price.get(),brand.get(),model.get()))
    con.commit()
    con.close()




def save_info():
    name_ = name.get()
    service_ = service.get()
    price_ = price.get()
    brand_ = brand.get()
    model_ = model.get()

    file = open("info.txt", "w")
    file.write(name_)
    file.write(service_)
    file.write(price_)
    file.write(brand_)
    file.write(model_)
    file.close()

def click():
    tkinter.messagebox.showinfo('message'," Saved Info Into Text File")

def calculatepage():

    screen2 = Tk()
    screen2.geometry("500x500")
    screen2.title("Calculate Page")
    body2 = Label(screen2, bg="white", width="500", height="500")
    body2.pack()

    cstprice = StringVar()
    shipprice = StringVar()
    r = StringVar()

    heading3 = Label(screen2, text="New Era Calculate Cost ", font="52", fg="green", bg="white", )
    heading3.place(x=150, y=10)
    heading4 = Label(screen2, text="Enter Cost Details", font="30", fg="green", bg="white", )
    heading4.place(x=180, y=60)

    myLabel6 = Label(screen2, text="Enter Cost price :", fg="green", bg="white", )
    myLabel7 = Label(screen2, text="Enter Shipping price :", fg="green", bg="white", )
    myLabel6.place(x=150, y=170)
    myLabel7.place(x=150, y=230)
    entry6 = Entry(screen2, textvariable = cstprice)
    entry7 = Entry(screen2, textvariable = shipprice)
    entry6.place(x=300, y=170, width="180")
    entry7.place(x=300, y=230, width="180")

    entry8 = Entry(screen2, textvariable = r)
    entry8.place(x=300, y=330, width="180")

    def add():
        b = float(cstprice.get())
        i = float(shipprice.get())
        s = b + i
        r.set(s)


    calucost = Button(screen2, text="Calulate", command=add, width="20", height="2")
    calucost.place(x=300, y=440)
    screen2.mainloop()




screen = Tk()
screen.geometry("500x500")
screen.title("New Era App")









body = Label(bg="white", width = "500", height = "500")
body.pack()
menu = Menu(screen)
screen.config(menu=menu)

heading = Label(screen,text = "New Era Date Entry Application", font = "52", fg = "green", bg = "white", )
heading.place(x= 270, y = 10)
heading2 = Label(screen, text = "Enter Phone Details", font = "30", fg = "green", bg = "white",)
heading2.place(x = 300, y = 60)

photo = PhotoImage(file="newera.png", width = "180", height = "100")
label = Label(screen,image = photo)
label.place(x = 10, y = 10)

myLabel = Label(screen, text="Enter name of phone :", fg = "green", bg = "white",)
myLabel2 = Label(screen, text="Enter Service provider :", fg = "green", bg = "white",)
myLabel3 = Label(screen, text="Enter Price of Phone :", fg = "green", bg = "white",)
myLabel4 = Label(screen, text="Enter name of brand :", fg = "green", bg = "white",)
myLabel5 = Label(screen, text="Enter name of model :", fg = "green", bg = "white",)

myLabel.place(x = 150, y =170)
myLabel2.place(x = 150, y = 230)
myLabel3.place(x = 150, y = 290)
myLabel4.place(x = 150, y = 340)
myLabel5.place(x = 150, y = 400)



name = StringVar()
service = StringVar()
price = StringVar()
brand = StringVar()
model = StringVar()







entry1 = Entry(screen, textvariable = name)
entry2 = Entry(screen, textvariable = service)
entry3 = Entry(screen, textvariable = price)
entry4 = Entry(screen, textvariable = brand)
entry5 = Entry(screen, textvariable = model)


entry1.place(x = 300, y = 170, width = "180")
entry2.place(x = 300, y = 230, width = "180")
entry3.place(x = 300, y = 290, width = "180")
entry4.place(x = 300, y = 340, width = "180")
entry5.place(x = 300, y = 400, width = "180")


save = Button(text = "Save Info ", command=lambda:[save_info(),click(),database()], width = "20", height = "2")
save.place(x = 300, y = 440)

exit = Button(text = "Exit app ", command= screen.destroy, width = "20", height = "2")
exit.place(x = 150, y = 440)

calulate  = Button(text = "Calulate", command = calculatepage, width = "20", height = "2")
calulate.place(x = 10, y = 440)





screen.mainloop()
