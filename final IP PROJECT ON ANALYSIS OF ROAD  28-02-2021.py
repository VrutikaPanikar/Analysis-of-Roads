# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:16:51 2020

@author: SEJAL
"""

import pandas as  pd
import matplotlib.pyplot as plt

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("            WELCOME TO OUR PROJECT ON ANALYSIS OF ROAD             ") 
print("                                              By Vrutika & Harshita\
                                                           & Krishna      ")    
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    print("1.Read complete csv file")
    print("2.Read complete csv file without index")
    print("3.Line chart")
    print("4.Bar chart")
    print("5.Histogram")
    print("6.Data Manipulation")
    print("7.Sorting the data")
    print("8.Reading top and bottom records from the file")
    print("9.Reading specific columns")
    print("10.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
       print()
       print("Reading data from csv file")
       print()
       print()
       print()
       df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv')
       pd.set_option('display.max_columns', None)
       pd.set_option('display.width', None)
       print(df)
   
    elif choice==2:
       print()
       print("Reading data from csv file without index")
       print() 
       print()
       print()
       df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',index_col=0)
       pd.set_option('display.max_columns', None)
       pd.set_option('display.width', None)
       print(df)
       
    elif choice==3:
        print("1. City vs No. Of Fatality chart of GUJARAT")
        print("2. City vs No. Of Fatality chart of MAHARASHTRA")
        print("3. City vs No. Of Fatality chart of HIMACHAL PRADESH")
        print("4. City vs No. Of Fatality chart of RAJASTHAN")
        print("5. City vs No. Of Fatality chart of ODISHA")
        print("6. City vs No. Of Fatality chart of WEST BENGAL")
        print("7. City vs No. Of Fatality chart of KERALA") 
        print("8. City vs No. Of Fatality chart of TAMIL NADU")
        print("9. CITY vs No. Of Fatality chart of ALL THE 8 STATES")
       
        choice1=int(input("Enter your choice: "))
        if choice1==1:
            city=[1,2,3,4,5]
            Fatality=[953,180,256,2000,213]
            plt.xlabel=("CITY")
            plt.ylabel("NO. OF FATALITY")
            plt.title("City vs No. Of Fatality chart of GUJARAT")
            plt.xticks(city,['Ahemdabad','Gandhinagar','Mehsana','Rajkot','Surat'])
            plt.plot(city,Fatality,'b',linestyle='dashed',marker='.', markersize=8,markeredgecolor="black")
            plt.show()
            print()
            print()
            print()
        elif choice1==2:
            city=[1,2,3,4,5]
            Fatality=[199,200,373,250,12000]
            plt.xlabel=("CITY")
            plt.ylabel("NO. OF FATALITY")
            plt.title("City vs No. Of Fatality chart of RAJASTHAN")
            plt.xticks(city,['Aurangabad','Kolhapur','Mumbai','Nagpur','Pune'])
            plt.plot(city,Fatality,linestyle='solid',marker='p', markersize=10,markeredgecolor="green")
            plt.grid()
            plt.show()
            print()
            print()
            print()
           
        elif choice1==3:
             city=[1,2,3,4,5]
             Fatality=[278,150,100,2155,269]
             plt.xlabel=("CITY")
             plt.ylabel("NO. OF FATALITY")
             plt.title("City vs No. Of Fatality chart of HIMACHAL PRADESH")
             plt.xticks(city,['Dharamshala','Manali','Mandi','Shimla','Solan'])
             plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="cyan")
             plt.show()
             plt.grid()
             print()
             print()
             print()
             
        elif choice1==4:
           city=[1,2,3,4,5]
           Fatality=[893,753,161,1500,1218]
           plt.xlabel=("CITY")
           plt.ylabel("NO. OF FATALITY")
           plt.title("City vs No. Of Fatality chart of RAJASTHAN")
           plt.xticks(city,['Bikaner','Jaipur','Jaisalmer','Kota','Udaipur'])
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="red")
           plt.grid()
           plt.show()
           print()
           print()
           print()
            
        elif choice1==5:
           city=[1,2,3,4,5]
           Fatality=[5315,350,6180,200,448]
           plt.xlabel=("CITY")
           plt.ylabel("NO. OF FATALITY")
           plt.xticks(city,['Bhubhaneshwar','Cuttack','Kharagpur','Konark','Puri'])
           plt.title("City vs No. Of Fatality chart of ODISHA")
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="magenta")
           plt.grid()
           plt.show()
           print()
           print()
           print() 
           
        elif choice1==6:
           city=[1,2,3,4,5]
           Fatality=[10500,500,300,294,99]
           plt.xlabel=("CITY")
           plt.ylabel("NO. OF FATALITY")
           plt.title("City vs No. Of Fatality chart of WEST BENGAL")
           plt.xticks(city,['Asanol','Darjeeling','Howrah','Kolkata','Malda',])
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="black")
           plt.grid()
           plt.show()
           print()
           print()
           print() 
           
        elif choice1==7:
           city=[1,2,3,4,5]
           Fatality=[4155,155,125,179,211,]
           plt.xlabel=("CITY")
           plt.ylabel("NO. OF FATALITY")
           plt.title("City vs No. Of Fatality chart of KERELA")
           plt.xticks(city,['Kannur','Kochi','Kolam','Kozhikode','Thrissur'])
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="yellow")
           plt.grid()
           plt.show()
           print()
           print()
           print()
           
        elif choice1==8:
           city=[1,2,3,4,5]
           Fatality=[409,10525,1548,800,644]
           plt.xlabel=("CITY")
           plt.ylabel("NO. OF FATALITY")
           plt.title("City vs No. Of Fatality chart of TAMIL NADU")
           plt.xticks(city,['Alappuzha','Chennai','Coimbatore','Salem','Vellore'])
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=10,markeredgecolor="blue")
           plt.grid()
           plt.show()
           print()
           print()
           print()
           
        elif choice1==9:
           city=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34
                 ,35,36,37,38,39,40]
           Fatality=[953,409,10500,199,5315,893,10525,1548,350,500,278,180,300,753,161,4115,6180,155,125,200
                     ,1500,179,150,100,99,256,373,250,12000,448,2000,800,2155,269,213,211,1218,644,569,125]
           plt.xlabel=("CITIES")
           plt.ylabel("NO. OF FATALITY")
           plt.title("CITY vs No. Of Fatality chart of ALL THE 8 STATES")
           plt.xticks(city,['AHEMDABAD','ALAPPUZHA','ASANOL','AURANGABAD','BHUBNESHWAR','BIKNAER','CHENNAI'
                            ,'COIMBATORE','CUTTACK','DARJEELING','DHARAMSHALA','GANDHINAGAR','HOWRAH','JAIPUR'
                            ,'JAISALMER','KANNUR','KHARAGPUR','KOCHI','KOLAM','KOLHAPUR','KOLKATA','KONARK'
                            ,'KOTA','KOZHIKODE','MANALI','MANDI','MALDA','MEHSANA','MUMBAI','NAGPUR','PUNE'
                            ,'PURI','PURI','RAJKOT','SALEM','SHIMLA','SOLAN','SURAT','THRISSUR','UDAIPUR'
                            ,'VELLORE'],rotation='vertical',fontsize=8)
           plt.plot(city,Fatality,linestyle='solid',marker='2', markersize=8,markeredgecolor="CYAN")
           plt.grid()
           plt.show()
        
        else:
            print("ENTER VALID NUMBER!!!")
            print()
            print()
            print()
           
    elif choice==4:
        print("1. City vs Rank chart of GUJARAT")
        print("2. City vs Rank chart of MAHARASHTRA")
        print("3. City vs Rank chart of HIMACHAL PRADESH")
        print("4. City vs Rank chart of RAJASTHAN")
        print("5. City vs Rank chart of ODISHA")
        print("6. City vs Rank chart of WEST BENGAL")
        print("7. City vs Rank chart of KERELA")
        print("8. City vs Rank chart of TAMIL NADU")
        print("9. CITY vs Rank chart of ALL THE 8 STATES")

        choice2=int(input("Enter your choice: "))

        if choice2==1:
            city=[1,2,3,4,5]
            rank=[7,8,99,6,2]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank chart of GUJARAT")
            plt.xticks(city,['Ahemdabad','Gandhinagar','Mehsana','Rajkot','Surat'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==2:
            city=[1,2,3,4,5]
            rank=[288,16,49,15,14]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank chart of RAJASTHAN")
            plt.xticks(city,['Aurangabad','Kolhapur','Mumbai','Nagpur','Pune'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==3:
            city=[1,2,3,4,5]
            rank=[629,477,75,65,159]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank chart of HIMACHAL PRADESH")
            plt.xticks(city,['Dharamshala','Manali','Mandi','Shimla','Solan'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==4:
            city=[1,2,3,4,5]
            rank=[319,44,50,302,54]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank of RAJASTHAN")
            plt.xticks(city,['Bikaner','Jaipur','Jaisalmer','Kota','Udaipur'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==5:
            city=[1,2,3,4,5]
            rank=[288,232,57,166,256]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.xticks(city,['Bhubhaneshwar','Cuttack','Kharagpur','Konark','Puri'])
            plt.title("City vs Rank chart of ODISHA")
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==6:
            city=[1,2,3,4,5]
            rank=[129,275,255,382,200]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank chart of WEST BENGAL")
            plt.xticks(city,['Asanol','Darjeeling','Howrah','Kolkata','Malda'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
           
        elif choice2==7:
            city=[1,2,3,4,5]
            rank=[372,300,254,324,350]
            plt.xlabel=("CITY")
            plt.ylabel("RANKY")
            plt.title("City vs Rank chart of KERELA")
            plt.xticks(city,['Kannur','Kochi','Kolam','Kozhikode','Thrissur'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==8:
            city=[1,2,3,4,5]
            rank=[380,12,40,172,272]
            plt.xlabel=("CITY")
            plt.ylabel("RANK")
            plt.title("City vs Rank chart of TAMIL NADU")
            plt.xticks(city,['Alappuzha','Chennai','Coimbatore','Salem','Vellore'])
            plt.bar(city,rank)
            plt.grid()
            plt.show()
            print()
            print()
            print()
            
        elif choice2==9:
           city=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34
                 ,35,36,37,38,39,40]
           rank=[7,380,179,288,319,312,40,232,129,629,8,275,44,50,57,372,300,16,255,166,302,254,42,477,75,382
                 ,99,49,15,14,256,6,173,243,65,159,2,324,54,272]
           plt.xlabel=("CITIES")
           plt.ylabel("RANK")
           plt.title("CITY vs Rank chart of ALL THE 8 STATES")
           plt.xticks(city,['AHEMDABAD','ALAPPUZHA','ASANOL','AURANGABAD','BHUBNESHWAR','BIKNAER','CHENNAI'
                            ,'COIMBATORE','CUTTACK','DARJEELING','DHARAMSHALA','GANDHINAGAR','HOWRAH','JAIPUR'
                            ,'JAISALMER','KANNUR','KHARAGPUR','KOCHI','KOLAM','KOLHAPUR','KOLKATA','KONARK'
                            ,'KOTA','KOZHIKODE','MANALI','MANDI','MALDA','MEHSANA','MUMBAI','NAGPUR','PUNE'
                            ,'PURI','PURI','RAJKOT','SALEM','SHIMLA','SOLAN','SURAT','THRISSUR','UDAIPUR'
                            ,'VELLORE'],rotation='vertical',fontsize=8)
           plt.bar(city,rank)
           plt.grid()
           plt.show()
          
        else:
            print("ENTER VALID NUMBER!!!")
            print()
            print()
            print()
            
    elif choice==5:    
        print("1. Fatality vs No.Of Cities chart ")
        print("2. Rank vs No.Of Cities chart ")
        
        choice3=int(input("Enter your choice: "))
        
        if choice3==1:
            no_of_cities1=[29,4,1,0,1,1,1,0,0,0,2,1]
            plt.hist(no_of_cities1,bins=[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000],
                     color='red',edgecolor='k')
            plt.xlabel=("FATALITY")
            plt.ylabel("NO.OF CITIES")
            plt.title("HISTOGRAM SHOWING NO.OF CITIES IN THE GIVEN RANGE OF FATALITY")
            plt.show()
            
        elif choice3==2:
             no_of_cities2=[17,5,8,8,1,0,1]
             plt.hist(no_of_cities2,bins=[0,100,200,300,400,500,600,700],color='green',edgecolor='red')
             plt.xlabel=("RANK")
             plt.ylabel("NO.OF CITIES")
             plt.title("HISTOGRAM SHOWING NO.OF CITIES IN THE GIVEN RANGE OF RANK")
             plt.show()
    
        else:
            print("ENTER VALID NUMBER!!!")
            print()
            print()
            print()
            
    elif choice==6:
        print("1. Add a new record")
        print("2. Add a new row")
        print("3. Delete a column")
        
        choice4=int(input("Enter your choice: "))
        if choice4==1:
           df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',index_col=0)
           a=input("Enter the name of the city: ")
           b=input("Enter its state: ")
           c=input("Enter its direction:")
           d=input("Enter the road with highest traffic: ")
           e=input("Enter the road most affected by rain: ")
           f=input("Enter the road with max accidents: ")
           g=input("Enter the number of fatalities: ")
           h=input("Enter rank in terms of cleanliness:")
           dict1={'City':a,'State':b,'Direction':c,'Road With Highest Traffic':d,'Road which is most affected by rain':e,'ROAD where max. accidents occur':f,'No. of Fatalities':g,'Rank in Terms of Cleanliness':h}
           print(dict1)
           df=df.append(dict1,ignore_index=True)
           df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv')
           pd.set_option('display.max_columns', None)
           pd.set_option('display.width', None)

           print(df)
        if choice4==2:
            df['Work In Progress']=[20,10,34,16,4,5,0,12,13,15,18,9,10,4,2,5,7,18,19,20,20,10,34,16,4,5,0,12,13,15,18,9,10,4,2,5,7,18,19,20]
            print(df)
        if choice4==3:
            del1=("Enter the column to delete: ")
            del df[del1]
            print(df)
    
    elif choice==7:
        df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv')
        print("Press 1 to arrange the record as per the STATE NAME")
        print("Press 2 to arrange the record as per the ROAD WITH HIGHEST TRAFFIC")
        print("Press 3 to arrange the record as per the ROAD WHICH IS MOST AFFECTED BY RAIN")
        print("Press 4 to arrange the record as per the ROAD WHERE MAX ACCIDENTS OCCUR")
        print("Press 5 to arrange the record as per the NUMBER OF FATALITY")
        print("Press 6 to arrange the record as per the RANK IN TERMS OF CLEANLINESS")
        
        choice5=int(input("Enter your choice: "))
        
        if choice5==1:
            df.sort_values(["State"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
        
        if choice5==2:
            df.sort_values(["Road With Highest Traffic"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
            
        if choice5==3:
            df.sort_values(["Road which is most affected by Rain"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
        
        if choice5==4:
            df.sort_values(["Road where Max. accidents occur"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
        
        if choice5==5:
            df.sort_values(["No. of Fatality"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
        
        if choice5==6:
            df.sort_values(["Rank in Terms of Cleanliness"], inplace=True)
            #inplace: make the changes in passed DataFrame
            print(df)
    
        else:
            print("ENTER A VALID COLUMN!!!")
            print()
            print()
            print()
            
    elif choice==8:
        df=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv')
        print("1. Top Records")
        print("2. Bottom Records")
        
        choice6=int(input("Enter your choice: "))
        
        if choice6==1:
            top=int(input("How many records from top you want to be displayed: "))
            print("First",top,"records are:")
            print(df.head(top))
            
        elif choice6==2:
            bottom=int(input("How many records from bottom you want to be displayed: "))
            print("Last",bottom,"records are:")
            print(df.tail(bottom))
            
        else:
            print("ENTER A VALID NUMBER!!!")
            print()
            print()
            print()
            
    elif choice==9:
        print("Reading Specific columns feom csv file")
        print("1. City with it's State")
        print("2. City with it's Direction")
        print("3. City with it's Road with Highest Traffic")
        print("4. City with it's Road which is most affected by Rain")
        print("5. City with it's Road where Max. accidents occur")
        print("6. City with it's No. of Fatality")
        print("7. City with it's Rank in Terms of Cleanliness")
        
        choice7=int(input("Enter your choice: "))
        
        if choice7==1:
            df1=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',usecols=['City','State'],index_col=0)
            print(df1)
            print()
            print()
            print()
            
        elif choice7==2:
            df2=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',usecols=['City','Direction'],index_col=0)
            print(df2)
            print()
            print()
            print()
            
        elif choice7==3:
            df3=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',usecols=['City','Road With Highest Traffic']
                           ,index_col=0)
            print(df3)
            print()
            print()
            print()
            
        elif choice7==4:
            df4=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',
                            usecols=['City','Road which is most affected by Rain'],index_col=0)
            print(df4)
            print()
            print()
            print()
            
        elif choice7==5:
            df5=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',
                            usecols=['City','Road where Max.accidents occur'],index_col=0)
            print(df5)
            print()
            print()
            print()
            
        elif choice7==6:
            df6=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv'
                            ,usecols=['City','No.of Fatality'],index_col=0)
            print(df6)
            print()
            print()
            print()
            
        elif choice7==7:
            df7=pd.read_csv('E:\projects\ROAD ISSUES ip project (FINAL).csv',
                           usecols=['City','Rank in Terms of Cleanliness'],index_col=0)
            print(df7)
            print()
            print()
            print()
            
        else:
            print("ENTER VALID NUMBER!!!")
            print()
            print()
            print()
            
    elif choice==10:
        print()
        print()
        print("***************THANK YOU***************")
        break

    else:
        print("ENTER A VALID NUMBER!!!")
        print()
        print()
        print()
        