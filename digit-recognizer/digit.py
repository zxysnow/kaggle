import sys
import csv
from numpy import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn import decomposition

def loadTrainData(file_name) :
	l = []
	header = False
	with open(file_name) as file :
		lines = csv.reader(file)
		for line in lines :
			if header == False :
				header = True
				continue
			l.append([int(i) for i in line])
	l = array(l)
	train = l[:, 1:]
	label = l[:, 0]
	return normalizatio(train), label.tolist()

def toInt(array) :
	array = mat(array)
	m, n = shape(array)
	newArray = zeros((m, n))
	for i in xrange(m) :
		for j in xrange(n) :
			newArray[i, j] = int(array[i, j])
	return newArray

def normalization(array) :
#	return array
	m, n = shape(array)
	for i in xrange(m) :
		for j in xrange(n) :
			if array[i, j] != 0 :
				array[i, j] = 1
	return array

def loadTestData(file_name) :
	l = []
	with open(file_name) as file :
		lines = csv.reader(file)
		for line in lines :
			l.append(line)
	l.remove(l[0])
	data = array(l)
	return normalization(toInt(data))

def loadTestResult(file_name) :
	l = []
	header = False
	with open(file_name) as file :
		lines = csv.reader(file)
		for line in lines :
			if header == False :
				header = True
				continue
			l.append(int(line[1]))
	return l 

def compare(Y1, Y2) :
	print 'compare ...'
	wrong_cnt = 0
	for i in range(0, len(Y1)) :
		if Y1[i] != Y2[i] :
			wrong_cnt += 1
	print 'wrong rate : '
	return wrong_cnt * 1.0 / len(Y1)

def classify(train_data, labels, test_data) :
	train_data = mat(train_data)
	pca = decomposition.PCA(n_components = 100).fit(train_data)
#train_reduced = train_data
	train_reduced = pca.transform(train_data)
	print "knn--------------------------------"
	knn = KNeighborsClassifier(n_neighbors = 10, algorithm = "kd_tree")
	print "knn training..."
	knn.fit(train_reduced, labels)
	print 'knn predicting...'
	test_reduced = test_data
	test_reduced = pca.transform(test_data)
	predictions = knn.predict(test_reduced);
	print 'knn done---------------------------'
	return predictions

def saveResult(result) :
	with open('result.csv', 'wb') as myFile :
		myWriter = csv.writer(myFile)
		ind = 1
		for i in result :
			data = [ind, i]
			myWriter.writerow(data)
			ind += 1

def main() :
	print 'load train data...'
	train_data, labels = loadTrainData('train.csv.bak')
	print 'load test data...'
	test_data = loadTestData('test.csv.bak')
	predictions = classify(train_data, labels, test_data)
	saveResult(predictions)
	test_labels = loadTestResult('knn_benchmark.csv.bak')
	wrong_rate_knn = compare(test_labels, predictions)
	print wrong_rate_knn


if __name__ == '__main__' :
	main()
	
