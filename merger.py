from tkinter import *
import pandas as pd

def submit_fields():
    
    
    # path = 'merge.xlsx'
    # df1 = pd.read_excel(path)
    # SeriesA = df1['Operator']
    # SeriesB = df1['Number']
    # A = pd.Series(entry1.get())
    # B = pd.Series(entry2.get())
    # SeriesA = SeriesA.append(A)
    # SeriesB = SeriesB.append(B)
    excel1 = entry1.get()
    excel2 = entry2.get()
    df1 = pd.read_excel(excel1)
    df2 = pd.read_excel(excel2)
    values1 = df1['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or Company name goes here)','COMML (phone number)','Email ','Site(e.g. "FRCSW")','Room, WS, or Office (Room, Cube or Office)','Building - Floor']
    values2 = df2['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or Company name goes here)','COMML (phone number)','Email ','Site(e.g. "FRCSW")','Room, WS, or Office (Room, Cube or Office)','Building - Floor']
    dataframes = [values1, values2]
    join = pd.concat(dataframes)
    join.to_excel("merge.xlsx")
   # writer.save()
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

