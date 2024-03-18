from tkinter import *
from modul import *
import random
from tkinter import ttk

global stat
stat=False

def create_notif(Text,color):
    label=ttk.Label(main,text=Text,foreground=color)

    label.pack(pady="10")
    label.after(2000,label.destroy)

def delete_menu(*labels):
    for label in labels:
        label.pack_forget()
def return_menu(*labels):
    for label in labels:
        label.pack(pady="7")

def destroy_menu(*labels):
    for label in labels:
        label.destroy()

def delete_main_menu():
    delete_menu(label_menu,button_tolk,button_lisa_sõna,button_muuda,button_tead_kont,button_vaata,button_valja,button_settings)

def return_main_menu():
    return_menu(label_menu,button_tolk,button_lisa_sõna,button_muuda,button_tead_kont,button_vaata,button_valja,button_settings)
    main.title("Sõnastik")

def choise_keel(i):
    delete_main_menu()

    def ok():
        selected_keel1 = keel1.get()
        values1 = selected_keel1.split(",")

        f1 = values1[0]
        text1 = values1[1]

        selected_keel2 = keel2.get()
        values2 = selected_keel2.split(",")

        f2 = values2[0]
        text2 = values2[1]
        if selected_keel1!=selected_keel2:
            if i==1:
                tolge_window(f2,f1,text1,text2)
            elif i==2:
                kont_win(f2,f1,text1)
                
            delete_menu(option_est_1,option_est_2,option_ing_1,option_ing_2,option_rus_1,option_rus_2,ok_button,label_keel_1,label_keel_2)
        else:
            create_notif("Sisestage erinevad keeled","red")

    label_keel_1=ttk.Label(main,text="Keel, millest tõlkida")
    label_keel_1.pack(pady="10")
    keel1 = StringVar()
    keel1.set("rus.txt,vene")  # Установка значения по умолчанию
    option_rus_1 = Radiobutton(main, text="Vene", variable=keel1, value="rus.txt,vene")
    option_est_1 = Radiobutton(main, text="Eesti", variable=keel1, value="est.txt,eesti")
    option_ing_1 = Radiobutton(main, text="Inglise", variable=keel1, value="eng.txt,inglise")

    option_rus_1.pack()
    option_est_1.pack()
    option_ing_1.pack()

    label_keel_2=ttk.Label(main,text="Keel, millesse tõlkida")
    label_keel_2.pack(pady="10")

    keel2 = StringVar()
    keel2.set("est.txt,eesti")  # Установка значения по умолчанию
    option_rus_2 = Radiobutton(main, text="Vene", variable=keel2, value="rus.txt,vene")
    option_est_2 = Radiobutton(main, text="Eesti", variable=keel2, value="est.txt,eesti")
    option_ing_2 = Radiobutton(main, text="Inglise", variable=keel2, value="eng.txt,inglise")

    option_rus_2.pack()
    option_est_2.pack()
    option_ing_2.pack()

    ok_button = ttk.Button(main, text="Ok", command=ok,width=10)
    ok_button.pack(pady="20")

    
def tolge_window(fail1,fail2,keel1,keel2):

    main.title("Tõlgemine")

    label_sisestage=ttk.Label(main,text="Sõna "+keel1+ " keeles",width=20)
    label_sisestage.pack(pady="7")
    entry_est_sona=Entry(main)
    entry_est_sona.pack()
    label_sisestage2=ttk.Label(main,text="Tõlkinud sõna "+keel2+" keeles",width=20)
    label_sisestage2.pack(pady="7")
    tõlginud_sõna=Entry(main)
    tõlginud_sõna.pack()
    def ok():
        sõna=entry_est_sona.get()
        sõna=sõna.lower()

        if len(sõna)==0:
            create_notif("Sisestage sõna","red")
        else:
            resault_text,resault_status=tõlge(fail1,fail2,sõna)
            
            if resault_status==True:
                text_var=StringVar(value=resault_text)
                tõlginud_sõna.config(textvariable=text_var)
                
            elif resault_status==False:
                create_notif(resault_text,"yellow")
                tõlginud_sõna.delete(0,END)
    

    ok_button=ttk.Button(main,text="Ok",command=ok,width=10)
    ok_button.pack(pady="20")

    def tagasi():
        delete_menu(label_sisestage,entry_est_sona,label_sisestage2,tõlginud_sõna,ok_button,tagasi_button)
        return_main_menu()
    
    tagasi_button=ttk.Button(main,text="Tagasi",command=tagasi,width=15)
    tagasi_button.pack(side='bottom', anchor='se',padx="10",pady="10")

