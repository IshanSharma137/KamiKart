from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import math,random,os
import mysql.connector
import uuid
import smtplib
import datetime



mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
cursor=mydb.cursor()

cursor.execute("CREATE DATABASE if not exists customor")
        
cursor.execute("USE Customor")

cursor.execute("CREATE TABLE if not exists customer(customername VARCHAR(20),customernumber VARCHAR(25),password VARCHAR(20),email VARCHAR(25),cid VARCHAR(100),PRIMARY KEY(cid))")

cursor.execute("CREATE TABLE if not exists stockinfo(productname VARCHAR(20),stock int(20))")

now = datetime.datetime.now()
window=Tk()
window.geometry("1500x680")
window.title("WELCOME to KAMIKART")
window.configure(background="black")
global txtent1

def furnishing():
        global bed
        global sofa
        global chair
        global table
        global cupboard
        global showcase
        global bookshelf
        global dressing
        global lamp
        global shoerack
        global bedq,sofaq,chairq,bookq,dressq,tableq,cupq,showcaseq,lfq,sfq, flag,txtent1

        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
        cursor=mydb.cursor()

        cursor.execute("CREATE DATABASE if not exists customor")
                
        cursor.execute("USE Customor")

        cursor.execute("CREATE TABLE if not exists stockinfo(productname VARCHAR(20),stock int(20))")

        flag=10
        
        root=Toplevel()
        root.configure(background="#3AAFA9")
        

        f2=Frame(root,bg="#17252A",relief=SUNKEN,pady=330)
        f2.grid(rowspan=100,column=0)
        lbl0=Label(f2,text="LOGIN\n\n↓\n\nCHOOSE PRODUCT\n\n↓\n\nFURNISHING",bg="#17252A",fg="#FEFFFF", font=("comic sans ms",12))
        lbl0.grid(row=0,column=0)


        frame1=LabelFrame(root,bg="#17252A")
        frame1.grid(row=0,columnspan=500)
        header=Label(frame1,text="| KAMI KART |",font=("comic sans ms",50,"bold"),bg="#17252A",fg="#FEFFFF",width=30,justify=CENTER)
        header.grid(row=4,column=2)
            
        frame2=LabelFrame(root)
        frame2.grid(row=1,columnspan=100)
        subheader=Label(frame2,text="F U R N I T U R E",font=("Earwig Factory",25),bg="#2B7A78",fg="#DEF2F1",padx=450)
        subheader.grid(row=1,column=1)

