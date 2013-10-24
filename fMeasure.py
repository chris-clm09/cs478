
import sys

def odd(num):
	return num & 1

#########################################################

#########################################################
def parseAssignmentFile(assignFileName):
	f = open(assignFileName, 'r')

	assignments = []

	cnt = 1
	for line in f:
		if not odd(cnt):
			s = line.split()
			
			for a in s:
				assignments.append(a)

		cnt += 1 

	return assignments

#########################################################
#150          5.9         3.0          5.1         1.8  virginica
#########################################################
def parseDataFile(dataFileName):
	f = open(dataFileName, 'r')
	classN = 0
	d = {}
	answers = []

	for line in f:
		s = line.split()
		if not d.has_key(s[5]):
			classN += 1
			d[s[5]] = 1
		answers.append(classN)

	return answers

def cluster(assignments):
	clusters = []
	d = {}
	i = -1
	cnt = 0

	for a in assignments:
		if not d.has_key(a):
			i += 1
			d[a] = i
			clusters.append([])
		clusters[d[a]].append(cnt)
		cnt += 1

	return clusters

def majorityForCluster(clusters, answers):
	counts     = []
	majorities = []

	for c in range(0, len(clusters)):
		curCluster = clusters[c]
		counts.append({})

		for v in curCluster:
			if not counts[c].has_key(answers[v]):
				counts[c][answers[v]] = 0	

			counts[c][answers[v]] = counts[c][answers[v]] + 1
	
	for c in counts:
		majority = 0
		amax      = 0
		for key in c.keys():
			if (amax < c[key]):
				amax = c[key]
				majority = key
		majorities.append(majority)

	return majorities

def genSuggested(clusters, majorities, size):
	suggested = []
	for i in range(0, size):
		suggested.append(0)

	for c in range(0, len(clusters)):
		cluster = clusters[c]
		major  = majorities[c]

		for v in cluster:
			suggested[v] = major

	return suggested

#########################################################

#########################################################
def calcFMeasure(assignments, answers):
	clusters   = cluster(assignments)
	majorities = majorityForCluster(clusters, answers)
	suggested  = genSuggested(clusters, majorities, len(answers))

	

	return 1

#########################################################

#########################################################
if __name__ == "__main__":
   execName, assignFileName, dataFileName = sys.argv

   assignments = parseAssignmentFile(assignFileName)
   answers     = parseDataFile(dataFileName)

   print calcFMeasure(assignments, answers)
