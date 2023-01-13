# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:36:20 2021

@author: musta
"""
import pandas as pd

def main():
    df = pd.read_csv(r'C:\Users\musta\OneDrive\Desktop\Python-Softwerar\salary_2021_11_28_20_25_47.csv')
    print(df)
    while True:
        x = int(input("Enter a number you want:"))
        if x > 0 and x < 5:
            if x == 1:
              data = display(df)
              print(data)
            if x == 2:
                print('Add')
                add(df)
            if x == 3:
                print('remove')
                remove(df, str(input("Enter a name you want:")))
                #df.to_csv(r'C:\Users\musta\OneDrive\Desktop\Python-Softwerar\salary_2021_11_28_20_25_47.csv', index=False,
                     #header=False)
            if x == 4:
                print('exit')
            else:
                print ( 'choose between 1 to 4')

def display(df):
    print(df)
#Add data
def add(df):
    
    while True:
        row = []
        N = str(input("Enter a name:"))
        row.append(N)
        
        A = int(input("Enter the age:"))
        row.append(A)
        
        S = int(input("Enter the salary:"))
        row.append(S)
        
        #row = [name, age, salary]
        df.loc[len(df)] = row
       
        #print(df)
        df.to_csv(r'C:\Users\musta\OneDrive\Desktop\Python-Softwerar\salary_2021_11_28_20_25_47.csv', mode='a', index=False,
                  header=False)
#def remove(m, n):        
         #d= int(input("Enter a number you want:"))
         m = m.drop(m[m.Name ==n ].index)
         m.to_csv(r'C:\Users\musta\OneDrive\Desktop\Python-Softwerar\salary_2021_11_28_20_25_47.csv', index=False,
              header=True)
         
         #print(m)

    
    
main()

#df = df.drop(df[df.name == 'abd'].index)
        