def lisa_sõna_window():
    delete_main_menu()
    main.title("Sõna lisamine")

    def ok():
        uus_eesti_sõna=entry_est_sõna.get()
        uus_vene_sõna=entry_vene_sõna.get()
        uus_ing_sõna=entry_ing_sõna.get()
        if len(uus_eesti_sõna)!=0 and len(uus_vene_sõna)!=0 and len(uus_ing_sõna)!=0:
            uus_eesti_sõna=uus_eesti_sõna.lower()

            uus_vene_sõna=uus_vene_sõna.lower()

            uus_ing_sõna=uus_ing_sõna.lower()

            lisa_sõna(uus_vene_sõna,uus_eesti_sõna,uus_ing_sõna)

            entry_est_sõna.delete(0,END)
            entry_vene_sõna.delete(0,END)
            entry_ing_sõna.delete(0,END)

            create_notif("Sõnad on lisanud","green")
        else:
            create_notif("Täitke mõlemad sisestusväljad","red")


    label_est_sõna=ttk.Label(main,text="Uus eesti sõna")
    label_est_sõna.pack(pady="7")

    entry_est_sõna=Entry(main)
    entry_est_sõna.pack()

    label_vene_sõna=ttk.Label(main,text="Uus vene sõna")
    label_vene_sõna.pack(pady="7")

    entry_vene_sõna=Entry(main)
    entry_vene_sõna.pack()

    label_ing_sõna=ttk.Label(main,text="Uus inglise sõna")
    label_ing_sõna.pack(pady="7")

    entry_ing_sõna=Entry(main)
    entry_ing_sõna.pack()

    button_ok=ttk.Button(main,text="Ok",command=ok,width="10")
    button_ok.pack(pady="20")

    def tagasi():
        delete_menu(label_est_sõna,label_vene_sõna,entry_est_sõna,entry_vene_sõna,button_ok,tagasi_button,label_ing_sõna,entry_ing_sõna)
        return_main_menu()
    tagasi_button=ttk.Button(main,text="Tagasi",command=tagasi,width="15")
    tagasi_button.pack(side='bottom', anchor='se',padx="10",pady="10")
    

def muuda_window():
    delete_main_menu()
    main.title("Sõna muutumine")

    def ok():

        old_sõna=entry_old_sõna.get()
        old_sõna=old_sõna.lower()
        new_sõna=entry_new_sõna.get()
        new_sõna=new_sõna.lower()
        if len(old_sõna)!=0 and len(new_sõna)!=0:


            answer=muuda_sõna(old_sõna,new_sõna)
            create_notif(answer,"yellow")
            entry_old_sõna.delete(0,END)
            entry_new_sõna.delete(0,END)
        else:
            create_notif("Täitke mõlemad sisestusväljad","red")

    label_old_sõna=ttk.Label(main,text="Vana sõna")
    label_old_sõna.pack(pady="7")

    entry_old_sõna=Entry(main)
    entry_old_sõna.pack()

    label_new_sõna=ttk.Label(main,text="Uus sõna")
    label_new_sõna.pack(pady="7")

    entry_new_sõna=Entry(main)
    entry_new_sõna.pack()

    button_ok=ttk.Button(main,text="Ok",command=ok,width="10")
    button_ok.pack(pady="20")

    def tagasi():
        delete_menu(label_old_sõna,entry_old_sõna,label_new_sõna,entry_new_sõna,button_ok,tagasi_button)
        return_main_menu()
    tagasi_button=ttk.Button(main,text="Tagasi",command=tagasi,width="15")
    tagasi_button.pack(side='bottom', anchor='se',padx="10",pady="10")



