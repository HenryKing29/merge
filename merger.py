#from tkinter import *
import pandas as pd
from functools import reduce
excel1 = input("Please enter excel1:\n")
excel2 = input("Please enter excel2:\n")
excel3 = input("Please enter excel3:\n")
excel4 = input("Please enter excel4:\n")
excel5 = input("Please enter excel5:\n")
excel6 = input("Please enter excel6:\n")
excel7 = input("Please enter excel7:\n")
excel8 = input("Please enter excel8:\n")
excel9 = input("Please enter excel8:\n")

df1 = pd.read_excel(excel1,sheet_name=1)
df2 = pd.read_excel(excel2,sheet_name=1)
df3 = pd.read_excel(excel3,sheet_name=1) 
df4 = pd.read_excel(excel4,sheet_name=1) 
df5 = pd.read_excel(excel5,sheet_name=1) 
df6 = pd.read_excel(excel6,sheet_name=1) 
df7 = pd.read_excel(excel7,sheet_name=1)  
df8 = pd.read_excel(excel8,sheet_name=1)
df9 = pd.read_excel(excel9,sheet_name=1)  
df10 = [df1,df2,df3,df4,df5,df6,df7,df8,df9]
# print(df1.get('Team','Subteam'))
#dat = 'EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or\nCompany name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")','Room, WS, or Office (Room,\nCube or Office)','Building - Floor','Asset Status','Service ID','Asset Number','Machine Name','"System Model" (found by hitting the windows key and then typing system, and choosing "System Information")','Port','Additional PC assigned to user?','Scheduled for Tech Refresh?','Acrobat Pro','Visio','Project','Roxio\nSeat?','Date Last Validated Against NMCI Config\nReport','Results of Validation Against NMCI Config\nReport','Developer Seat?  If yes, please fill out the administrator column --------------->','Administrator for developer seat','4.0 NMCI POC Email','Notes']].merge(df2[['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or\nCompany name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")','Room, WS, or Office (Room,\nCube or Office)','Building - Floor','Asset Status','Service ID','Asset Number','Machine Name','"System Model" (found by hitting the windows key and then typing system, and choosing "System Information")','Port','Additional PC assigned to user?','Scheduled for Tech Refresh?','Acrobat Pro','Visio','Project','Roxio\nSeat?','Date Last Validated Against NMCI Config\nReport','Results of Validation Against NMCI Config\nReport','Developer Seat?  If yes, please fill out the administrator column --------------->','Administrator for developer seat','4.0 NMCI POC Email','Notes'
#df11 = ((df1[[dat]]).merge(df2[[dat]])).merge()
#df11 = reduce(lambda left,right: pd.concat(left,right,on=['EmployeeID','Team','Subteam','First Name','Last Name','DCPDS Employee Name','Function (job title)','CAO Shop Code','MAO Code','Source','ORG (NAVAIR or\nCompany name goes here)','COMML (phone number)','Email','Site(e.g. "FRCSW")','Room, WS, or Office (Room,\nCube or Office)','Building - Floor','Asset Status','Service ID','Asset Number','Machine Name','"System Model" (found by hitting the windows key and then typing system, and choosing "System Information")','Port','Additional PC assigned to user?','Scheduled for Tech Refresh?','Acrobat Pro','Visio','Project','Roxio\nSeat?','Date Last Validated Against NMCI Config\nReport','Results of Validation Against NMCI Config\nReport','Developer Seat?  If yes, please fill out the administrator column --------------->','Administrator for developer seat','4.0 NMCI POC Email','Notes']), df10)
df11 = df1.append([df2,df3,df4,df5,df6,df7,df8,df9])
df11.to_excel("merge.xlsx")


