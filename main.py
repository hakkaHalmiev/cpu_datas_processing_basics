import sys

import pandas
import matplotlib.pyplot as plt
import seaborn
from datetime import datetime as dt

df = pandas.read_csv('tempLog.csv')

print("Please select one of the followings:")

print("     1.Read data set")
print("     2.Exit")

num=int(input("Your choice : "))

if (num==1):

    df = pandas.read_csv('tempLog.csv')

    print("     1.Show info about data set")
    print("     2.Show data set")
    print("     3.List named column 'Air' from  data set and calculate average value of this column")
    print("     4.Calculate average values from data set")
    print("     5.List named column 'CPU' from  data set and calculate average value of this column")
    print("     6.Show overview of data set")
    print("     7.Convert from Timestamp to real time")
    print("     8.Show histogram graph of 'Air'")
    print("     9.Show histogram graph of 'CPU'")

    num_1=int(input("Your choice : "))

    if(num_1==1):
        print(df.info())

    elif(num_1==2):
        print(df)


    elif(num_1==3):

        val = int(input("Write first number where you want start to get value : "))
        val_1 = int(input("Write second number where you want finish to get value : "))
        print(df.loc[val:val_1,['Air']])
        print(df.loc[val:val_1, ['Air']].mean())

        val_str = input("Save result ?  [Y]  [N] : ")

        if (val_str == 'Y'):
            text_name = input("Write folder name : ")
            text_name = text_name + ".txt"
            f = open(text_name, "x")
            f.write(str(df.loc[val:val_1, ['Air']]))
            f.close()

    elif(num_1==4):
        val = int(input("Write first number where you want start to get value : "))
        val_1 = int(input("Write second number where you want finish to get value : "))
        print(df.loc[val:val_1].mean())

        val_str = input("Save result ?  [Y]  [N] : ")

        if (val_str == 'Y'):
            text_name = input("Write folder name : ")
            text_name = text_name + ".txt"
            f = open(text_name, "x")
            f.write(str(df.loc[val:val_1].mean()))
            f.close()

    elif(num_1==5):
        val = int(input("Write first number where you want start to get value : "))
        val_1 = int(input("Write second number where you want finish to get value : "))
        print(df.loc[val:val_1, ['CPU']])
        print(df.loc[val:val_1, ['CPU']].mean())

        val_str = input("Save result ?  [Y]  [N] : ")

        if (val_str == 'Y'):
            text_name = input("Write folder name : ")
            text_name = text_name + ".txt"
            f = open(text_name, "x")
            f.write(str(df.loc[val:val_1, ['CPU']]))
            f.close()

    elif(num_1==6):
        print(df.head())

    elif(num_1==7):
        val = int(input("Write a number which number of row you want to get : "))
        print(dt.fromtimestamp(df.loc[val,'Timestamp']))

        val_str=input("Save result ?  [Y]  [N] : ")

        if(val_str=='Y'):
            text_name=input("Write folder name : ")
            text_name=text_name+".txt"
            f = open(text_name, "x")
            f.write(str(dt.fromtimestamp(df.loc[val, 'Timestamp'])))
            f.close()


    elif(num_1==8):
        df.head()
        plt.hist(df['Air'])
        plt.show()

    elif(num_1==9):
        df.head()
        plt.hist(df['CPU'])
        plt.show()
    else:
        print("Invalid!")

else:
    sys.exit()












