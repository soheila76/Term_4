from tkinter import *
import pymysql

def save():
    model=ent_model.get()
    company=ent_company.get()
    year=ent_year.get()
    fuel=ent_fuel.get()
    description=ent_description.get("1.0",END)
    if model != "" and company != "" and year != "" and fuel !="" and description != "":
        try:
            dbconnect=pymysql.connect(host="localhost",user="root",password="root",database="gallery")
            cursor=dbconnect.cursor()
            query=f"insert into car (model,company,year,fuel,description) values('{model}','{company}','{year}','{fuel}','{description}')"
            print("ok")
            cursor.execute(query)
            dbconnect.commit()
            lbl_ok.config(text="Saved",fg="green")
        except:
            print("errooooooor!!")

        
    else:
        lbl_ok.config(text="you can't leave the boxes empty!",fg="red")

root=Tk()
root.geometry("500x500")
root.config(bg="light blue")


lbl_model=Label(root,text="model",font=('',16),bg="light blue")
lbl_company=Label(root,text="company",font=('',16),bg="light blue")
lbl_year=Label(root,text="year",font=('',16),bg="light blue")
lbl_fuel=Label(root,text="fuel:",font=('',16),bg="light blue")
lbl_description=Label(root,text="description",font=('',16),bg="light blue")

ent_model=Entry(root,font=('',15))
ent_company=Entry(root,font=('',15))
ent_year=Entry(root,font=('',15))
ent_fuel=Entry(root,font=('',15))
ent_description=Text(root,font=('',15),width=20,height=3)

btn=Button(root,text="save",width=8,height=2,bg="chocolate2",command=save)
lbl_ok=Label(root,text="",bg="light blue")

#grid
lbl_model.grid(row=0,column=0,pady=10,padx=10)
lbl_company.grid(row=1,column=0,padx=10,pady=10)
lbl_year.grid(row=2,column=0,padx=10,pady=10)
lbl_fuel.grid(row=3,column=0,padx=10,pady=10)
lbl_description.grid(row=4,column=0,padx=10,pady=10)

ent_model.grid(row=0,column=1)
ent_company.grid(row=1,column=1)
ent_year.grid(row=2,column=1)
ent_fuel.grid(row=3,column=1)
ent_description.grid(row=4,column=1)

btn.grid(row=7,column=1)
lbl_ok.grid(row=8,column=1)


root.mainloop()