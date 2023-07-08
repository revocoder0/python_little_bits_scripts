import os
print("**************************************")
print("**********Hello Friend ***************")
print("**************************************")

if(os.system=="windows"):
    os.system("shudown -P")
elif(os.system=="linux"):
    os.system("init 0")
elif(os.system=="mac"):
    os.system("init 0")
else:
    os.system("shutdown -P")