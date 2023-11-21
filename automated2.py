import os
import shutil

from_dir="C:/Users/Admin/Downloads"
to_dir="C:/Users/Admin/Desktop/C-102 Organized"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
        
    if extension=="":
        continue
    elif extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir + '/' + file_name
        path2=to_dir + '/' + "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("Moving " + file_name)

        else:
            os.makedirs(path2)
            print("Folder(s) Created!!")
            shutil.move(path1,path3)
            print("Moving " + file_name)
            