def kont_win(f1,f2,keel):
    main.title("Teadmise kontroll")
    
    def tagasi():
        delete_menu(label_resault,button_tagasi2)
        return_main_menu()

    list1=[]
    list2=[]

    with open(f1, 'r', encoding='utf-8') as file1, \
        open(f2, 'r', encoding='utf-8') as file2:
        
        for line in file1:
            word = line.strip()  
            list1.append(word)

        for line in file2:
            word = line.strip() 
            list2.append(word)

        global i,õiged,valled,lens,sõna
        i=0
        õiged=0
        valled=0
        lens=len(list1)
        sõna="start"

        label_index=ttk.Label(main,text="Küsimuste arv(mitte rohkem {})".format(lens))
        entry_index=Entry(main)
        label_index.pack(pady=(7,0))
        entry_index.pack(pady=7)


        list1r=[]
        list2r=[]

        def ok():
            global index
            index=int(entry_index.get())
            if isinstance(index,int):
                if index<=lens:
                    for g in range(0,index+1):
                        s=random.randint(0,index)
                        w1=list1[s]
                        w2=list2[s]
                        list1r.append(w1)
                        list2r.append(w2)
                        delete_menu(label_index,entry_index,button_ok)
                        button_edasi.pack(pady=10)
                        list1.remove(w1)
                        list2.remove(w2)
                else:
                    create_notif("Nii suur arv","red")
            else:
                create_notif("Sisestage arv","red")

        
    def edasi(i,õiged,valled):
   
        label.pack(pady=(7,0))
        entry.pack(pady=7)
        button_edasi.config(text="Edasi")
 
        sõna=list1r[i]
        tõlges=list2r[i-1]

        print(sõna,tõlges)
     
       
        i=i+1
        resault=entry.get()
        resault=resault.lower()
       
        if i>=2 :
            if resault==tõlges:
                create_notif("Õige","green")
                õiged=õiged+1

            elif resault!=tõlges:
                notif=("Vale, õige on: {} ".format(tõlges))
                valled=valled+1
                create_notif(notif,"red")

        if i==index+1:
            if resault==tõlges:
                create_notif("Õige","green")
                õiged=õiged+1

            elif resault!=tõlges:
                notif=("Vale, õige on: {} ".format(tõlges))
                valled=valled+1
                create_notif(notif,"red")
            delete_menu(label,entry,button_edasi)
            global label_resault
            label_resault=ttk.Label(main,text=("Tulemus:\n Õiged= {},Valled= {}".format(õiged,valled-1)))
            label_resault.pack(pady="7")
            button_tagasi2.pack(side='bottom', anchor='se',padx="10",pady="10")

        if index==i:
            button_edasi.config(text="Lõpeta")

        
        label.config(text="Tõlge {} {} keelse".format(sõna, keel))
        entry.delete(0,END)
        return i,õiged,valled

    def edasi_call():
        
        
        global i,õiged,valled
        i,õiged,valled=edasi(i,õiged,valled)
        

    label = ttk.Label()
    entry=Entry(main)
    button_edasi=ttk.Button(main,text="Start",command=edasi_call)
    button_ok=ttk.Button(main,text="OK",command=ok)
    button_ok.pack()
    
    
    button_tagasi2=ttk.Button(main,text="Tagasi",command=tagasi,width="15")

    
    
        

