###########################################################################################################################
##
##  Author : Deepika Jagdish Dhote
##  Date : 23/03/2019
##  Program : Bank Management System
##
################################################################################################################################
#Required Imports
import tkinter as tk
from tkinter import CENTER, RIGHT, W, Entry, Label, messagebox
from time import gmtime, strftime


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

#Credit Amount
def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")

	lbl = Label(creditwn,font=(20),text="Enter Amount : ")
	lbl.grid(column=1, row=0,sticky= W,pady= 20)

	txt = Entry(creditwn,width=50)
	txt.grid(column=2,row=0,pady = 20)
	b=tk.Button(creditwn,text="Credit",font=(20),width=20,height=2,command=lambda:crdt_write(creditwn,txt.get(),accnt,name))
	b.place(relx=0.5,rely=0.4,anchor=CENTER)
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,txt.get(),accnt,name))

#Debuit Amount
def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	
	lbl = Label(debitwn,font=(20),text="Enter Amount : ")
	lbl.grid(column=1, row=0,sticky= W,pady= 20)

	txt = Entry(debitwn,width=50)
	txt.grid(column=2,row=0,pady = 20)
	
	b=tk.Button(debitwn,text="Debit",font=(20),width=20,height=2,command=lambda:debit_write(debitwn,txt.get(),accnt,name))
	b.place(relx=0.5,rely=0.4,anchor=CENTER)
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,txt.get(),accnt,name))

#Display Balance
def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

#Display Transaction History
def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="white")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="Pratibha Bank",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="Dark Gray",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History : ",padx=100,pady=20,width=1500,font=(50),bg="Gray",fg="white",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",padx=100,pady=20,width=4000,font=(60))
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy,font=(20),width=20,height=2)
	b.place(relx=0.5,rely=0.8,anchor=CENTER)
	frec.close()

#Log in Page
def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("600x600")
	rootwn.title("Pratibha BANK-"+name)
	rootwn.configure(background='white')
	
	b2=tk.Button(text="Credit Amount",font=(20),width=30,height=2,command=lambda: Cr_Amt(accnt,name))
	
	b3=tk.Button(text= "Debit Amount",font=(20),width=30,height=2,command=lambda: De_Amt(accnt,name))
	
	b4=tk.Button(text="Display Amount",font=(20),width=30,height=2,command=lambda: disp_bal(accnt))
	
	b5=tk.Button(text="Display Transaction History",font=(30),width=30,height=2,command=lambda: disp_tr_hist(accnt))
	
	b6=tk.Button(text="Log Out",font=(20),width=20,height=2,command=lambda: logout(rootwn))

	b2.place(relx=0.5,rely=0.1,anchor=CENTER)
	b3.place(relx=0.5,rely=0.3,anchor=CENTER)	
	b4.place(relx=0.5,rely=0.5,anchor=CENTER)
	b5.place(relx=0.5,rely=0.7,anchor=CENTER)
	b6.place(relx=0.5,rely=0.9,anchor=CENTER)
	
#Log Out
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("700x400")
	loginwn.title("Log in")
	
	#Labels
	lbl = Label(loginwn,font=(20),text="Enter Name : ")
	lbl2 = Label(loginwn,font=(20),text="Enter Account Number : ")
	lbl3 = Label(loginwn,font=(20),text = "Enter Pin : ")


	lbl.grid(column=1, row=0,sticky= W,pady= 20)
	lbl2.grid(column= 1, row = 3,sticky=W,pady=20)
	lbl3.grid(column= 1, row = 6,sticky=W,pady=20)

	#Text Fiels
	txt = Entry(loginwn,width=50)
	txt2 = Entry(loginwn,width=50)
	txt3 = Entry(loginwn,show="*",width=50)

	txt.grid(column=2,row=0,pady = 20)
	txt2.grid(column= 2, row = 3,pady=20)
	txt3.grid(column= 2, row = 6,pady=20)
	
	b=tk.Button(loginwn,text="Submit",font=(20),width=20,height=2,command=lambda: check_log_in(loginwn,txt.get().strip(),txt2.get().strip(),txt3.get().strip()))
	b.place(relx=0.5,rely=0.6,anchor=CENTER)
	b1=tk.Button(text="HOME",font=(20),width=20,height=2,command=lambda: home_return(loginwn))
	b1.place(relx=0.5,rely=0.8,anchor=CENTER)
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,txt.get().strip(),txt2.get().strip(),txt3.get().strip()))
	
#Create New Account
def Create():
	crwn=tk.Tk()
	crwn.geometry("600x300")
	crwn.title("Create Account")
	
	lbl = Label(crwn,font=(20),text="Enter Name : ")
	lbl2 = Label(crwn,font=(20),text="Enter Amount To Credit : ")
	lbl3 = Label(crwn,font=(20),text = "Enter Desired Pin : ")


	lbl.grid(column=1, row=0,sticky= W,pady= 20)
	lbl2.grid(column= 1, row = 3,sticky=W,pady=20)
	lbl3.grid(column= 1, row = 6,sticky=W,pady=20)

	#Text Fiels
	txt = Entry(crwn,width=50)
	txt2 = Entry(crwn,width=50)
	txt3 = Entry(crwn,show="*",width=50)

	txt.grid(column=2,row=0,pady = 20)
	txt2.grid(column= 2, row = 3,pady=20)
	txt3.grid(column= 2, row = 6,pady=20)

	b=tk.Button(crwn,text="Submit",font=(20),width=20,height=2,command=lambda: write(crwn,txt.get().strip(),txt2.get().strip(),txt3.get().strip()))
	b.place(relx=0.5,rely=0.8,anchor=CENTER)
	crwn.bind("<Return>",lambda x:write(crwn,txt.get().strip(),txt2.get().strip(),txt3.get().strip()))
	return


#Staring Point of Project
def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("800x600")
	rootwn.title("Pratibha Bank")
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")

	l_title=tk.Message(text="Pratibha BANKING\nSYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="darkgray",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")

	b1=tk.Button(text = "LOG IN",font=(20),width=20,height=2,command=lambda: log_in(rootwn),anchor=CENTER)
	b2=tk.Button(text = "Create New Account",font=(20),width=20,height=2,command = Create)

	b6=tk.Button(text = "Quit",font=(20),width=20,height=2,command=rootwn.destroy)

	b1.place(relx=0.5,rely=0.4,anchor=CENTER)
	b2.place(relx=0.5,rely=0.5,anchor=CENTER)	
	b6.place(relx=0.5,rely=0.6,anchor=CENTER)

	rootwn.mainloop()

Main_Menu()
