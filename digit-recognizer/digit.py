import sys
import csv
import numpy

def loadTrainData() :
	l = []
	with open('train.csv') as file :
		lines = csv.reader(file)
		for line in lines :
			l.append(line)
	l.remove(l[0])
	l = array(l)
	label = l[:, 0]
	data = l[:, 1:]
	return nomalizing(toInt(data)), toInt(label)

def toInt(array) :
	array = mat(array)
	m, n = shape(array)
	newArray = zeros((m, n))
	for i in xrange(m) :
		for j in xrange(n) :
			newArray[i, j] = int(array[i, j])
	return newArray

def nomalizing(array) :
	m, n = shape(array)
	for i in xrange(m) :
		for j in xrange(n) :
			if array[i, j] != 0 :
				array[i, j] = 1
	return array

def loadTestData() :
	l = []
	with open('test.csv') as file :
		lines = csv.reader(file)
		for line in lines :
			l.append(line)
	l.remove(l[0])
	data = array(l)
	return nomalizing(toInt(data))


def loadTestResult() :
	l = []
	with open('knn_benchmark.csv') as file :
		lines = csv.reader(file)
		for line in lines :
			l.append(line)
	l.remove(l[0])
	label = array(l)
	return toInt(label[:, 1])

def classify(inX, dataSet, labels, k) :
	inX = mat(inX)
	oo

def saveResult(result) :
	with open('result.csv', 'wb') as myFile :
		myWriter = csv.writer(myFile)
		for i in result :
			tmp = []
			tmp.append(i)
			myWriter.writerow(tmp)
