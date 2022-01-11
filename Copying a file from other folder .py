#Copying a file with same filename but different file type after checking if there is any other file

import os 
from os import path 
import shutil
annota_path = 'FinalJsonfile' #Path 
for anno in os.listdir(annota_path):
    # print(anno)
    filename = anno.split('.json')
    #print(filename)
    imagename = filename[0] + '.png'
    #print(imagename)
    imagepath = os.path.join('Labelfiles/labels/',imagename)
    if path.exists(imagepath):
        shutil.copy(imagepath,'labels')
    