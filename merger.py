from tkinter import *
import pandas as pd

def submit_fields():
    excel1 = entry1.get()
    excel2 = entry2.get()
    a = 'b.xlsx'
    df1 = pd.read_excel(excel1)
    print(df1)
    df2 = pd.read_excel(excel2)
    values1 = df1['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or Company name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")']
    values2 = df2['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or Company name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")']
    dataframes = [values1, values2]
    join = pd.concat(dataframes)
    join.to_excel("merge.xlsx")
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