def vaata_win():
    main.title("Sõnastikuse vaatamine")
    def tagasi():
        delete_menu(label_rus,label_est,button_tagasi,label_ing,frame)
        return_main_menu()

    delete_main_menu()

    with open('rus.txt','r',encoding='utf-8') as rus_file:
        rus=rus_file.read()

    with open('est.txt','r',encoding='utf-8') as est_file:
        est=est_file.read()

    with open('eng.txt','r',encoding='utf-8') as ing_file:
        ing=ing_file.read()

    frame = ttk.Label(main)
    frame.pack()

    frame.pack(anchor="center")

    label_rus=ttk.Label(frame,text="Vene sõnad:\n{}".format(rus),width="15")
    label_rus.pack(side="left",padx=(10,10),pady=10)

    label_est=ttk.Label(frame,text="Eesti sõnad:\n{}".format(est),width="15")
    label_est.pack(side="left",padx=(10,10),pady=10)


    label_ing=ttk.Label(frame,text="Inglise sõnad:\n{}".format(ing),width="15")
    label_ing.pack(side="left",padx=(10,10),pady=10)
        
    button_tagasi=ttk.Button(main,text="Tagasi",command=tagasi)
    button_tagasi.pack(side='bottom', anchor='se',padx="10",pady="10")
    
def call_choise_keel_tolk():
    choise_keel(1)

def call_choise_keel_tead():
    choise_keel(2)


def toggle_theme():
    current_theme = style.theme_use()
    new_theme = "DarkTheme" if current_theme == "LightTheme" else "LightTheme"
    style.theme_use(new_theme)



main=Tk()
main.title("Sõnastik")
main.geometry("800x450")


style = ttk.Style()


style.theme_create("LightTheme", parent="default", settings={
   
    "TLabel": {"configure": {"foreground": "black", "background": "light gray", "borderwidth": 1, "relief": "solid", "padding": 5, "bordercolor": "black", "borderradius": 5}},
    "TButton": {"configure": {"foreground": "black", "background": "light gray", "borderwidth": 1, "relief": "solid", "padding": 5, "bordercolor": "black", "borderradius": 5},
                 "map": {"foreground": [("active", "blue")]}
                }
})


style.theme_create("DarkTheme", parent="default", settings={
  
    "TLabel": {"configure": {"foreground": "white", "background": "gray", "borderwidth": 1, "relief": "solid", "padding": 5, "bordercolor": "white", "borderradius": 5}},
    "TButton": {"configure": {"foreground": "white", "background": "gray", "borderwidth": 1, "relief": "solid", "padding": 5, "bordercolor": "white", "borderradius": 5},
                "map": {"foreground": [("active", "light gray")]}
               }
})


theme_list=["LightTheme","DarkTheme"]
random_theme=random.choice(theme_list)
style.theme_use(random_theme)

label_bg=ttk.Label()
label_bg.place(x=0, y=0, relwidth=1, relheight=1) 


label_menu=ttk.Label(main,text="Menu")
label_menu.pack(pady="7")

button_tolk=ttk.Button(main,text="Tõlkija",command=call_choise_keel_tolk,width=15)
button_tolk.pack(pady="7")

button_lisa_sõna=ttk.Button(main,text="Lisa uus sõna",command=lisa_sõna_window,width=15)
button_lisa_sõna.pack(pady="7")

button_muuda=ttk.Button(main,text="Muuda",command=muuda_window,width=15)
button_muuda.pack(pady="7")

button_tead_kont=ttk.Button(main,text="Teadmise kontroll",command=call_choise_keel_tead,width=15)
button_tead_kont.pack(pady="7")

button_vaata=ttk.Button(main,text="Vaata sõnastik",command=vaata_win,width=15)
button_vaata.pack(pady="7")

button_valja=ttk.Button(main,text="Välja",command=exit,width=15)
button_valja.pack(pady="7")

button_settings=ttk.Button(main,text="Muuta teem",command=toggle_theme,width=15)
button_settings.pack(pady="7")


main.mainloop()