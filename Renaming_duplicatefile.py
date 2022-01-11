#Renaming a file if the filename already exists



import uuid
import os 
from os import getuid, path 
import shutil

path1 = 'a' #Specify the path of first file
path2 = 'b' #Specify the path of other file

    
for anno in os.listdir(path1):
   for anno2 in os.listdir(path2):
        if anno == anno2 :
            
            # filename = anno.split('.pdf')
            # imagename = filename[0] + '.png'
            new_filename = str(uuid.uuid4())
            # # new_filename = new_filename + '.json'
            # # print(new_filename)
            anno_path = os.path.join(path1,anno)
            # imagepath1 = os.path.join(path3,imagename)
            # imagepath2 = os.path.join(path4,imagename)
            
            src_path1 = os.path.join(path1,new_filename )           #Specify the files that you want to rename
            src_path2 = os.path.join(path2,new_filename + '.png')   #Specify the files that you want to rename with same id
            # srcpath3 = os.path.join(path4,new_filename + '.png')
            
            os.rename(anno_path,src_path1)
            os.rename(os.path.join(path2,anno),src_path2)
            # os.rename(imagepath2,srcpath3)
            



    