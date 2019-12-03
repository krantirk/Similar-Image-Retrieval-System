from Descriptor import Descriptor
from Searcher import Searcher
import argparse
import cv2
import re


ap=argparse.ArgumentParser()
ap.add_argument("-i","--index",required=True,help="C:\ml\Monumark")
ap.add_argument("-q","--query",required=True,help="C:\ml\Monumark\queries")
ap.add_argument("-r","--result_path",required=True,help="C:\ml\Monumark\Final_Results")
args=vars(ap.parse_args())

cd=Descriptor((8,12,3))
query=cv2.imread(args["query"])
features=cd.describe(query)
results=Searcher(args["index"])
final=results.search(features)

cv2.imshow("Query",query)


for (score,resultID) in final:
	print(score,resultID)
	resultID=resultID.split("\\")[1]
	
	print(score,resultID)

	result=cv2.imread(args["result_path"]+"/"+resultID)
	cv2.imshow("Result",result)
	cv2.waitKey(0)


