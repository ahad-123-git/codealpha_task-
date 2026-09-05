import os
import shutil
print("=======================================")
print("         Task Automation Started ......")
print("=======================================")
folder_path=input("Enter source folder path :")
destination_path=os.path.join(folder_path,"jpg folder")
print("Destination folder Created:",destination_path)
os.makedirs(destination_path)
files_list=os.listdir(folder_path)
count=0
print("Moving jpg Files.....")
for i in files_list:
    if(i.endswith(".jpg")  and os.path.isfile(os.path.join(folder_path,i))):
        count=count+1
        files_path=os.path.join(folder_path,i)
        shutil.move(files_path,destination_path)
        print("Moved:",i)
if(count==0):
    print("No .jpg files found in the source folder")
    print("Task completed .")
else:
    print(count,"jpg files moved successfully .")
    print("Task completed successfully !")
    
    
