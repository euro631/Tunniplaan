from tkinter import *
def uus_aken(ind:int):
    if askyesno("Küsimus","kas teen lahti?"):
        showinfo("vastus","Teen lahti aken")
    else:
        showinfo("Vastus","Panen kinnu aken")
        aken.destroy()
    uusaken=Toplevel() #tk()
    tabs=ttk.Notebook(uusaken)
    texts=[]
    textn=[]
    tab=[]
root=Tk()
Button(text="Расписание LogITpv21").grid(row=0,column=1)
Button(text="Понедельник:").grid(row=1,column=1)
Button(text="Вторник:").grid(row=2,column=1)
Button(text="Среда:").grid(row=3,column=1)
Button(text="Четверг:").grid(row=4,column=1)
Button(text="Пятница:").grid(row=5,column=1)
Button(text="1").grid(row=0,column=2)
Button(text="2").grid(row=0,column=3)
Button(text="3").grid(row=0,column=4)
Button(text="4").grid(row=0,column=5)
Button(text="5").grid(row=0,column=6)
Button(text="6").grid(row=0,column=7)
Button(text="7").grid(row=0,column=8)
Button(text="8").grid(row=0,column=9)
Button(text="9").grid(row=0,column=10)
Button(text="10").grid(row=0,column=11)
Button(text="Tugiõpe gr2").grid(row=1,column=2)
Button(text="logistika").grid(row=1,column=3,columnspan=2)
Button(text="matematika").grid(row=1,column=5,columnspan=2)
Button(text="Перерыв").grid(row=1,column=7)
Button(text="vene keel").grid(row=1,column=8,columnspan=2)
Button(text="Tugiõpe keemia").grid(row=2,column=2)
Button(text="Programeriumine").grid(row=2,column=3,columnspan=3)
Button(text="Перерыв").grid(row=2,column=6)
Button(text="Füüsika").grid(row=2,column=7,columnspan=2)
Button(text="Tugiõpe gr1").grid(row=3,column=2)
Button(text="Kunst:").grid(row=3,column=3,columnspan=2)
Button(text="Перерыв:").grid(row=3,column=5)
Button(text="Физра").grid(row=3,column=6,columnspan=2)
Button(text="logistika").grid(row=4,column=2,columnspan=2)
Button(text="Перерыв:").grid(row=4,column=4)
Button(text="Programeriumine").grid(row=4,column=5,columnspan=2)
Button(text="Inglih").grid(row=4,column=7,columnspan=2)
Button(text="Rakendus").grid(row=4,column=9,columnspan=2)
Button(text="ruhma tund").grid(row=4,column=11)
Button(text="Estikell").grid(row=5,column=2,columnspan=2)
Button(text="                 Programeriumine     alused                     ").grid(row=5,column=4,columnspan=5)
Button(text="Rakendus").grid(row=5,column=9,columnspan=2)


root.mainloop()