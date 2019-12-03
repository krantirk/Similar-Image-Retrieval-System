import glob
import os
import fnmatch


#rename files in order1 to n
os.chdir(r"C:/ml/Monumark/dataset")
for index, oldfile in enumerate(glob.glob("*.png")):
    newfile = '{}.png'.format(index+1)
    os.rename (oldfile,newfile)


# to count the number of images indexed type 
# $find /v /c "&*fake&*" index.csv