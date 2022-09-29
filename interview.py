# a='{}[]()'
# m=input("enter brackets:-")
# i=0
# if '{'==m[i] and '}'==m[i+1]:
#     print("true")
# elif '['==m[i] and ']'==m[i+1]:
#     print("true")
# elif '('==m[i] and ')'==m[i+1]:
#     print("true")
# else:
#     print("false")



# a='{}[]()'
# m=input("enter brackets:-")
# i=0
# if '{'==m[i] and '}'==m[i+1] in a:
#     print("true")
# elif '['==m[i] and ']'==m[i+1] in a:
#     print("true")
# elif '('==m[i] and ')'==m[i+1]in a:
#     print("true")
# else:
#     print("false")


# a=int(input("enter the num:-"))
# s=''
# i=0
# while i<(a):
#     if i==a-1:
#         p='1/'+str(i+1)
#     else:
#         p='1/'+str(i+1)+"+"
#     s+=p
#     i=i+1
# print(s)
       
# def abc():
#     i=0
#     while i<26:
#         a=65
#         c=a+i
#         print(chr(c), end =" ")
#         i=i+1
# abc()



# list=[[0, 1, 2,'',''], [2, 3, 4,'',''], [3, 4, 5, 6,''], [7, 8, 9, 10, 11], [12, 13, 14,'','']]
# i=0
# l=[]
# while i<len(list):
#     c=0
#     j=0
#     sum=0
#     while j<len(list):
#         if type(list[j][i])==int:
#             sum=sum+list[j][i]
#         if list[j][i]!='':
#             c=c+1
#         j=j+1
#     ave=sum/c
#     l.append(ave)
#     i=i+1
# print(l)
        


# list = ['flour','cheese','carrots']
# i=0
# while i<len(list):
#     a=list[i]
#     print(i,":",a)
#     i=i+1

# l=[ [4,4,3], [1,4,3], [9,8,7] ]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         a=l[i][0]+l[i][j]
#         b=l[i][1]+l[i][j]
#         j=j+1
#     i=i+1
# print(a)
# print(b)
# print(a-b)




# l=[ [3,3,3], [3,3,3], [3,3,3] ]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         a=l[i][0]+l[i][j]
#         b=l[i][1]+l[i][j]
#         j=j+1
#     i=i+1
# print("diffrence:-",a-b)


# l= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# a=''
# while i<len(l):
#     j=0
#     while(j<len(l[i])):
#         a+=l[i][j]
#         j+=1
#     i+=1
# print(a)

# op:-loops

# 0
# *1
# **2
# ***3
# ****4
# *****5
# i=0
# while i<=5:
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j=j+1
#     print(i)
#     i=i+1
    


    
# date=int(input("enter the date"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# if date>=1 and date<=31:
#     if month>=1 and month<=12:
#         if year>=2000 and year<=2024:
#             if date<=31 and month==month:
#                 nextdate=date+1 
#                 print(nextdate,"/",month,"/",year)
#             elif month>=12 and year==year:
#                 nextdate=date+1
#                 nextmonth=month+1
#                 print(nextdate,"-",nextmonth,"-",year)
#             elif month>=12 and year>=2000:
#                 nextdate=date+1
#                 nextmonth=month+1
#                 nextyear=year+1
#                 print(nextdate,"-",nextmonth,"-",nextyear)


# date=int(input("enter the date"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# if year>=2000 and year<=2024:
#     if year%4==0:
#         print(year, "leap year")
#     else:
#         print("not leap year")
    
    # if month in (1,3,5,7,8,10,12):
        
    
                
    

# i=1
# while i<=4:
#     print(i)
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1


# *
# 12
# **
# 234
# ***
# 4567
# ****
# 7891011








# i=1
# while i<=10:
#     print(i,end=" ")
#     i=i+1

# a={'x':'19','y':{'z':'25','d':'60'}}
# for i in a:
#     for j in a[i]:
#         if a[i] in dict:


a=8
b=7
c=10
# print(a>b and b<a or c>a and a>c)


print(a>b or b<a)