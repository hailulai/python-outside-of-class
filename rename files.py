## Rename files

import os
def renameFiles():
    fileList = os.listdir(r"/Users/hailulai/Desktop/gary's cal 2 notes")
##    print (fileList)
    savedPath = os.getcwd()
    print("Current Working Directory is" + savedPath)
    os.chdir(r"/Users/hailulai/Desktop/gary's cal 2 notes")

    for file_name in fileList:
        os.rename(file_name, file_name.translate(None, "0123456789"))

renameFiles()
