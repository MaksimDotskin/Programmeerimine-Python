from tkinter import Tk, Label, Entry, Button, Toplevel,ttk, END,font
from tkinter import PhotoImage
import random
import string

paroolid = []
nimed = []

sisse_log=False

def hide_menu_buttons():
        btn_reg.pack_forget()
        btn_aut.pack_forget()
        btn_mut.pack_forget()
        btn_un.pack_forget()
        
def show_menu_buttons():
    btn_reg.pack(pady=(10,10))
    btn_aut.pack(pady=(10,10))
    btn_mut.pack(pady=(10,10))
    btn_un.pack(pady=(10,10))

def Registreerimine_aken():

    def menu_tagasi():
        entry_nimi.destroy()
        entry_parool.destroy()
        label_nimi.destroy()
        label_parool.destroy()
        button_aut_parool.destroy()
        button_ok.destroy()
        button_tagasi.destroy()
        show_menu_buttons()

    def automaatne_parooli_genereerimine():
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls = list(str4)
        random.shuffle(ls)
        parool = ''.join([random.choice(ls) for x in range(12)])
        entry_parool.delete(0,END)
        entry_parool.insert(0,parool)

    def check_parool():
        parool=entry_parool.get()
        label1=Label(main_window,text='Parool peab sisaldama vähemalt ühte suurtähte, väiketähte, numbrit ja sümbolit',borderwidth=0)
        if not any(char.isupper() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        if not any(char.islower() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        if not any(char.isdigit() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        spec_simv = set(string.punctuation)
        if not any(char in spec_simv for char in parool): 
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        return True

    def check_nimi():
        nimi=entry_nimi.get()
        if not any(char.isupper() for char in nimi):
            label=Label(main_window,text=('Sisestage nimi suurtähtedega'),borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)
            return False
        
        elif not any(char.islower() for char in nimi):
            label2=Label(main_window,text=('Nimi ei tohi olla ainult suurtähtedega'),borderwidth=0)
            label2.pack(side='bottom', anchor='se')
            label2.after(2000,label2.destroy)
            return False
        elif nimi in nimed:
            label3=Label(main_window,text=('See nimi on hõivatud'),borderwidth=0)
            label3.pack(side='bottom', anchor='se')
            label3.after(2000,label3.destroy)
            return False
        return True

    def check_nimi_parool():
        if check_parool() and check_nimi():
            nimi=entry_nimi.get()
            parool=entry_parool.get()
            nimed.append(nimi)
            paroolid.append(parool)
            label=Label(main_window,text='Olete registreeritud',borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)
            entry_nimi.delete(0,END)
            entry_parool.delete(0,END)

        else:
            label=Label(main_window,text='Viga',borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)


    if sisse_log==True:
        label1=Label(main_window,text=('Te olete juba registreeritud ja autoriseeritud'),borderwidth=0)
        label1.pack(side='bottom', anchor='se')
        label1.after(2000,label1.destroy)
    else:

        hide_menu_buttons()
        label_nimi=Label(main_window,text='Nimi',borderwidth=0)
        label_nimi.pack(pady=(10,0))

        entry_nimi=Entry(main_window,borderwidth=0)
        entry_nimi.pack(pady=(0,10))

        label_parool=Label(main_window,text='Parool',borderwidth=0)
        label_parool.pack(pady=(0,0))
        
        entry_parool=Entry(main_window,borderwidth=0)
        entry_parool.pack(pady=(0,5))

        button_aut_parool=Button(main_window,text='Genereerida parool',borderwidth=0,command=automaatne_parooli_genereerimine)
        button_aut_parool.pack(pady=(0,0))

        button_ok=Button(main_window,text='Ok',command=check_nimi_parool,borderwidth=0)
        button_ok.pack(pady=(5,0))

        button_tagasi=Button(main_window,text='Tagasi',command=menu_tagasi,borderwidth=0)
        button_tagasi.pack(side='left', anchor='sw',pady=(10,10),padx=(10,10))
    
def Autoriseerimine_aken():

    def menu_tagasi():
        label_nimi.destroy()
        entry_nimi.destroy()
        label_parool.destroy()
        entry_parool.destroy()
        button_ok.destroy()
        button_tagasi.destroy()
        show_menu_buttons()

    def check_parool():
        parool=entry_parool.get()
    
        if parool not in paroolid:
            label1=Label(main_window,text='Vale nimi või parool',borderwidth=0)
            label1.pack(side='bottom', anchor='se')
            label1.after(2000,label1.destroy)
            return False
        return True

    def check_nimi():
        nimi=entry_nimi.get()
        if nimi not in nimed:
            label1=Label(main_window,text='Vale nimi või parool',borderwidth=0)
            label1.pack(side='bottom', anchor='se')
            label1.after(2000,label1.destroy)
            return False
        return True

    def check_nimi_parool():
        if check_parool() and check_nimi():
            label=Label(main_window,text='Olete autoriseeritud',borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)
            entry_nimi.delete(0,END)
            entry_parool.delete(0,END)
            global sisse_log
            sisse_log=True

        else:
            label=Label(main_window,text='Viga',borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)

    if sisse_log==True:
        label1=Label(main_window,text=('Te olete juba registreeritud ja autoriseeritud'),borderwidth=0)
        label1.pack(side='bottom', anchor='se')
        label1.after(2000,label1.destroy)
    else:
        hide_menu_buttons()

        label_nimi=Label(main_window,text='Nimi',borderwidth=0)
        label_nimi.pack(pady=(10,0))

        entry_nimi=Entry(main_window)
        entry_nimi.pack(pady=(0,10))

        label_parool=Label(main_window,text='Parool',borderwidth=0)
        label_parool.pack(pady=(0,0))
        
        entry_parool=Entry(main_window)
        entry_parool.pack(pady=(0,5))

        button_ok=Button(main_window,text='Ok',command=check_nimi_parool,borderwidth=0)
        button_ok.pack(pady=(5,0))

        button_tagasi=Button(main_window,text='Tagasi',command=menu_tagasi,borderwidth=0)
        button_tagasi.pack(side='left', anchor='sw',pady=(10,10),padx=(10,10))

def nimi_parroli_muutmine_aken():
    def menu_tagasi():
        label_nimi.destroy()
        entry_nimi.destroy()
        label_parool.destroy()
        entry_parool.destroy()
        button_ok.destroy()
        button_tagasi.destroy()
        label_1.destroy()
        label_2.destroy()
        show_menu_buttons()

    def check_parool():
        parool=entry_parool.get()
    
        if parool not in paroolid:
            label1=Label(main_window,text='Vale nimi või parool',borderwidth=0)
            label1.pack(side='bottom', anchor='se')
            label1.after(2000,label1.destroy)
            return False
        return True

    def check_nimi():
        nimi=entry_nimi.get()
        if nimi not in nimed:
            label1=Label(main_window,text='Vale nimi või parool',borderwidth=0)
            label1.pack(side='bottom', anchor='se')
            label1.after(2000,label1.destroy)
            return False
        return True

    def check_nimi_parool():
        if check_parool() and check_nimi():
            label_nimi.destroy()
            entry_nimi.destroy()
            label_parool.destroy()
            entry_parool.destroy()
            button_ok.destroy()
            button_tagasi.destroy()
            label_1.destroy()
            global sisse_log
            sisse_log=False
            Registreerimine_aken()

        else:
            label=Label(main_window,text='Viga',borderwidth=0)
            label.pack(side='bottom', anchor='se')
            label.after(2000,label.destroy)

    if sisse_log==True:
        hide_menu_buttons()

        label_1=Label(main_window,text='Sisestage vanad nimi ja parool',borderwidth=0)
        label_1.pack(pady=(10,0))

        label_2=Label(main_window,text='pärast muudatust peate uuesti sisse logima',borderwidth=0)
        label_2.pack(pady=(10,0))

        label_nimi=Label(main_window,text='Nimi',borderwidth=0)
        label_nimi.pack(pady=(10,0))

        entry_nimi=Entry(main_window)
        entry_nimi.pack(pady=(0,10))

        label_parool=Label(main_window,text='Parool',borderwidth=0)
        label_parool.pack(pady=(0,0))
        
        entry_parool=Entry(main_window)
        entry_parool.pack(pady=(0,5))

        button_ok=Button(main_window,text='Ok',command=check_nimi_parool,borderwidth=0)
        button_ok.pack(pady=(5,0))

        button_tagasi=Button(main_window,text='Tagasi',command=menu_tagasi,borderwidth=0)
        button_tagasi.pack(side='left', anchor='sw',pady=(10,10),padx=(10,10))
    else:
        label1=Label(main_window,text=('Te EI ole juba registreeritud ja autoriseeritud'),borderwidth=0)
        label1.pack(side='bottom', anchor='se')
        label1.after(2000,label1.destroy)

def unustanud_parooli_taastamine_aken():

    def menu_tagasi():
        label_1.destroy()
        label_parool.destroy()
        entry_parool.destroy()
        button_ok.destroy()
        button_tagasi.destroy()
        show_menu_buttons()

    def check_parool_sim():
        parool=entry_parool.get()
        label1=Label(main_window,text='Parool peab sisaldama vähemalt ühte suurtähte, väiketähte, numbrit ja sümbolit',borderwidth=0)
        if not any(char.isupper() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        if not any(char.islower() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        if not any(char.isdigit() for char in parool):
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        spec_simv = set(string.punctuation)
        if not any(char in spec_simv for char in parool): 
            label1.pack(side='bottom', anchor='se')
            label1.after(4000,label1.destroy)
            return False
        return True

    def check_parool():
        vana_parool=entry_parool.get()
        if vana_parool in paroolid:
            entry_parool.delete(0,END)
            label_1.destroy()
            label_parool.destroy()
            button_ok.destroy()
            label_1=Label(main_window,text=('Sisestage uus parool'),borderwidth=0)
            label_1.pack()
            uus_parool=entry_parool.get()

            def replace_parool():
                if check_parool_sim():
                    for i in range(len(paroolid)):
                        if paroolid[i] == vana_parool:
                            paroolid[i] = uus_parool
                    label_0=Label(main_window,text='Parool on muudatud',borderwidth=0)
                    label_0.pack(side='bottom', anchor='se')
                    label_0.after(2000,label_0.destroy)
                    entry_parool.delete(0,END)
                    return paroolid

            button_ok2=Button(main_window,text='Ok',command=replace_parool,borderwidth=0)
            button_ok2.pack(pady=(5,0))

        else:
            label1=Label(main_window,text='Vale parool',borderwidth=0)
            label1.pack(side='bottom', anchor='se')
            label1.after(2000,label1.destroy)

    if sisse_log==True:
        hide_menu_buttons()

        label_1=Label(main_window,text=('Parooli taastamiseks peate sisestama viimase meeldejääva parooli'),borderwidth=0)
        label_1.pack(pady=(10,0))

        label_parool=Label(main_window,text=('Parool'),borderwidth=0)
        label_parool.pack(pady=(10,0))

        entry_parool=Entry(main_window)
        entry_parool.pack(pady=(0,0))

        button_ok=Button(main_window,text='Ok',command=check_parool,borderwidth=0)
        button_ok.pack(pady=(5,0))

        button_tagasi=Button(main_window,text='Tagasi',command=menu_tagasi,borderwidth=0)
        button_tagasi.pack(side="bottom",pady=(10,10),padx=(10,10))

    else:
        label1=Label(main_window,text=('Te EI ole juba registreeritud ja autoriseeritud'),borderwidth=0)
        label1.pack(side='bottom', anchor='se')
        label1.after(2000,label1.destroy)

main_window = Tk()
main_window.title('Autoriseerimine/registreerimine')
main_window.geometry('600x250')
main_window.resizable(False, False)
gradient_image = PhotoImage(file="gradient.png")

label_bg = Label(main_window, image=gradient_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1) 

btn_reg = Button(main_window,text='Registreerimine',borderwidth=0,command=Registreerimine_aken)
btn_reg.pack(pady=(10,10))

btn_aut = Button(main_window, text='Autoriseerimine',borderwidth=0, command=Autoriseerimine_aken)
btn_aut.pack(pady=(10,10))

btn_mut = Button(main_window, text='Nime või parooli muutmine',borderwidth=0, command=nimi_parroli_muutmine_aken)
btn_mut.pack(pady=(10,10))

btn_un = Button(main_window, text='Unustanud parooli taastamine',borderwidth=0, command=unustanud_parooli_taastamine_aken)
btn_un.pack(pady=(10,10))

main_window.mainloop()




