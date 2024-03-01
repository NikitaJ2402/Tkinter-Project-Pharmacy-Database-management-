from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpiryDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.Storage=StringVar()
        self.BloodPressure=StringVar()
        self.Medication=StringVar()
        self.PatientID=StringVar()
        self.NHSNumber=StringVar()
        self.PatientN=StringVar()
        self.DOB=StringVar()
        self.PatientsAddress=StringVar()


    


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg='red',bg='white',font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        #_________DATAFRAME for PATIENT INFORMATION________________

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                                         font=("times new roman",12,"bold"),text="Patient Information")

        DataFrameLeft.place(x=0,y=5,width=980,height=400)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                                         font=("times new roman",12,"bold"),text="Prescription")

        DataFrameRight.place(x=990,y=5,width=460,height=350)


        #_________________BUTTONS FRAME________________

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        #_________________DETAILS FRAME________________

        DetailFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailFrame.place(x=0,y=600,width=1530,height=190)

        #__________________Dataframeleft_______________

        lblNameTablet=Label(DataFrameLeft,text="Names of Tablet : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=35)
        comNametablet["values"]=("Nicip Cold","Corona Vaccine","Dolo 650","Crocin","Paracetamol","Aspririn","Ibuprofin","Naproxen","Acetaminophen","Activan","Adderall")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial,12,bold"),text="Reference No : ",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.ref,width=30)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial,12,bold"),text="Dose : ",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.Dose,width=30)
        txtDose.grid(row=2,column=1)

        lblNotablets=Label(DataFrameLeft,font=("arial,12,bold"),text="No of Tablets : ",padx=2,pady=6)
        lblNotablets.grid(row=3,column=0,sticky=W)
        txtNotablets=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.NumberofTablets,width=30)
        txtNotablets.grid(row=3,column=1)
        
        lblLot=Label(DataFrameLeft,font=("arial,12,bold"),text="Lot : ",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.Lot,width=30)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial,12,bold"),text="Issue Date : ",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.IssueDate,width=30)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial,12,bold"),text="Expiry Date : ",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.ExpiryDate,width=30)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial,12,bold"),text="Daily Dose : ",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.DailyDose,width=30)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial,12,bold"),text="Side Effect : ",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.SideEffect,width=30)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataFrameLeft,font=("arial,12,bold"),text="Further Information : ",padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.FurtherInformation,width=30)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,font=("arial,12,bold"),text="Blood Pressure : ",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.BloodPressure,width=30)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial,12,bold"),text="Storage Advice : ",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.Storage,width=30)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft,font=("arial,12,bold"),text="Medication : ",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.Medication,width=30)
        txtMedicine.grid(row=3,column=3)

        lblPatientID=Label(DataFrameLeft,font=("arial,12,bold"),text="Patient ID : ",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.PatientID,width=30)
        txtPatientID.grid(row=4,column=3)

        lblNHSNumber=Label(DataFrameLeft,font=("arial,12,bold"),text="NHS Number : ",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.NHSNumber,width=30)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,font=("arial,12,bold"),text="Patient Name : ",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.PatientN,width=30)
        txtPatientName.grid(row=6,column=3)

        lblDOB=Label(DataFrameLeft,font=("arial,12,bold"),text="Date of Birth : ",padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.DOB,width=30)
        txtDOB.grid(row=7,column=3)

        lblAddress=Label(DataFrameLeft,font=("arial,12,bold"),text="Patient Address : ",padx=2,pady=6)
        lblAddress.grid(row=8,column=2,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("arial,12,bold"),textvariable=self.PatientsAddress,width=30)
        txtAddress.grid(row=8,column=3)


        #________________________DATAFRAME RIGHT__________________________


        self.txtPrescription=Text(DataFrameRight,font=("arial,12,bold"),width=38,height=13,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        #_____________BUTTONS__________________________

        btnPrescription=Button(ButtonFrame,text="Prescription",bg="green",fg="white",font=("arial",10,"bold"),width=30,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",command=self.iPrescriptionData,bg="green",fg="white",font=("arial",10,"bold"),width=30,height=1,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Update",bg="green",fg="white",font=("arial",10,"bold"),width=30,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",bg="green",fg="white",font=("arial",10,"bold"),width=30,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,text="Clear",bg="green",fg="white",font=("arial",10,"bold"),width=30,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,text="Exit",bg="green",fg="white",font=("arial",10,"bold"),width=28,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=5)


        #____________________Table___________________

        #____________________Scrollbar_________________

        scroll_x=ttk.Scrollbar(DetailFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailFrame,orient=VERTICAL)

        self.Hospital_table=ttk.Treeview(DetailFrame,column=("Nameoftable","Ref","Dose","NoOfTablets","lot","IssueDate",
                                    "ExpiryDate","DailyDose","Storage","NHSNumber","PName","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)                                 
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_x=ttk.Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("Nameoftable",text="Name of Tablets")
        self.Hospital_table.heading("Ref",text="Reference Number")
        self.Hospital_table.heading("Dose",text="Dose")
        self.Hospital_table.heading("NoOfTablets",text="Number of Tablets")
        self.Hospital_table.heading("lot",text="Lot")
        self.Hospital_table.heading("IssueDate",text="Issue Date")
        self.Hospital_table.heading("ExpiryDate",text="Expiry Date")
        self.Hospital_table.heading("DailyDose",text="Daily Dose")
        self.Hospital_table.heading("Storage",text="Storage")
        self.Hospital_table.heading("NHSNumber",text="NHS Number")
        self.Hospital_table.heading("PName",text="Patient Name")
        self.Hospital_table.heading("DOB",text="Date of Birth")
        self.Hospital_table.heading("Address",text="Address")

        self.Hospital_table['show']="headings"
        self.Hospital_table.pack(fill=BOTH,expand=1)

        self.Hospital_table.column("Nameoftable",width=100)
        self.Hospital_table.column("Ref",width=100)
        self.Hospital_table.column("Dose",width=100)
        self.Hospital_table.column("NoOfTablets",width=100)
        self.Hospital_table.column("lot",width=100)
        self.Hospital_table.column("IssueDate",width=100)
        self.Hospital_table.column("ExpiryDate",width=100)
        self.Hospital_table.column("DailyDose",width=100)
        self.Hospital_table.column("Storage",width=100)
        self.Hospital_table.column("NHSNumber",width=100)
        self.Hospital_table.column("PName",width=100)
        self.Hospital_table.column("DOB",width=100)
        self.Hospital_table.column("Address",width=100)


        self.Hospital_table.pack(fill=BOTH,expand=1)
        # self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)                                                   #error


    #___________________Functionality Declaration______________________

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="MyData")
            mycursor=conn.cursor()
            mycursor.execute("insert into Hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                 self.ref.get(),
                                                                                                 self.Dose.get(),
                                                                                                 self.NumberofTablets.get(),
                                                                                                 self.Lot.get(),
                                                                                                 self.IssueDate.get(),
                                                                                                 self.ExpiryDate.get(),
                                                                                                 self.DailyDose.get(),
                                                                                                 self.Storage.get(),
                                                                                                 self.NHSNumber.get(),
                                                                                                 self.PatientN.get(),
                                                                                                 self.DOB.get(),
                                                                                                 self.PatientsAddress.get() ))

            conn.commit()
            self.Fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been Inserted")


    def Fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="root",database="MyData")
         mycursor=conn.cursor()
         mycursor.execute("select * from Hospital")
         rows=mycursor.fetchall()
         if len(rows)!=0:
            self.Hospital_table.delete(* self.Hospital_table.get_children())
            for i in rows:
                self.Hospital_table.insert("",END,Values=i)
            conn.commit()
         conn.close()


         def get_cursor(self,event):
            cursor_row=self.Hospital_table.focus()
            content=self.Hospital_table.item(cursor_row)
            row=content["values"]
            self.Nameoftable.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets(row[3])
            self.Lot.set(row[4])
            self.IssueDate.set(row[5])
            self.ExpiryDate.set(row[6])
            self.DailyDose.set(row[7])
            self.Storage.set(row[8])
            self.NHSNumber.set(row[9])
            self.PatientN(row[10])
            self.DOB(row[11])
            self.PatientsAddress(row[12])
















    

root=Tk()
ob=Hospital(root)
root.mainloop()