from tkinter import *
import pandas as pd

def submit_fields():
    excel1 = entry1.get()
    excel2 = entry2.get()
    a = 'b.xlsx'
    df1 = pd.read_excel(excel1,sheet_name=1)
 #   print(df1)
    df2 = pd.read_excel(excel2,sheet_name=1) 
   # print(df1.get('Team','Subteam'))
    df3 = df1[['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or\nCompany name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")','Room, WS, or Office (Room,\nCube or Office)','Building - Floor','Asset Status','Service ID','Asset Number','Machine Name','"System Model" (found by hitting the windows key and then typing system, and choosing "System Information")','Port','Additional PC assigned to user?','Scheduled for Tech Refresh?','Acrobat Pro','Visio','Project','Roxio\nSeat?','Date Last Validated Against NMCI Config\nReport','Results of Validation Against NMCI Config\nReport','Developer Seat?  If yes, please fill out the administrator column --------------->','Administrator for developer seat','4.0 NMCI POC Email','Notes']].merge(df2[['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or\nCompany name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")','Room, WS, or Office (Room,\nCube or Office)','Building - Floor','Asset Status','Service ID','Asset Number','Machine Name','"System Model" (found by hitting the windows key and then typing system, and choosing "System Information")','Port','Additional PC assigned to user?','Scheduled for Tech Refresh?','Acrobat Pro','Visio','Project','Roxio\nSeat?','Date Last Validated Against NMCI Config\nReport','Results of Validation Against NMCI Config\nReport','Developer Seat?  If yes, please fill out the administrator column --------------->','Administrator for developer seat','4.0 NMCI POC Email','Notes']])
    df3.to_excel("merge.xlsx")
    entry1.delete(0, END)
    entry2.delete(0, END)
root = Tk()
Label(root, text="File1").grid(row=0)
Label(root, text="File2").grid(row=1)
entry1 = Entry(root)
entry2 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(root, text='Quit', command=root.quit).grid(row=3,column=0, pady=4)
Button(root, text='Submit', command=submit_fields).grid(row=3,column=1, pady=4)

  
root.mainloop()

