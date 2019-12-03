import numpy as np
import csv

class Searcher:
	#store the path of the index file
	def __init__(self,indexPath):
		self.indexPath=indexPath

	
	#search function searches the images similar to the query image 
	#queryFeatures are the features of the query image 
	#limit is the nuber of search results that we want
	#results is the dictionary data structure having key as image id
	#and the value as the similarity parameter	
	def search(self,queryFeatures, limit=10):
		#store the results in a dictionary
		results={}
		#open the file to load the features 
		with open(self.indexPath) as f:
			reader=csv.reader(f)

			for row in reader:

				features=[float(x) for x in row[1:]]
				d=self.chi_squared_distance(features,queryFeatures)
				results[row[0]]=d

			f.close()
		#sort the results
		results=sorted([(v,k) for (k,v) in results.items()])

		return results[:limit]

	def chi_squared_distance(self,histA,histB,eps=1e-10):

		d=0.5* np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA,histB)])
		return d


#chi squared distance is based on the pearson formula for statistics used to compare the probability distributions
#eps is used to avoid division by zero while computing for 2 histogram distributions
#it is used for confidance interval or determining the goodness of fit 
#it has a parameter k used to highlight the number of squared terms 
#it is sum of squared terms of a distribution
#chi_squared_distance= sum of square of independent features




