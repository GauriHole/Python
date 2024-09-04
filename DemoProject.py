# Program For Demo Project Of My Business...
import sys
print("--------------- Welcome To Desirable Desing & Development (#3D) ----------------\n")
userwarn='Uppsss , Incorrect Username Try Again .... '
psdwarn='Uppsss , Wrong Password Try Again .... '
input_info=input(" Create New Account ....\n Enter Your Username :  Enter Your Email :  Enter Your Mobile :  Enter Your Password : \n                     NOTE : Put Your Above Info Using Space ... \n ")

for i in range(0,len(input_info)):
    User_info=input_info.split()
print('List : ',User_info)

print("\n --------------------------- Account Created Successfully ----------------------------","\n\n                           Welcome User                ")

yes=input("\n Do You Have An Account ? ")

if(yes =='yes'):
    name=input(" Enter Your Username : ")
    psd=input(" Enter Your Password : ")
    if(User_info[0]==name and User_info[3]==psd):
        print("\n --------------------------- Login Successfull ----------------------------")
    elif(User_info[0]!=name):
        print("    ",userwarn)
        name=input(" Enter Your Username : ")
        if(User_info[0]==name):
            print("\n --------------------------- Login Successfull ----------------------------")
        else:
            print("\n --------------------------- Login Unsuccessfull ----------------------------")
    elif(User_info[3]!=psd):
        print("   ",psdwarn)
        psd=input(" Enter Your Password : ")
        if(User_info[3]==psd):
            print("\n --------------------------- Login Successfull ----------------------------")
        else:
            print("\n --------------------------- Login Unsuccessfull ----------------------------")
    else:
        print("                         Don't  Have an Account ? \n                                               Create New Account ")
        name=input("                    Enter Your Username : ")
        email=input("                   Enter Your Email : ")
        mobile=input("                  Enter Your Mobile : ")
        password=input("                Enter Your Password : ")
        print("\n --------------------------- Account Created Successfully ----------------------------","\n                           Welcome User                ")
    choice=input("\n             What Do You Want ? \n 1.Video Editing \n 2.Web Development \n 3.Collage Making  \n 4.Visiting Card Making \n")
    if (choice=='1'):
        print(" Video Editing ")
    elif (choice=='2'):
        print(" Web Development ")
        input("\n  Which Type of Site You Want ? \n 1. Simple Site \n 2. Ecommerce Site \n 3. Company Site( Business Site ) \n 4. Education Site \n ")
        if(choice=='1'):
            print("     Simple Site  \n  Involvement :  Pages - Min (5), Max (7) / Video - Introductory 1 (if required) / Photo - According Need / Slider - (if Required) \n  Rate :  3000/- ")
        elif(choice=='2'):
            print("     Eccommerce Site  \n  Involvement :  Pages - Min (5), Max (25) / Slider 1 + Other (if Required) / Photo - According Need  \n  Rate :  3000/- ")
        elif(choice=='3'):
            print("     Company (Business) Site  \n  Involvement :  Pages - Min (5), Max (15) /  Member Board / Video - Introductory 1 + Other (if required) / Photo - According Need / Slider - (if Required) \n  Rate :  3000/- ")
        elif(choice=='4'):
            print("     Education Site  \n  Involvement :  Pages - Min (5), Max (20) / Video - Introductory 1  + Other(if required) / School Member Board  / Photo - According Need / Slider - (if Required) \n  Rate :  3000/- ")
        else:
            print("   Sorry , We Don't Having Same Choice ..... ")
    elif (choice=='3'):
        print(" Collage Making ")
    elif (choice=='4'):
        print(" Visiting Card Making ")
    else:
        print(" Sorry , We Don't Have the Similar Option !!! ")