#####################yaha se
        cursor.execute("select stock from stockinfo where productname='BED'")
        for a in cursor:
            print(a)
            
        bedq=IntVar()
        bed=ImageTk.PhotoImage(Image.open("bed.jpg"))
        bedlbl=Label(root,image=bed)
        bedlbl.grid(row=2,column=1)
        bedcaption=Label(root,text="BED\n(Rs.40000)\n Stock:{"+str(a[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        bedcaption.grid(row=3,column=1)
        if a[0]==0:
                bedentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                bedentryL.grid(row=4,column=1)
        else:
                bedentry=Entry(root,textvariable=bedq,font=("comicsansms"),justify=CENTER,width=10)
                bedentry.grid(row=4,column=1)
############################yaha tak
        cursor.execute("select stock from stockinfo where productname='SOFA'")
        for b in cursor:
            print(b)

        sofaq=IntVar()
        sofa=ImageTk.PhotoImage(Image.open("sofa.jpg"))
        sofalbl=Label(root,image=sofa)
        sofalbl.grid(row=2,column=2)
        sofacaption=Label(root,text="Sofa\n(Rs.32000)\n Stock:{"+str(b[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        sofacaption.grid(row=3,column=2)
        if b[0]==0:
                sofaentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                sofaentryL.grid(row=4,column=2)
        else:
                sofaentry=Entry(root,textvariable=sofaq,font=("comicsansms"),justify=CENTER,width=10)
                sofaentry.grid(row=4,column=2)
        
        cursor.execute("select stock from stockinfo where productname='CHAIR'")
        for ac in cursor:
            print(ac)
            
        chairq=IntVar()
        chair=ImageTk.PhotoImage(Image.open("chair.jpg"))
        chairlbl=Label(root,image=chair)
        chairlbl.grid(row=2,column=3)
        chaircaption=Label(root,text="Chair\n(Rs.200)\n Stock:{"+str(ac[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        chaircaption.grid(row=3,column=3)
        if ac[0]==0:
                chairentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                chairentryL.grid(row=4,column=3)
        else:
                chairentry=Entry(root,textvariable=chairq,font=("comicsansms"),justify=CENTER,width=10)
                chairentry.grid(row=4,column=3)

        cursor.execute("select stock from stockinfo where productname='BOOKSHELF'")
        for ad in cursor:
            print(ad)
        
        bookq=IntVar()
        bookshelf=ImageTk.PhotoImage(Image.open("bookshelf.jpg"))
        bookshelflbl=Label(root,image=bookshelf)
        bookshelflbl.grid(row=2,column=4)
        bookshelfcaption=Label(root,text="Bookshelf\n(Rs.12000)\n Stock:{"+str(ad[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        bookshelfcaption.grid(row=3,column=4)
        if ad[0]==0:
                bookshelfentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                bookshelfentryL.grid(row=4,column=4)
        else:
                bookshelfentry=Entry(root,textvariable=bookq,font=("comicsansms"),justify=CENTER,width=10)
                bookshelfentry.grid(row=4,column=4)

        cursor.execute("select stock from stockinfo where productname='DRESSING TABLE'")
        for ae in cursor:
            print(ae)

        dressq=IntVar()
        dressing=ImageTk.PhotoImage(Image.open("dressing.jpg"))
        dressinglbl=Label(root,image=dressing)
        dressinglbl.grid(row=2,column=5)
        dressingcaption=Label(root,text="Dressing Table\n(Rs.9000)\n Stock:{"+str(ae[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        dressingcaption.grid(row=3,column=5)
        if ae[0]==0:
                dressingL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                dressingentryL.grid(row=4,column=5)
        else:
                dressingentry=Entry(root,textvariable=dressq,font=("comicsansms"),justify=CENTER,width=10)
                dressingentry.grid(row=4,column=5)

        cursor.execute("select stock from stockinfo where productname='TABLE'")
        for af in cursor:
            print(af)
        
        tableq=IntVar()
        table=ImageTk.PhotoImage(Image.open("table.jpg"))
        tablelbl=Label(root,image=table)
        tablelbl.grid(row=6,column=1)
        tablecaption=Label(root,text="Table\n(Rs.3000)\n Stock:{"+str(af[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        tablecaption.grid(row=7,column=1)
        if af[0]==0:
                tableentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                tableentryL.grid(row=8,column=1)
        else:
                tableentry=Entry(root,textvariable=tableq,font=("comicsansms"),justify=CENTER,width=10)
                tableentry.grid(row=8,column=1)

        cursor.execute("select stock from stockinfo where productname='CUPBOARD'")
        for ag in cursor:
            print(ag)
        
        cupq=IntVar()
        cupboard=ImageTk.PhotoImage(Image.open("cupboard.jpg"))
        cupboardlbl=Label(root,image=cupboard)
        cupboardlbl.grid(row=6,column=2)
        cupboardcaption=Label(root,text="Cupboard\n(Rs.20000)\n Stock:{"+str(ag[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        cupboardcaption.grid(row=7,column=2)
        if ag[0]==0:
                cupboardentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                cupboardentryL.grid(row=8,column=2)
        else:
                cupboardentry=Entry(root,textvariable=cupq,font=("comicsansms"),justify=CENTER,width=10)
                cupboardentry.grid(row=8,column=2)

        cursor.execute("select stock from stockinfo where productname='SHOWCASE'")
        for ah in cursor:
            print(ah)
        
        showcaseq=IntVar()
        showcase=ImageTk.PhotoImage(Image.open("showcase.jpg"))
        showcaselbl=Label(root,image=showcase)
        showcaselbl.grid(row=6,column=3)
        showcasecaption=Label(root,text="Showcase\n(Rs.15000)\n Stock:{"+str(ah[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        showcasecaption.grid(row=7,column=3)
        if ah[0]==0:
                showcaseentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                showcaseentryL.grid(row=8,column=3)
        else:
                showcaseentry=Entry(root,textvariable=showcaseq,font=("comicsansms"),justify=CENTER,width=10)
                showcaseentry.grid(row=8,column=3)

        cursor.execute("select stock from stockinfo where productname='LAMP'")
        for ai in cursor:
            print(ai)

        lfq=IntVar()
        lamp=ImageTk.PhotoImage(Image.open("lamp.jpg"))
        lamplbl=Label(root,image=lamp)
        lamplbl.grid(row=6,column=4)
        lampcaption=Label(root,text="Lamp\n(Rs.350)\n Stock:{"+str(ai[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        lampcaption.grid(row=7,column=4)
        if ai[0]==0:
                lampentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                lampentryL.grid(row=8,column=4)
        else:
                lampentry=Entry(root,textvariable=lfq,font=("comicsansms"),justify=CENTER,width=10)
                lampentry.grid(row=8,column=4)

        cursor.execute("select stock from stockinfo where productname='SHOERACK'")
        for aj in cursor:
            print(aj)

        sfq=IntVar()
        shoerack=ImageTk.PhotoImage(Image.open("shoerack.jpg"))
        shoeracklbl=Label(root,image=shoerack)
        shoeracklbl.grid(row=6,column=5)
        shoerackcaption=Label(root,text="Shoerack\n(Rs.2000)\n Stock:{"+str(aj[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        shoerackcaption.grid(row=7,column=5)
        if aj[0]==0:
                shoerackentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                shoerackentryL.grid(row=8,column=5)
        else:
                shoeentry=Entry(root,textvariable=sfq,font=("comicsansms"),justify=CENTER,width=10)
                shoeentry.grid(row=8,column=5)





        b22=Button(root,text="ADD TO CART",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billdataf)
        b22.grid(row=4,column=6)

        b33=Button(root,text="VIEW BILL",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billprint)
        b33.grid(row=5,column=6)

        b11=Button(root,text="BACK",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=root.destroy)
        b11.grid(row=6,column=6)

def stockupdates():
        global bed0,sofa0,chair0,book0,bedq, xf
       
        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
        cursor=mydb.cursor()

        cursor.execute("CREATE DATABASE if not exists customor")
                
        cursor.execute("USE Customor")

        cursor.execute("CREATE TABLE if not exists stockinfo(productname VARCHAR(20),stock int(20))")
##############done
        try:
                        
                cursor.execute("select stock from stockinfo where productname='BED'")
                for a in cursor:
                    print(a)

                bed0=a[0]-bedq.get()
                if bed0<0:
                        
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='BED'".format(bed0))
                        xf=2
                               
                        mydb.commit()


                cursor.execute("select stock from stockinfo where productname='SOFA'")
                for b in cursor:
                    print(b)

                sofa0=b[0]-sofaq.get()
                if sofa0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SOFA'".format(sofa0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='CHAIR'")
                for ac in cursor:
                    print(ac)

                chair0=ac[0]-chairq.get()
                if chair0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='CHAIR'".format(chair0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='BOOKSHELF'")
                for ad in cursor:
                    print(ad)

                book0=ad[0]-bookq.get()
                if book0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='BOOKSHELF'".format(book0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='DRESSING TABLE'")
                for ae in cursor:
                    print(ae)

                dress0=ae[0]-dressq.get()
                if dress0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='DRESSING TABLE'".format(dress0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='TABLE'")
                for af in cursor:
                    print(af)

                table0=af[0]-tableq.get()
                if table0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='TABLE'".format(table0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='CUPBOARD'")
                for ag in cursor:
                    print(ag)

                cup0=ag[0]-cupq.get()
                if cup0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='CUPBOARD'".format(cup0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SHOWCASE'")
                for ah in cursor:
                    print(ah)

                showcase0=ah[0]-showcaseq.get()
                if showcase0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SHOWCASE'".format(showcase0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='LAMP'")
                for ai in cursor:
                    print(ai)

                lamp0=ai[0]-lfq.get()
                if lamp0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='LAMP'".format(lamp0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SHOERACK'")
                for aj in cursor:
                    print(aj)

                sr0=aj[0]-sfq.get()
                if sr0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SHOERACK'".format(sr0))
                        mydb.commit()
                        xf=2
        except Exception:
                print("")
        try:

                cursor.execute("select stock from stockinfo where productname='PHONE'")
                for ak in cursor:
                    print(ak)

                bph0=ak[0]-phonequant.get()
                if bph0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='PHONE'".format(bph0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='FRIDGE'")
                for al in cursor:
                    print(al)

                fridge0=al[0]-fridgeyquant.get()
                if fridge0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='FRIDGE'".format(fridge0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='LAPTOP'")
                for am in cursor:
                    print(am)

                lap0=am[0]-leq.get()
                if lap0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='LAPTOP'".format(lap0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='WASHING MACHINE'")
                for an in cursor:
                    print(an)

                wm0=an[0]-weq.get()
                if wm0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='WASHING MACHINE'".format(wm0))
                        mydb.commit()
                        xf=2
                        

                cursor.execute("select stock from stockinfo where productname='HEATER'")
                for ao in cursor:
                    print(ao)

                he0=ao[0]-heq.get()
                if he0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='HEATER'".format(he0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SPEAKER'")
                for ap in cursor:
                    print(ap)

                se0=ap[0]-speq.get()
                if se0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SPEAKER'".format(se0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='TV'")
                for aq in cursor:
                    print(aq)

                tv0=aq[0]-teq.get()
                if tv0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='TV'".format(tv0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='AC'")
                for ar in cursor:
                    print(ar)

                ac0=ar[0]-aeq.get()
                if ac0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='AC'".format(ac0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='GEYSER'")
                for ass in cursor:
                    print(ass)

                ge0=ass[0]-geyq.get()
                if ge0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='GEYSER'".format(ge0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='IRON'")
                for at in cursor:
                    print(at)

                iron0=at[0]-ieq.get()
                if iron0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='IRON'".format(iron0))
                        mydb.commit()
                        xf=2

        except Exception:
                print("")

        try:
        

                cursor.execute("select stock from stockinfo where productname='BELT'")
                for au in cursor:
                    print(au)

                belt0=au[0]-blq.get()
                if belt0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='BELT'".format(belt0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='CARPET'")
                for av in cursor:
                    print(av)

                cp0=av[0]-clq.get()
                if cp0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='CARPET'".format(cp0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='HAIRDRYER'")
                for aw in cursor:
                    print(aw)

                hd0=aw[0]-hlq.get()
                if hd0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='HAIRDRYER'".format(hd0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='JEANS'")
                for ax in cursor:
                    print(ax)

                jeans0=ax[0]-jlq.get()
                if jeans0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='JEANS'".format(jeans0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='KURTI'")
                for ay in cursor:
                    print(ay)

                kurti0=ay[0]-klq.get()
                if kurti0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='KURTI'".format(kurti0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='PERFUME'")
                for az in cursor:
                    print(az)

                per0=az[0]-plq.get()
                if per0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='PERFUME'".format(per0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SUNGLASSES'")
                for ba in cursor:
                    print(ba)

                sun0=ba[0]-slq.get()
                if sun0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SUNGLASSES'".format(sun0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SAREE'")
                for bb in cursor:
                    print(bb)

                sar0=bb[0]-sareelq.get()
                if sar0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SAREE'".format(sar0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='SHIRT'")
                for bc in cursor:
                    print(bc)

                shirt0=bc[0]-shirtlq.get()
                if shirt0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='SHIRT'".format(shirt0))
                        mydb.commit()
                        xf=2

                cursor.execute("select stock from stockinfo where productname='WATCH'")
                for bd in cursor:
                    print(bd)

                watch0=bd[0]-wlq.get()
                if watch0<0:
                        messagebox.showerror("Error", "Please enter item according to the AVAILABLE stock")
                        return False
                else:
                        cursor.execute("update stockinfo set stock={} where productname='BED'".format(watch0))
                        mydb.commit()
                        xf=2
        except Exception:
                print("")

       
######################done


def member():

        def signup():
                if textentry1.get()=="" or textentry2.get()=="" or textentry3.get()=="" or textentry4.get()=="":
                        messagebox.showerror("Error","All fields are Required")

                elif textentry3.get()!= textentry4.get():
                        messagebox.showerror("Error","Different Password Entered")
                else:
                        

    
                        cname=textentry1.get()
                        phone=textentry2.get()
                        passwd=textentry3.get()
                        em=textentry5.get()
                        ui=str(uuid.uuid4())
                
        
                        sql="INSERT INTO customer(customername ,customernumber, password, email,cid)  VALUES(%s, %s , %s, %s, %s)"
                        cursor.execute(sql,(cname, phone, passwd,em,ui))
                        mydb.commit()
                        print("Customer added")
                        

                        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        server.login("abraxaskami138@gmail.com","wateriscold12")
                        server.sendmail("abraxaskami138@gmail.com",em,ui)
                        server.quit()
                        

                        messagebox.showinfo("Unique ID","YOUR UNIQUE ID HAS BEEN SENT TO UR EMAIL \nYOU R NOW A MEMBER OF KAMIKART HOPE U HAVE A WONDERFUL EXPERIENCE ")
                        return True
                        
                        

        
        window = Tk()
        window.title("SignUp")
        window.configure(background="black")
        window.after(120000,lambda:window.destroy())

        cname=StringVar()
        phone=StringVar()
        passwd=StringVar()
        passwda=StringVar()
        em=StringVar()
        ui=StringVar()
        
        Label (window,text="NAME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

        textentry1= Entry(window,width=20,bg="#EC4D37",textvariable=cname)
        textentry1.grid(row=1,column=1)

        Label (window,text="PHONE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        textentry2= Entry(window,width=20,bg="#EC4D37",textvariable=phone)
        textentry2.grid(row=2,column=1)

        Label (window,text="PASSWORD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=3,column=0,sticky=W)

        textentry3= Entry(window,width=20,bg="#EC4D37",textvariable=passwd,show="*")
        textentry3.grid(row=3,column=1)

        Label (window,text="RE ENTER:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=4,column=0,sticky=W)

        textentry4= Entry(window,width=20,bg="#EC4D37",textvariable=passwda,show="*")
        textentry4.grid(row=4,column=1)


        Label (window,text="EMAIL:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=5,column=0,sticky=W)

        textentry5= Entry(window,width=20,bg="#EC4D37",textvariable=em)
        textentry5.grid(row=5,column=1)


        bt= Button(window,text="SUBMIT",bg="#EC4D37",fg="black",font="none 12 bold",width=30,command= signup )
        bt.grid(row=7,column=2,sticky=S)

        

        
def actd():
        def delete():
                while True:

                        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
                        cursor=mydb.cursor()
                        
                        cursor.execute("USE Customor")
                
                        cursor.execute("select * from customer where CID='"+txtentry2.get()+"'AND customername ='"+txtentry1.get()+"'")

                        finala=cursor.fetchall()

                        if finala:
                                for i in finala:
                                        print("true")

                                        cursor.execute("USE Customor")

                                        cursor.execute("delete from customer where cid='"+txtentry2.get()+"'AND customername='"+txtentry1.get()+"'")
                                
                
                                        mydb.commit()
                                        messagebox.showinfo("INFO","Account DELETED")
                                        return True

                        else:
                                messagebox.showerror("ERROR","WRONG OR NO PASS&ID ENTERED")
                                return("EXIT")
                

        


        window = Tk()
        window.title("DELETE")
        window.configure(background="black")
        window.after(60000,lambda:window.destroy())

        cnameeu=StringVar()
        passweu=StringVar()
      
        
        Label (window,text="NAME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

        txtentry1= Entry(window,width=20,bg="#EC4D37",textvariable=cnameeu)
        txtentry1.grid(row=1,column=1)

        Label (window,text="UNIQUE ID:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        txtentry2= Entry(window,width=20,bg="#EC4D37",textvariable=passweu)
        txtentry2.grid(row=2,column=1)

        bt= Button(window,text="DELETE ACCOUNT",bg="#EC4D37",fg="black",font="none 12 bold",width=30,command=delete )
        bt.grid(row=4,column=1,sticky=S)





def actu():
        global txtentry3
        
        
        def update():
                
                while True:

                        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
                        cursor=mydb.cursor()

                        cursor.execute("CREATE DATABASE if not exists customor")
                        
                        cursor.execute("USE Customor")
                
                        cursor.execute("select * from customer where CID='"+txtentry7.get()+"'")

                        finals=cursor.fetchall()

                        if finals:
                                for i in finals:
                                        print("true")

                                        cursor.execute("USE Customor")

                                        cursor.execute("update customer set customername='"+txtentry3.get()+"',customernumber='"+txtentry4.get()+"',email='"+txtentry5.get()+"',password='"+txtentry6.get()+"'where cid='"+txtentry7.get()+"'")
                                
                
                                        mydb.commit()
                                        messagebox.showinfo("INFO","Account UPDATED")
                                        return True 
                                

                        else:
                                messagebox.showerror("ERROR","ID REQUIRED")
                                return("EXIT")

                
                

        


        window = Tk()
        window.title("EDIT")
        window.configure(background="black")
        window.after(90000,lambda:window.destroy())

        cnameeue=StringVar()
        passweue=StringVar()
        emaileue=StringVar()
        phoneeue=StringVar()
        
        Label (window,text="NAME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

        txtentry3= Entry(window,width=20,bg="#EC4D37",textvariable=cnameeue)
        txtentry3.grid(row=1,column=1)

        Label (window,text="PHONE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        txtentry4= Entry(window,width=20,bg="#EC4D37",textvariable=phoneeue)
        txtentry4.grid(row=2,column=1)

        Label (window,text="EMAIL:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=3,column=0,sticky=W)

        txtentry5= Entry(window,width=20,bg="#EC4D37",textvariable=emaileue)
        txtentry5.grid(row=3,column=1)

        Label (window,text="PASSWORD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=4,column=0,sticky=W)

        txtentry6= Entry(window,width=20,bg="#EC4D37",textvariable=passweue,show="*")
        txtentry6.grid(row=4,column=1)

        Label (window,text="UNIQUE ID:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=5,column=0,sticky=W)

        txtentry7= Entry(window,width=20,bg="#EC4D37")
        txtentry7.grid(row=5,column=1)
 
 

         
        bt= Button(window,text="UPDATE",bg="#EC4D37",fg="black",font="none 12 bold",width=30,command=update )
        bt.grid(row=6,column=1,sticky=S)
        
        
        
def admin():
        global txtad1, txtad2
        
        def adminlog():
                global ftxt1, ftxt2, ftxt3, ftxt4, ftxt5, ftxt6, ftxt7, ftxt8, ftxt9, ftxt10, etxt1, etxt1, etxt2, etxt3, etxt4, etxt5, etxt6, etxt7, etxt8, etxt9, etxt10, ltxt1, ltxt2, ltxt3, ltxt4, ltxt5, ltxt6, ltxt7, ltxt8, ltxt9, ltxt10

                while True:


                        if txtad1.get()=="kamixzero" and txtad2.get()=="123@x":



                                windowa = Toplevel()
                                windowa.title("STOCK UPDATION")
                                windowa.configure(background="black")

                                
                                Label (windowa,text="BED:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

                                ftxt1= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt1.grid(row=1,column=1)
                                
                                Label (windowa,text="SOFA:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

                                ftxt2= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt2.grid(row=2,column=1)

                                Label (windowa,text="CHAIR:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=3,column=0,sticky=W)

                                ftxt3= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt3.grid(row=3,column=1)

                                Label (windowa,text="BOOKSHELF:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=4,column=0,sticky=W)

                                ftxt4= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt4.grid(row=4,column=1)

                                                                
                                Label (windowa,text="DRESSING TABLE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=5,column=0,sticky=W)

                                ftxt5= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt5.grid(row=5,column=1)

                                Label (windowa,text="TABLE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=6,column=0,sticky=W)

                                ftxt6= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt6.grid(row=6,column=1)

                                Label (windowa,text="SHOWCASE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=7,column=0,sticky=W)

                                ftxt7= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt7.grid(row=7,column=1)

                                Label (windowa,text="CUPBOARD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=8,column=0,sticky=W)

                                ftxt8= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt8.grid(row=8,column=1)

                                Label (windowa,text="LAMP:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=9,column=0,sticky=W)

                                ftxt9= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt9.grid(row=9,column=1)

                                Label (windowa,text="SHOERACK:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=10,column=0,sticky=W)

                                ftxt10= Entry(windowa,width=20,bg="#EC4D37")
                                ftxt10.grid(row=10,column=1)




                                ##electronic

                                Label (windowa,text="PHONE`:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=11,column=0,sticky=W)

                                etxt1= Entry(windowa,width=20,bg="#EC4D37")
                                etxt1.grid(row=11,column=1)
                                
                                Label (windowa,text="FRIDGE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=12,column=0,sticky=W)

                                etxt2= Entry(windowa,width=20,bg="#EC4D37")
                                etxt2.grid(row=12,column=1)

                                Label (windowa,text="LAPTOP:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=13,column=0,sticky=W)

                                etxt3= Entry(windowa,width=20,bg="#EC4D37")
                                etxt3.grid(row=13,column=1)

                                Label (windowa,text="WASHING MACHINE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=14,column=0,sticky=W)

                                etxt4= Entry(windowa,width=20,bg="#EC4D37")
                                etxt4.grid(row=14,column=1)

                                                                
                                Label (windowa,text="HEATER:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=15,column=0,sticky=W)

                                etxt5= Entry(windowa,width=20,bg="#EC4D37")
                                etxt5.grid(row=15,column=1)

                                Label (windowa,text="SPEAKER:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=16,column=0,sticky=W)

                                etxt6= Entry(windowa,width=20,bg="#EC4D37")
                                etxt6.grid(row=16,column=1)

                                Label (windowa,text="TV:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=17,column=0,sticky=W)

                                etxt7= Entry(windowa,width=20,bg="#EC4D37")
                                etxt7.grid(row=17,column=1)

                                Label (windowa,text="AC:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=18,column=0,sticky=W)

                                etxt8= Entry(windowa,width=20,bg="#EC4D37")
                                etxt8.grid(row=18,column=1)

                                Label (windowa,text="GEYSER:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=19,column=0,sticky=W)

                                etxt9= Entry(windowa,width=20,bg="#EC4D37")
                                etxt9.grid(row=19,column=1)

                                Label (windowa,text="IRON:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=20,column=0,sticky=W)

                                etxt10= Entry(windowa,width=20,bg="#EC4D37")
                                etxt10.grid(row=20,column=1)

                                ##lifestyle

                                                                
                                Label (windowa,text="BELT:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=21,column=0,sticky=W)

                                ltxt1= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt1.grid(row=21,column=1)
                                
                                Label (windowa,text="CARPET:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=22,column=0,sticky=W)

                                ltxt2= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt2.grid(row=22,column=1)

                                Label (windowa,text="HAIRDRYER:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=23,column=0,sticky=W)

                                ltxt3= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt3.grid(row=23,column=1)

                                Label (windowa,text="JEANS:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=24,column=0,sticky=W)

                                ltxt4= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt4.grid(row=24,column=1)

                                                                
                                Label (windowa,text="KURTI:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=25,column=0,sticky=W)

                                ltxt5= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt5.grid(row=25,column=1)

                                Label (windowa,text="PERFUME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=26,column=0,sticky=W)

                                ltxt6= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt6.grid(row=26,column=1)

                                Label (windowa,text="SUNGLASSES:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=27,column=0,sticky=W)

                                ltxt7= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt7.grid(row=27,column=1)

                                Label (windowa,text="SAREE:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=28,column=0,sticky=W)

                                ltxt8= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt8.grid(row=28,column=1)

                                Label (windowa,text="SHIRT:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=29,column=0,sticky=W)

                                ltxt9= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt9.grid(row=29,column=1)

                                Label (windowa,text="WATCH:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=30,column=0,sticky=W)

                                ltxt10= Entry(windowa,width=20,bg="#EC4D37")
                                ltxt10.grid(row=30,column=1)





                                bt= Button(windowa,text="SUBMIT",bg="#EC4D37",fg="black",font="none 12 bold",width=15,command=stockup)
                                bt.grid(row=32,column=5,sticky=E)
                                return("EXIT")
                        

                        else:
                                messagebox.showerror("ERROR","Wrong info entered")
                                return("EXIT")






        window = Tk()
        window.title("ADMIN LOGIN")
        window.configure(background="black")
        window.after(30000,lambda:window.destroy())

       
        
        Label (window,text="ADMIN NAME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

        txtad1= Entry(window,width=20,bg="#EC4D37")
        txtad1.grid(row=1,column=1)

        Label (window,text="PASSWORD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        txtad2= Entry(window,width=20,bg="#EC4D37",show="*")
        txtad2.grid(row=2,column=1)

        bt= Button(window,text="SUBMIT",bg="#EC4D37",fg="black",font="none 12 bold",width=30,command=adminlog )
        bt.grid(row=4,column=3,sticky=S)

        

def stockup():

        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
        cursor=mydb.cursor()

        cursor.execute("CREATE DATABASE if not exists customor")
                
        cursor.execute("USE Customor")

        cursor.execute("CREATE TABLE if not exists stockinfo(productname VARCHAR(20),stock int(20))")


        try:        
                int(ftxt1.get())
        except Exception:
                print("")
        try:
                int(ftxt2.get())
        except Exception:
                print("")
        try:
                
                int(ftxt3.get())
        except Exception:
                print("")
        try:
                int(ftxt4.get())
        except Exception:
                print("")
        try:
                int(ftxt5.get())
        except Exception:
                print("")
        try:
                int(ftxt6.get())
        except Exception:
                print("")
        try:
                int(ftxt7.get())
        except Exception:
                print("")
        try:
        
                int(ftxt9.get())
        except Exception:
                print("")
        try:
                int(ftxt10.get())
        except Exception:
                print("")
                ###################elec
        try:
                int(etxt1.get())
        except Exception:
                print("")
        try:
                int(etxt2.get())
        except Exception:
                print("")
        try:
                int(etxt3.get())
        except Exception:
                print("")
        try:
                int(etxt4.get())
        except Exception:
                print("")
        try:
                int(etxt5.get())
        except Exception:
                print("")
        try:
                int(etxt6.get())
        except Exception:
                print("")
        try:
                int(etxt7.get())
        except Exception:
                print("")
        try:
                int(etxt8.get())
        except Exception:
                print("")
        try:
                int(etxt9.get())
        except Exception:
                print("")
        try:
                int(etxt10.get())
        except Exception:
                print("")
        try:

                int(ltxt1.get())
        except Exception:
                print("")
        try:
                int(etxt2.get())
        except Exception:
                print("")
        try:
                int(ltxt3.get())
        except Exception:
                print("")
        try:
                int(ltxt4.get())
        except Exception:
                print("")
        try:
                int(ltxt5.get())
        except Exception:
                print("")
        try:
                int(ltxt6.get())
        except Exception:
                print("")
        try:
                int(ltxt7.get())
        except Exception:
                print("")
        try:
                int(ltxt8.get())
        except Exception:
                print("")
        try:
                int(ltxt9.get())
        except Exception:
                print("")
        try:
                int(ltxt10.get())
        except Exception:
                print("")
                
        
        
        
        try:
                cursor.execute("update stockinfo set stock="+ftxt1.get()+" where productname='BED'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt2.get()+" where productname='SOFA'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt3.get()+" where productname='CHAIR'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt4.get()+" where productname='BOOKSHELF'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt5.get()+" where productname='DRESSING TABLE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt6.get()+" where productname='TABLE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt7.get()+" where productname='CUPBOARD'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt8.get()+" where productname='SHOWCASE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt9.get()+" where productname='LAMP'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ftxt10.get()+" where productname='SHOERACK'")
        except Exception:
                print("")
        try:
                
                cursor.execute("update stockinfo set stock="+etxt1.get()+" where productname='PHONE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt2.get()+" where productname='FRIDGE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt3.get()+" where productname='LAPTOP'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt4.get()+" where productname='WASHING MACHINE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt5.get()+" where productname='HEATER'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt6.get()+" where productname='SPEAKER'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt7.get()+" where productname='TV'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt8.get()+" where productname='AC'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt9.get()+" where productname='GEYSER'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+etxt10.get()+" where productname='IRON'")
        except Exception:
                print("")
        try:

                cursor.execute("update stockinfo set stock="+ltxt1.get()+" where productname='BELT'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt2.get()+" where productname='CARPET'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt3.get()+" where productname='HAIRDRYER'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt4.get()+" where productname='JEANS'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt5.get()+" where productname='KURTI'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt6.get()+" where productname='PERFUME'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt7.get()+" where productname='SUNGLASSES'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt8.get()+" where productname='SAREE'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt9.get()+" where productname='SHIRT'")
        except Exception:
                print("")
        try:
                cursor.execute("update stockinfo set stock="+ltxt10.get()+" where productname='WATCH'")
        except Exception:
                print("")        
        
        mydb.commit()





                

def clicked():
        global txtent1,windowl

        def login():
               
                
                while True:
                   
                        mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
                        cursor=mydb.cursor()

                        cursor.execute("CREATE DATABASE if not exists customor")
                        
                        cursor.execute("USE Customor")

                        cursor.execute("select * from customer where customername='"+txtent1.get()+"' AND password='"+txtent2.get()+"'")

                        final=cursor.fetchall()

                        if final:
                                for i in final:
                                        print("true")
                        

        
                                global img
                                global img2
                                global img3
                                global img4
                                global img5
                                global img6
                                

                                
                            
                                top=Toplevel()
                                top.title("Hello Customer ")
                                top.configure(background="#2D3032")
                                top.geometry("1280x720")

                                      
                                
                                
                                f1=Frame(top,bg="#9615DB",borderwidth=8,relief=SUNKEN)
                                f1.pack(side=TOP, fill="x")

                                f2=Frame(top,bg="#9615DB",borderwidth=5,relief=SUNKEN)
                                f2.pack(side=LEFT, fill="y")

                                f3=Frame(top,bg="#9615DB",borderwidth=5,relief=SUNKEN)
                                f3.pack(side=RIGHT, fill="y")   

                                img6 = ImageTk.PhotoImage(Image.open("pane.jpg"))      
                                lblp=Label(f3,image=img6, bg="#9615DB").pack()

                                lblr=Label (f3,text=".....",bg="#9615DB",fg="#2D3032",font=("Bowlby One SC",20))
                                lblr.pack(side=LEFT)

                                lbl0=Label (f2,text="Welcome to KAMIKART,\n\n The home of your needs \n\n We here provide a \n\n wide range of products\n\n of Daily use to \n\n Rich expenses.",bg="#9615DB",fg="#2D3032", font=("comic sans ms",10))
                                lbl0.pack()
                                
                                img2 = ImageTk.PhotoImage(Image.open("shopp.jpg"))      
                                lblx=Label(f2,image=img2, bg="#9615DB").pack(side=BOTTOM)
                                
                                img = ImageTk.PhotoImage(Image.open("cool1.jpg"))      
                                lbl=Label(f1,image=img, bg="#9615DB").pack(side=LEFT, anchor="nw")

                                lbl1=Label (f1,text="           || KAMI KART ||",bg="#9615DB",fg="#2D3032",font=("Bowlby One SC",50,"bold"))
                                lbl1.pack(side=LEFT)
                                
                                lbl2=Label (top,text="► LIFESTYLE",bg="#2D3032",fg="white",font=("Earwig Factory",60))
                                lbl2.pack(side=TOP,anchor="w")

                                img3 = ImageTk.PhotoImage(Image.open("lifestylebutton.jpg"))      
                                
                                
                                bt1= Button(top,image=img3,bg="#2D3032",command=lifestyle )
                                bt1.pack(side=TOP)

                                
                                lbl3=Label (top,text="► ELECTRONICS",bg="#2D3032",fg="white",font=("Earwig Factory",60))
                                lbl3.pack(side=TOP,anchor="w")

                                img4 = ImageTk.PhotoImage(Image.open("electronicsbutton.jpg"))
                                
                                bt2= Button(top,image=img4,bg="#2D3032",command= electronics )
                                bt2.pack(side=TOP, padx=1, pady=1)
                                
                                lbl4=Label (top,text="► FURNISHING",bg="#2D3032",fg="white",font=("Earwig Factory",60))
                                lbl4.pack(side=TOP,anchor="w")

                                img5 = ImageTk.PhotoImage(Image.open("furniturebutton.jpg"))

                                bt3= Button(top,image=img5,bg="#2D3032",command= furnishing )
                                bt3.pack(side=TOP, padx=1, pady=1)

                                return("EXIT")

                        else:
                                messagebox.showerror("ERROR","Wrong info entered")
                                return("EXIT")

        global txtent1
        windowl = Tk()
        windowl.title("LOGIN")
        windowl.configure(background="black")
        windowl.after(30000,lambda:windowl.destroy())

       
        
        Label (windowl,text="NAME:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)

        txtent1= Entry(windowl,width=20,bg="#EC4D37")
        txtent1.grid(row=1,column=1)

        Label (windowl,text="PASSWORD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        txtent2= Entry(windowl,width=20,bg="#EC4D37",show="*")
        txtent2.grid(row=2,column=1)

        bt= Button(windowl,text="SUBMIT",bg="#EC4D37",fg="black",font="none 12 bold",width=30,command= login )
        bt.grid(row=4,column=2,sticky=S)

                                
        








bill_no=StringVar()
a=random.randint(10000,99999)
bill_no.set(str(a))




photo1= PhotoImage(file="masterg.gif")
Label (window ,image=photo1,width=1320,height=541,bg="black", bd=10).grid(row=0,column=0)

fprime=LabelFrame(window,bg="black",padx=420)
fprime.grid(row=1,columnspan=100)




bt= Button(fprime,text="SIGN UP",bg="#EC4D37",fg="black",font="none 12 bold",width=20,command= member )
bt.grid(row=5,column=2)

bt= Button(fprime,text="LOGIN",bg="#EC4D37",fg="black",font="none 12 bold",width=20,command= clicked )
bt.grid(row=5,column=0)

bt= Button(fprime,text="DELETE",bg="#EC4D37",fg="black",font="none 12 bold",width=20,command= actd)
bt.grid(row=6,column=2)

bt= Button(fprime,text="UPDATE",bg="#EC4D37",fg="black",font="none 12 bold",width=20,command= actu)
bt.grid(row=6,column=0)

bt= Button(fprime,text="ADMIN MODE",bg="#EC4D37",fg="black",font="none 12 bold",width=20,command= admin)
bt.grid(row=5,column=1)

try:
        prinname=(txtent1.get)
        print(prinname)
except Exception:
        print("")


def namex():
        nx=txtent1.get()

def electronics():
        global phone
        global fridge
        global laptop
        global speaker
        global tv
        global ac
        global washing
        global geyser
        global heater
        global iron
        global phonequant, fridgeyquant, leq,weq,heq,speq,teq,aeq,geyq,ieq, flag,bedq,sofaq,chairq,bookq,dressq,tableq,cupq,showcaseq,lfq,sfq, flag, txtent1
        

        flag=11
        
        root=Toplevel()
        root.configure(background="#FF6C5C")
        root.geometry("1111x780")

        f2=Frame(root,bg="#17252A",relief=SUNKEN,pady=330)
        f2.grid(rowspan=100,column=0)
        lbl0=Label(f2,text="LOGIN\n\n↓\n\nCHOOSE PRODUCT\n\n↓\n\nELECTRONICS",bg="#17252A",fg="#FEFFFF", font=("comic sans ms",12))
        lbl0.grid(row=0,column=0)


        frame1=LabelFrame(root,bg="#17252A")
        frame1.grid(row=0,columnspan=100)
        header=Label(frame1,text="| KAMI KART |",font=("comic sans ms",50,"bold"),bg="#17252A",fg="#FEFFFF",width=30,justify=CENTER)
        header.grid(row=4,column=2)
            
        frame2=LabelFrame(root)
        frame2.grid(row=1,columnspan=100)
        subheader=Label(frame2,text="E L E C T R O N I C S",font=("Earwig Factory",25),bg="#D83C2D",fg="#DEF2F1",padx=450)
        subheader.grid(row=1,column=1)

        cursor.execute("select stock from stockinfo where productname='PHONE'")
        for ak in cursor:
            print(ak)

        
        phonequant=IntVar()
        phone=ImageTk.PhotoImage(Image.open("phone.png"))
        phonelbl=Label(root,image=phone)
        phonelbl.grid(row=2,column=1)
        phonecaption=Label(root,text="Phone\n(Rs.65000)\n Stock:{"+str(ak[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        phonecaption.grid(row=3,column=1)
        if ak[0]==0:
                phoneentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                phoneentryL.grid(row=4,column=1)
        else:
                phoneentry=Entry(root,textvariable=phonequant,font=("comicsansms"),justify=CENTER,width=10)
                phoneentry.grid(row=4,column=1)

        cursor.execute("select stock from stockinfo where productname='FRIDGE'")
        for al in cursor:
            print(al)
                                
        fridgeyquant=IntVar()
        fridge=ImageTk.PhotoImage(Image.open("fridge.jpg"))
        fridgelbl=Label(root,image=fridge)
        fridgelbl.grid(row=2,column=2)
        fridgecaption=Label(root,text="Fridge\n(Rs.45000)\n Stock:{"+str(al[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        fridgecaption.grid(row=3,column=2)
        if al[0]==0:
                fridgeentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                fridgeentryL.grid(row=4,column=2)
        else:
                fridgeentry=Entry(root,textvariable=fridgeyquant,font=("comicsansms"),justify=CENTER,width=10)
                fridgeentry.grid(row=4,column=2)

        cursor.execute("select stock from stockinfo where productname='LAPTOP'")
        for am in cursor:
            print(am)
        
        leq=IntVar()
        laptop=ImageTk.PhotoImage(Image.open("laptop.jpg"))
        laptoplbl=Label(root,image=laptop)
        laptoplbl.grid(row=2,column=3)
        laptopcaption=Label(root,text="Laptop\n(Rs.85000)\n Stock:{"+str(am[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        laptopcaption.grid(row=3,column=3)
        if am[0]==0:
                laptopentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                laptopentryL.grid(row=4,column=3)
        else:
                laptopentry=Entry(root,textvariable=leq,font=("comicsansms"),justify=CENTER,width=10)
                laptopentry.grid(row=4,column=3)

        cursor.execute("select stock from stockinfo where productname='WASHING MACHINE'")
        for an in cursor:
            print(an)

        weq=IntVar()
        washing=ImageTk.PhotoImage(Image.open("washing.png"))
        washinglbl=Label(root,image=washing)
        washinglbl.grid(row=2,column=4)
        washingcaption=Label(root,text="Washing\n(Rs.23000)\n Stock:{"+str(an[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        washingcaption.grid(row=3,column=4)
        if an[0]==0:
                washingentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                washingentryL.grid(row=4,column=4)
        else:
                washingentry=Entry(root,textvariable=weq,font=("comicsansms"),justify=CENTER,width=10)
                washingentry.grid(row=4,column=4)

        cursor.execute("select stock from stockinfo where productname='HEATER'")
        for ao in cursor:
            print(ao)

        heq=IntVar()
        heater=ImageTk.PhotoImage(Image.open("heater.jpg"))
        heaterlbl=Label(root,image=heater)
        heaterlbl.grid(row=2,column=5)
        heatercaption=Label(root,text="Heater\n(Rs.1800)\n Stock:{"+str(ao[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        heatercaption.grid(row=3,column=5)
        if ao[0]==0:
                heaterentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                heaterentryL.grid(row=4,column=5)
        else:
                heaterentry=Entry(root,textvariable=heq,font=("comicsansms"),justify=CENTER,width=10)
                heaterentry.grid(row=4,column=5)

        cursor.execute("select stock from stockinfo where productname='SPEAKER'")
        for ap in cursor:
            print(ap)
        
        speq=IntVar()
        speaker=ImageTk.PhotoImage(Image.open("speaker.jpg"))
        speakerlbl=Label(root,image=speaker)
        speakerlbl.grid(row=6,column=1)
        speakercaption=Label(root,text="Speaker\n(Rs.12000)\n Stock:{"+str(ap[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        speakercaption.grid(row=7,column=1)
        if ap[0]==0:
                bedentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                bedentryL.grid(row=8,column=1)
        else:
                speakerentry=Entry(root,textvariable=speq,font=("comicsansms"),justify=CENTER,width=10)
                speakerentry.grid(row=8,column=1)

        cursor.execute("select stock from stockinfo where productname='TV'")
        for aq in cursor:
            print(aq)
        
        teq=IntVar()
        tv=ImageTk.PhotoImage(Image.open("tv.jpg"))
        tvlbl=Label(root,image=tv)
        tvlbl.grid(row=6,column=2)
        tvcaption=Label(root,text="TV\n(Rs.32000)\n Stock:{"+str(aq[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        tvcaption.grid(row=7,column=2)
        if aq[0]==0:
                tventryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                tventryL.grid(row=8,column=2)
        else:
                tventry=Entry(root,textvariable=teq,font=("comicsansms"),justify=CENTER,width=10)
                tventry.grid(row=8,column=2)

        cursor.execute("select stock from stockinfo where productname='AC'")
        for ar in cursor:
            print(ar)
        
        aeq=IntVar()
        ac=ImageTk.PhotoImage(Image.open("ac.jpg"))
        aclbl=Label(root,image=ac)
        aclbl.grid(row=6,column=3)
        accaption=Label(root,text="AC\n(Rs.45000)\n Stock:{"+str(ar[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        accaption.grid(row=7,column=3)
        if ar[0]==0:
                acentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                acentryL.grid(row=8,column=3)
        else:
                acentry=Entry(root,textvariable=aeq,font=("comicsansms"),justify=CENTER,width=10)
                acentry.grid(row=8,column=3)

        cursor.execute("select stock from stockinfo where productname='GEYSER'")
        for ass in cursor:
            print(ass)
                              
        geyq=IntVar()
        geyser=ImageTk.PhotoImage(Image.open("geyser.jpg"))
        geyserlbl=Label(root,image=geyser)
        geyserlbl.grid(row=6,column=4)
        geysercaption=Label(root,text="Geyser\n(Rs.19000)\n Stock:{"+str(ass[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        geysercaption.grid(row=7,column=4)
        if ass[0]==0:
                geyserentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                geyserentryL.grid(row=8,column=4)
        else:
                geyserentry=Entry(root,textvariable=geyq,font=("comicsansms"),justify=CENTER,width=10)
                geyserentry.grid(row=8,column=4)


        cursor.execute("select stock from stockinfo where productname='IRON'")
        for at in cursor:
            print(at)
            
        ieq=IntVar()
        iron=ImageTk.PhotoImage(Image.open("iron.jpg"))
        ironlbl=Label(root,image=iron)
        ironlbl.grid(row=6,column=5)
        ironcaption=Label(root,text="Iron\n(Rs.500)\n Stock:{"+str(at[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        ironcaption.grid(row=7,column=5)
        if at[0]==0:
                ironentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                ironentryL.grid(row=8,column=5)
        else:
                ironentry=Entry(root,textvariable=ieq,font=("comicsansms"),justify=CENTER,width=10)
                ironentry.grid(row=8,column=5)

        b2=Button(root,text="ADD TO CART",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billdatae)
        b2.grid(row=4,column=6)

        b3=Button(root,text="VIEW BILL",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billprint)
        b3.grid(row=5,column=6)

        b1=Button(root,text="BACK",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=root.destroy)
        b1.grid(row=6,column=6)



def lifestyle():
        global belt
        global carpet
        global hairdry
        global jeans
        global kurti
        global perfume
        global rayban
        global saree
        global shirt
        global watch
        global blq,clq,hlq,jlq,klq,plq,slq,sareelq,shirtlq,wlq, flag

        flag=12
        
        root=Toplevel()
        root.configure(background="#CCF381")
        root.geometry("1111x780")

        f2=Frame(root,bg="#17252A",relief=SUNKEN,pady=330)
        f2.grid(rowspan=100,column=0)
        lbl0=Label(f2,text="LOGIN\n\n↓\n\nCHOOSE PRODUCT\n\n↓\n\nLIFESTYLE",bg="#17252A",fg="#FEFFFF", font=("comic sans ms",12))
        lbl0.grid(row=0,column=0)


        frame1=LabelFrame(root,bg="#17252A")
        frame1.grid(row=0,columnspan=100)
        header=Label(frame1,text="| KAMI KART |",font=("comic sans ms",50,"bold"),bg="#17252A",fg="#FEFFFF",width=30,justify=CENTER)
        header.grid(row=4,column=2)
            
        frame2=LabelFrame(root)
        frame2.grid(row=1,columnspan=100)
        subheader=Label(frame2,text="   L I F E S T Y L E   ",font=("Earwig Factory",25),bg="#2C5F2D",fg="#DEF2F1",padx=450)
        subheader.grid(row=1,column=1)

        cursor.execute("select stock from stockinfo where productname='BELT'")
        for au in cursor:
            print(au)

        blq=IntVar()
        belt=ImageTk.PhotoImage(Image.open("belt.jpg"))
        beltlbl=Label(root,image=belt)
        beltlbl.grid(row=2,column=1)
        beltcaption=Label(root,text="Belt\n(Rs.150)\n Stock:{"+str(au[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        beltcaption.grid(row=3,column=1)
        if au[0]==0:
                beltentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                beltentryL.grid(row=4,column=1)
        else:
                beltentry=Entry(root,textvariable=blq,font=("comicsansms"),justify=CENTER,width=10)
                beltentry.grid(row=4,column=1)

        cursor.execute("select stock from stockinfo where productname='CARPET'")
        for av in cursor:
            print(av)
        
        clq=IntVar()
        carpet=ImageTk.PhotoImage(Image.open("carpet.jpg"))
        carpetlbl=Label(root,image=carpet)
        carpetlbl.grid(row=2,column=2)
        carpetcaption=Label(root,text="Carpet\n(Rs.400)\n Stock:{"+str(av[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        carpetcaption.grid(row=3,column=2)
        if av[0]==0:
                carpentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                carpentryL.grid(row=4,column=2)
        else:
                carpentry=Entry(root,textvariable=clq,font=("comicsansms"),justify=CENTER,width=10)
                carpentry.grid(row=4,column=2)

        cursor.execute("select stock from stockinfo where productname='HAIRDRYER'")
        for aw in cursor:
            print(aw)
        
        hlq=IntVar()
        hairdry=ImageTk.PhotoImage(Image.open("hairdry.jpg"))
        hairdrylbl=Label(root,image=hairdry)
        hairdrylbl.grid(row=2,column=3)
        hairdrycaption=Label(root,text="Hairdryer\n(Rs.1100)\n Stock:{"+str(aw[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        hairdrycaption.grid(row=3,column=3)
        if aw[0]==0:
                hairentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                hairentryL.grid(row=4,column=3)
        else:
                hairentry=Entry(root,textvariable=hlq,font=("comicsansms"),justify=CENTER,width=10)
                hairentry.grid(row=4,column=3)

        cursor.execute("select stock from stockinfo where productname='JEANS'")
        for ax in cursor:
            print(ax)
        
        jlq=IntVar()
        jeans=ImageTk.PhotoImage(Image.open("jeans.jpg"))
        jeanslbl=Label(root,image=jeans)
        jeanslbl.grid(row=2,column=4)
        jeanscaption=Label(root,text="Jeans\n(Rs.950)\n Stock:{"+str(ax[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        jeanscaption.grid(row=3,column=4)
        if ax[0]==0:
                jeanentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                jeanentryL.grid(row=4,column=4)
        else:
                jeanentry=Entry(root,textvariable=jlq,font=("comicsansms"),justify=CENTER,width=10)
                jeanentry.grid(row=4,column=4)

        cursor.execute("select stock from stockinfo where productname='KURTI'")
        for ay in cursor:
            print(ay)

        klq=IntVar()
        kurti=ImageTk.PhotoImage(Image.open("kurti.jpg"))
        kurtilbl=Label(root,image=kurti)
        kurtilbl.grid(row=2,column=5)
        kurticaption=Label(root,text="Kurti\n(Rs.350)\n Stock:{"+str(ay[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        kurticaption.grid(row=3,column=5)
        if ay[0]==0:
                kurtentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                kurtentryL.grid(row=4,column=5)
        else:
                kurtentry=Entry(root,textvariable=klq,font=("comicsansms"),justify=CENTER,width=10)
                kurtentry.grid(row=4,column=5)

        cursor.execute("select stock from stockinfo where productname='PERFUME'")
        for az in cursor:
            print(az)
        
        
        plq=IntVar()
        perfume=ImageTk.PhotoImage(Image.open("perfume.jpg"))
        perfumelbl=Label(root,image=perfume)
        perfumelbl.grid(row=6,column=1)
        perfumecaption=Label(root,text="Perfume\n(Rs.900)\n Stock:{"+str(az[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        perfumecaption.grid(row=7,column=1)
        if az[0]==0:
                perfentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                perfentryL.grid(row=8,column=1)
        else:
                perfentry=Entry(root,textvariable=plq,font=("comicsansms"),justify=CENTER,width=10)
                perfentry.grid(row=8,column=1)

        cursor.execute("select stock from stockinfo where productname='SUNGLASSES'")
        for ba in cursor:
            print(ba)

        
        slq=IntVar()
        rayban=ImageTk.PhotoImage(Image.open("rayban.jpg"))
        raybanlbl=Label(root,image=rayban)
        raybanlbl.grid(row=6,column=2)
        raybancaption=Label(root,text="Sunglasses\n(Rs.1500)\n Stock:{"+str(ba[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        raybancaption.grid(row=7,column=2)
        if ba[0]==0:
                raybentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                raybentryL.grid(row=8,column=2)
        else:
                raybentry=Entry(root,textvariable=slq,font=("comicsansms"),justify=CENTER,width=10)
                raybentry.grid(row=8,column=2)

        cursor.execute("select stock from stockinfo where productname='SAREE'")
        for bb in cursor:
            print(bb)
        
        sareelq=IntVar()
        saree=ImageTk.PhotoImage(Image.open("saree.jpg"))
        sareelbl=Label(root,image=saree)
        sareelbl.grid(row=6,column=3)
        sareecaption=Label(root,text="Saree\n(Rs.1200)\n Stock:{"+str(bb[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        sareecaption.grid(row=7,column=3)
        if bb[0]==0:
                sareeentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                sareeentryL.grid(row=8,column=3)
        else:
                sareeentry=Entry(root,textvariable=sareelq,font=("comicsansms"),justify=CENTER,width=10)
                sareeentry.grid(row=8,column=3)

        cursor.execute("select stock from stockinfo where productname='SHIRT'")
        for bc in cursor:
            print(bc)

        shirtlq=IntVar()
        shirt=ImageTk.PhotoImage(Image.open("shirt.jpg"))
        shirtlbl=Label(root,image=shirt)
        shirtlbl.grid(row=6,column=4)
        shirtcaption=Label(root,text="Shirt\n(Rs.800)\n Stock:{"+str(bc[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        shirtcaption.grid(row=7,column=4)
        if bc[0]==0:
                shirtentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                shirtentryL.grid(row=8,column=4)
        else:
                shirtentry=Entry(root,textvariable=shirtlq,font=("comicsansms"),justify=CENTER,width=10)
                shirtentry.grid(row=8,column=4)

        cursor.execute("select stock from stockinfo where productname='WATCH'")
        for bd in cursor:
            print(bd)

        wlq=IntVar()
        watch=ImageTk.PhotoImage(Image.open("watch.jpg"))
        watchlbl=Label(root,image=watch)
        watchlbl.grid(row=6,column=5)
        watchcaption=Label(root,text="Watch\n(Rs.1900)\n Stock:{"+str(bd[0])+"}",font=("comicsansms"),bg="#17252A",fg="#FEFFFF")
        watchcaption.grid(row=7,column=5)
        if bd[0]==0:
                watcentryL=Label(root,text="UNAVAILABLE",font=("comicsansms",15,"bold"),bg="#17252A",fg="red")
                watcentryL.grid(row=8,column=5)
        else:
                watcentry=Entry(root,textvariable=wlq,font=("comicsansms"),justify=CENTER,width=10)
                watcentry.grid(row=8,column=5)

        b22=Button(root,text="ADD to CART",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billdatal)
        b22.grid(row=4,column=6)

        b33=Button(root,text="VIEW BILL",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=billprint)
        b33.grid(row=5,column=6)


        b11=Button(root,text="BACK",font=("comicsansms"),bg="#17252A",fg="#FEFFFF",command=root.destroy)
        b11.grid(row=6,column=6)


def total():
        
                blt=blq.get()*150
                clt=clq.get()*400
                hlt=hlq.get()*1100
                jlt=jlq.get()*950
                klt=klq.get()*350
                plt=plq.get()*900
                slt=slq.get()*1500
                sareelt=sareelq.get()*1200
                shirtlt=shirtlq.get()*800
                wlt=wlq.get()*1900

                totall=blt+clt+hlt+jlt+klt+plt+slt+sareelt+shirtlt+wlt
                
def billprint():
        global textarea, final_total, txtent1
        root=Toplevel()
        root.configure(background="black")
        root.geometry("460x410")
        
        F5=Frame(root,bd=10,relief=GROOVE)
        F5.place(x=0,y=0,width=460,height=350)
        bill_title=Label(F5,text="BILL",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=textarea.yview)
        textarea.pack(fill=BOTH,expand=1)
        gbill_btn=Button(root,command=payment,text="CHECKOUT",bg="#123D5F",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").place(x=0,y=350,width=230,height=60)
        exit_btn=Button(root,text="EXIT APP",command=exitBill,bg="#123D5F",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").place(x=230,y=350,width=230,height=60)
        try:
                billdataf()
        except Exception:
                print("")
        try:
                billdatae()
        except Exception:
                print("")
        try:
                billdatal()
        except Exception:
                print("")
        textarea.delete('1.0',END)
        x=0
        y=0
        z=0
        try:
                x=totalf
        except Exception:
                print("")
        try:
                y=totale
        except Exception:
                print("")
        try:
                z=totall
        except Exception:
                print("")
        final_total=x+y+z
        
        
        
        textarea.insert(END,"\t Welcome to KAMIKART")
        textarea.insert(END,f"\n Bill Number :{bill_no.get()}")
        try:
                textarea.insert(END,f"\n Customer Name :{txtent1.get()}")
        except Exception:
                print("")
        datetime=now.strftime("%Y-%m-%d %H:%M:%S")
        textarea.insert(END,f"\n Date/Time: :{datetime}")
        




        
        textarea.insert(END,f"\n====================================================")
        textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        textarea.insert(END,f"\n====================================================")
        try:
                textarea.insert(END,f"{fadd}")
        except Exception:
                print("")

        try:
                textarea.insert(END,f"{eadd}")
        except Exception:
                print("")
        try:
                textarea.insert(END,f"{ladd}")
        except Exception:
                print("")
        textarea.insert(END,f"\n----------------------------------------------------")
        textarea.insert(END,f"\n Total Bill  \t\t\t\tRs. {final_total}")
        textarea.insert(END,f"\n----------------------------------------------------")

        
        
def billdataf():
        global fadd,totalf
        
        if flag==10:
                
                bedt=bedq.get()*40000
                bedt=bedq.get()*40000
                sofat=sofaq.get()*32000
                chairt=chairq.get()*200
                bookt=bookq.get()*12000
                dresst=dressq.get()*9000
                tablet=tableq.get()*3000
                cupt=cupq.get()*20000
                showcaset=showcaseq.get()*15000
                lft=lfq.get()*350
                sft=sfq.get()*2000

                totalf=(bedt+sofat+chairt+bookt+dresst+tablet+cupt+showcaset+lft+sft)

        if flag==10:
                try:
                        
                        if bedq.get()!=0:
                                textarea.insert(END,f"\n Bed      \t\t{bedq.get()}\t\t{bedt}")
                        if sofaq.get()!=0:
                                textarea.insert(END,f"\n Sofa     \t\t{sofaq.get()}\t\t{sofat}")
                        if chairq.get()!=0:
                                textarea.insert(END,f"\n Chair    \t\t{chairq.get()}\t\t{chairt}")
                        if bookq.get()!=0:
                                textarea.insert(END,f"\n Bookshelf\t\t{bookq.get()}\t\t{bookt}")
                        if dressq.get()!=0:
                                textarea.insert(END,f"\n Dressing T.\t\t{dressq.get()}\t\t{dresst}")
                        if tableq.get()!=0:
                                textarea.insert(END,f"\n Table    \t\t{tableq.get()}\t\t{tablet}")
                        if showcaseq.get()!=0:
                                textarea.insert(END,f"\n Showcase  \t\t{showcaseq.get()}\t\t{showcaset}")
                        if cupq.get()!=0:
                                textarea.insert(END,f"\n Cupboard  \t\t{cupq.get()}\t\t{cupt}")
                        if lfq.get()!=0:
                                textarea.insert(END,f"\n Lamp      \t\t{lfq.get()}\t\t{lft}")
                        if sfq.get()!=0:
                                textarea.insert(END,f"\n Shoerack  \t\t{sfq.get()}\t\t{sft}")

                        fadd=textarea.get('1.0',END)
                except Exception:
                        print("")


                
def billdatae():
        global eadd, totale


        if flag==11:        
                phonet=phonequant.get()*65000
                fridget=fridgeyquant.get()*45000
                let=leq.get()*85000
                wet=weq.get()*23000
                het=heq.get()*1800
                spet=speq.get()*12000
                tet=teq.get()*32000
                aet=aeq.get()*45000
                gett=geyq.get()*19000
                iet=ieq.get()*500

                totale=phonet+fridget+let+wet+het+spet+tet+aet+gett+iet

        if flag==11:
                try:
                
                        if phonequant.get()!=0:
                                textarea.insert(END,f"\n Phone     \t\t{phonequant.get()}\t\t{phonet}")        
                        if fridgeyquant.get()!=0:
                                textarea.insert(END,f"\n Fridge    \t\t{fridgeyquant.get()}\t\t{fridget}")
                        if leq.get()!=0:
                                textarea.insert(END,f"\n Laptop    \t\t{leq.get()}\t\t{let}")
                        if weq.get()!=0:
                                textarea.insert(END,f"\n Washing M.\t\t{weq.get()}\t\t{wet}")
                        if heq.get()!=0:
                                textarea.insert(END,f"\n Heater    \t\t{heq.get()}\t\t{het}")
                        if speq.get()!=0:
                                textarea.insert(END,f"\n Speaker   \t\t{speq.get()}\t\t{spet}")
                        if teq.get()!=0:
                                textarea.insert(END,f"\n TV        \t\t{teq.get()}\t\t{tet}")
                        if aeq.get()!=0:
                                textarea.insert(END,f"\n AC        \t\t{aeq.get()}\t\t{aet}")
                        if geyq.get()!=0:
                                textarea.insert(END,f"\n Geyser    \t\t{geyq.get()}\t\t{gett}")
                        if ieq.get()!=0:
                                textarea.insert(END,f"\n Iron      \t\t{ieq.get()}\t\t{iet}")
                        eadd=textarea.get('1.0',END)

                except Exception:
                        print("")




        

def billdatal():
        global ladd, totall

        if flag==12:
                blt=blq.get()*150
                clt=clq.get()*400
                hlt=hlq.get()*1100
                jlt=jlq.get()*950
                klt=klq.get()*350
                plt=plq.get()*900
                slt=slq.get()*1500
                sareelt=sareelq.get()*1200
                shirtlt=shirtlq.get()*800
                wlt=wlq.get()*1900

                totall=blt+clt+hlt+jlt+klt+plt+slt+sareelt+shirtlt+wlt

        
        if flag==12:
                try:
                
                        if blq.get()!=0:
                                textarea.insert(END,f"\n Belt      \t\t{blq.get()}\t\t{blt}")
                        if clq.get()!=0:
                                textarea.insert(END,f"\n Carpet    \t\t{clq.get()}\t\t{clt}")
                        if hlq.get()!=0:
                                textarea.insert(END,f"\n Hairdryer \t\t{hlq.get()}\t\t{hlt}")
                        if jlq.get()!=0:
                                textarea.insert(END,f"\n Jeans     \t\t{jlq.get()}\t\t{jlt}")
                        if klq.get()!=0:
                                textarea.insert(END,f"\n Kurti     \t\t{klq.get()}\t\t{klt}")
                        if plq.get()!=0:
                                textarea.insert(END,f"\n Perfume   \t\t{plq.get()}\t\t{plt}")
                        if slq.get()!=0:
                                textarea.insert(END,f"\n Sunglasses\t\t{slq.get()}\t\t{slt}")
                        if sareelq.get()!=0:
                                textarea.insert(END,f"\n Saree     \t\t{sareelq.get()}\t\t{sareelt}")
                        if shirtlq.get()!=0:
                                textarea.insert(END,f"\n Shirt     \t\t{shirtlq.get()}\t\t{shirtlt}")
                        if wlq.get()!=0:
                                textarea.insert(END,f"\n Watch     \t\t{wlq.get()}\t\t{wlt}")
                        ladd=textarea.get('1.0',END)
                except Exception:
                        print("")



def payment():

        

        global windowx
        windowx = Tk()
        windowx.title(" PAYMENT METHOD")
        windowx.configure(background="black")
        windowx.after(50000,lambda:windowx.destroy())

        cod=StringVar()
        cd=StringVar()

        Label (windowx,text="CHOOSE PAYMENT METHOD:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=1,column=0,sticky=W)
        
        rad2= Radiobutton(windowx,text="CREDIT CARD",bg="black",fg="#EC4D37",value=2,textvariable=cd,width=10,command=credit)
        rad1= Radiobutton(windowx,text="COD",bg="black",fg="#EC4D37",value=1,textvariable=cod,width=10,command=codd)


        rad1.grid(row=1,column=2,sticky=W)
        rad2.grid(row=1,column=1,sticky=W)
        

        rad2.deselect()
     
        bt15= Button(windowx,text="OK",bg="#EC4D37",fg="black",font="none 12 bold",width=5,command=saveBill)
        bt15.grid(row=5,column=5,sticky=S)

def codd():
        Label (windowx,text="OOOOOOOOOOOOOOO",bg="black",fg="black",font="none 12 bold").grid(row=2,column=0,sticky=W)
        Label (windowx,text="OOOOOOOOOOOOOOO",bg="black",fg="black",font="none 12 bold").grid(row=2,column=1,sticky=W)        

        Label (windowx,text="OOOOOOOOOOOOOOO",bg="black",fg="black",font="none 12 bold").grid(row=3,column=0,sticky=W)
        Label (windowx,text="OOOOOOOOOOOOOOOO",bg="black",fg="black",font="none 12 bold").grid(row=3,column=1,sticky=W)        


def credit():
        global ccad1, ccad2
        
        Label (windowx,text="Enter Credit Card NO:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=2,column=0,sticky=W)

        ccad1= Entry(windowx,width=20,bg="#EC4D37")
        ccad1.grid(row=2,column=1)

        Label (windowx,text="Enter Exp Date:",bg="black",fg="#EC4D37",font="none 12 bold").grid(row=3,column=0,sticky=W)

        ccad2= Entry(windowx,width=20,bg="#EC4D37")
        ccad2.grid(row=3,column=1)


def exitBill():
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            window.destroy()
            
def saveBill():
        windowx.destroy()
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
                
                
                if stockupdates()==False:
                        print("")
                else:
                        
                        bill_data=textarea.get('1.0',END)
                        f1=open("C:\\Users\\chakr\\Downloads\\KamiKart\\Invoice\\"+str(bill_no.get()+txtent1.get())+".txt","w")
                        f1.write(bill_data)
                        f1.close()
                        messagebox.showinfo("Saved",f"Bill no. :{bill_no.get()}{txtent1.get()} saved successfully")

window.mainloop()

        
