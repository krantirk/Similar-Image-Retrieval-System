from Descriptor import Descriptor
import argparse
import cv2
import glob
import os
import fnmatch

#constructing an argument parser
ap=argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="C:\ml\Monumark\dataset")
ap.add_argument("-i","--index", required=True,help="C:\ml\Monumark")
args=vars(ap.parse_args())

#initialising the color descriptor
cd=Descriptor((8,12,3))
output=open(args["index"],"w")



#for each image calculate the features and write in a file 
for imagePath in glob.glob(args["dataset"]+"/*.png"):

	imageID=imagePath[imagePath.rfind("/")+1:]
	print(imageID)
	image=cv2.imread(imagePath)

	features=cd.describe(image)
	features=[str(f) for f in features ]
	output.write("%s,%s\n" % (imageID,",".join(features)))

output.close()

