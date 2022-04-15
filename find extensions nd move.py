import os
import shutil
double_slash='\\'
path1=r"E:\TEST"
path2=r"C:\Users\hp world\Desktop"
# src_path = path1+m+i
# dst_path = path2+m+b+m+i
types_of_files=[]
for root, dirs, files in os.walk("E:\TEST"):
    for i in files:
        types_of_files.append(i)
for i in types_of_files:
    file_name=i.split(".")
    extension=file_name[-1]
    # b='txt'
    if i.endswith(extension):
        path_1=path2+double_slash+extension
        if not (os.path.exists(path_1)):
            directory = (extension)
            parent_dir = r"C:\Users\hp world\Desktop"
            path = os.path.join(parent_dir, directory)
            os.makedirs(path)    
        src_path = path1+double_slash+i
        dst_path = path2+double_slash+extension+double_slash+i
        shutil.move(src_path, dst_path)
        
