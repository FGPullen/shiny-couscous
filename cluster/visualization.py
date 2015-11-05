import numpy as np
from sklearn.manifold import TSNE
from page import Page
from pages import allPages
from sklearn.preprocessing import scale
import matplotlib.pyplot as Plot

class visualizer:
	def __init__(self,pages):
		self.UP_pages = pages
		feature_matrix = []
		for page in self.UP_pages.pages:
			tfidf_vector = []
			for key in page.tfidf:
				#tfidf_vector.append(page.normonehot[key])
				tfidf_vector.append(page.normtfidf[key])
			feature_matrix.append(tfidf_vector)
		X = np.array(feature_matrix)
		# rescale X
		X = scale(X)
		model = TSNE(n_components=2, random_state=0)
		self.Y = model.fit_transform(X)

	def show(self,group_list,file_name):
		cluster_name = ["Others","Users","Questions","Index","Tags","Posts","Feeds"]
		mark_list = ["yd","g+","bo","r*","k^","mH","c_"]
		label_count = [0 for i in range(len(mark_list))]
		x = self.Y[:,0]
		y = self.Y[:,1]
		print "Intotal we have " + str(x.size) + " data points"
		print str(len(group_list)) + "\t" + str(x.size)
		assert len(group_list) == x.size
		for i in range(len(group_list)):
			index = group_list[i]
			mark = mark_list[index]
			Plot.plot(x[i],y[i],mark,label=cluster_name[index] if label_count[index]==0 else "")
			label_count[index] = 1
		Plot.legend(numpoints=1,loc=3);
		#Plot.legend();  
		self.write2D(file_name,group_list)
		Plot.show()
	
	def write2D(self,file_name,group_list):
		write_file = open(file_name,"w")
		x = self.Y[:,0]
		y = self.Y[:,1]		
		assert len(self.UP_pages.pages) == x.size
		for i in range(x.size):
			write_file.write(self.filename2Url(self.UP_pages.pages[i].path)+"\t"+ str(group_list[i]) +"\t"+str(x[i])+"\t"+str(y[i])+"\n")
	
	def filename2Url(self,filename):
		return filename.replace("_","/")


if __name__=='__main__':
	#UP_pages = allPages(["../Crawler/toy_data/users/","../Crawler/toy_data/questions/","../Crawler/toy_data/lists/"])
	#UP_pages = allPages(["../Crawler/crawl_data/Users/","../Crawler/crawl_data/Outlinks_U/","../Crawler/crawl_data/Noise/"])
	UP_pages = allPages(["../Crawler/crawl_data/Questions/"])
	v = visualizer(UP_pages)
	v.show(v.UP_pages.ground_truth,"ground_truth.test")
	'''
	UP_pages = allPages(["../Crawler/crawl_data/Questions/"])
	feature_matrix = []
	for page in UP_pages.pages:
		tfidf_vector = []
		for key in page.tfidf:
			tfidf_vector.append(page.tfidf[key])
		feature_matrix.append(tfidf_vector)
	X = np.array(feature_matrix)
	X = scale(X)
	print len(UP_pages.pages)
	print X.shape
	model = TSNE(n_components=2, random_state=0)
	Y = model.fit_transform(X)

	x = v.Y[:,0]
	y = v.Y[:,1]
	print x.shape
	print y.shape
	Plot.plot(x[0:len(v.UP_pages.pages)],y[0:len(v.UP_pages.pages)], 'r*',label="questions")

	#Plot.plot(x[0:531],y[0:531], 'r*',label="users")
	#Plot.plot(x[531:],y[531:], 'g+',label="questions")

	#print Y[:,0].shape
	#print Y[:,1].shape
	#Plot.plot(Y[:,0],Y[:,1],'bo')
	#print UP_pages.pages[5].path
	#print UP_pages.pages[406].path
	#Plot.plot(x[0:531],y[0:531], 'r*',label="users")
	#Plot.plot(x[5],y[5], 'bo',label="102")
	#Plot.plot(x[406],y[406], 'yd',label="406")
	#Plot.plot(x[531:621],y[531:621], 'g+',label="outlinks")
	#Plot.plot(x[621:],y[621:], 'bo',label="noise")
	Plot.legend(loc=3);
	Plot.show()
'''
