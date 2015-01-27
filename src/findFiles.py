import os
import sys

def listFileExt(directory, search):
    fileList=[]
    for path,folders,files in os.walk(directory):
        for folder in folders:
            if folder == search:
                print "%s/%s"%(path,folder)


if __name__ == "__main__":
    if len(sys.argv)!=3:
        print "arguments error."
        sys.exit(1)

    listFileExt(sys.argv[1], sys.argv[2])
        
