# pip install tk
# pip install googletrans
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
	text1=text
	src1=src
	dest1=dest
	trans=Translator()
	trans1=trans.translate(text,src=src1,dest=dest1)
	return trans1.text

def dataget():
	s=comb_sor.get()
	d=comb_dest.get()
	msg=sor_txt.get(1.0,END)
	textget=change(text=msg,src=s,dest=d)
	dest_txt.delete(1.0,END)
	dest_txt.insert(END,textget)
	
root = Tk()
root.title("G-Translater") 
root.geometry('500x800')
root.config(bg="Gray")

lab_txt = Label(root,text="G-Translator",font=("Time New Roman",30,'bold'))
lab_txt.place(x=125,y=40,height=50,width=250)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman",20,'bold'),bg="Gray")
lab_txt.place(x=125,y=110,height=20,width=250)
sor_txt = Text(frame,font=("Time New Roman",20,'bold'),wrap=WORD)
sor_txt.place(x=10,y=140,height=200,width=480)

list_txt=list(LANGUAGES.values())
comb_sor=ttk.Combobox(frame,value=list_txt)
comb_sor.place(x=10,y=350,height=40,width=155)
comb_sor.set("English")
button_change = Button(frame,text="Translate",relief=RAISED,command=dataget)
button_change.place(x=175,y=350,height=40,width=150)
comb_dest=ttk.Combobox(frame,value=list_txt)
comb_dest.place(x=335,y=350,height=40,width=150)
comb_dest.set("English")

lab_txt = Label(root,text="Destination Text",font=("Time New Roman",20,'bold'),bg="Gray")
lab_txt.place(x=125,y=410,height=20,width=250)
dest_txt = Text(frame,font=("Time New Roman",20,'bold'),wrap=WORD)
dest_txt.place(x=10,y=440,height=200,width=480)

root.mainloop()

