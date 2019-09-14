country=input("請輸入國家　:　")
age=int(input("請輸入年齡　： "))
if country=="美國":
    if age>=16:
        print("你可以開車")
    else:
        print("你還不能開車")
     
elif country=="臺灣"：
    if age>=18:
        print("你可以開車")
    else:
        print("你還不能開車")
        
else:
    print("只能輸入　臺灣　和　美國")
     