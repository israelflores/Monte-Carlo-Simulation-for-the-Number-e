"""
@author: Israel Flores
This program estimates the number e with a random binary matrix. This program is free software. 
"""
import numpy as np
import matplotlib.pyplot as plt   

class RandomBinaryMatrix(object):
    
    def __init__(self, n):           
        self.n = n# n also automatically defines the cluster size
        self.length = 2**(n+1)#side length of the square matrix  
        #randomly build the matrix we intend to search for non-clustered rows and columns:
        self.matrix = np.random.randint(2, size=(self.length, self.length))
        self.totalTrials = 2**(n+3)#  = 2*(rows+columns)    
        
    def plotResult(self):
        #declare x-axis for graph
        self.trialsVector = np.linspace(1, self.totalTrials, self.totalTrials) 
        #plot the real value of e as a dashed horizontal line                     
        plt.plot([0, self.totalTrials],[np.e, np.e],'m',ls='dashed',label=('Real value of e = 2.71828...'))         
        plt.plot(self.trialsVector, self.getRatioVector(), label='Estimation of e')#plots trials/clusterMisses     
        plt.title(self.getTitleForGraph())
        plt.xlabel("Trials\n(i.e. rows and columns observed)")
        plt.ylabel("Trials/ClusterMisses")
        plt.legend()
        plt.show()
        print("Final result is e ~ " + self.getFinalEstimation(8) + " (see graph)\n")
        
    #i.e. returns the ratio trials/clusterMisses at every stage of the search     
    def getRatioVector(self):
        #declare an array that stores the cluster-miss count with the trial number  as its index
        self.missesVector = np.empty(self.totalTrials)
        self.trialsCount = 0
        self.clusterMisses = 0 #counter for both 1-cluster-misses and 0-cluster-misses
        self.searchMatrix(1)#find 1-cluter-misses in rows and columns
        self.searchMatrix(0)#find 0-cluter-misses in rows and columns
        return self.trialsVector/self.missesVector       
        
    def searchMatrix(self, binaryDigit):#binaryDigit must be a one or a zero (the cluster-type)
        #search all of the rows    
        for row in range(0, self.length):
            self.clusterMisses += 1#assume the row we're about to observe has no cluster
            streak = 0 #keeps track of the current number of consecutive binaryDigits 
            for nextDigit in self.matrix[row, 0:self.length]:
                if nextDigit == binaryDigit:
                    streak += 1
                    if streak >= self.n:#true when a cluster is found
                        self.clusterMisses -= 1#make up for assuming it had no cluster
                        break#no need to continue checking the same row when a cluster is found
                else: streak = 0 
            #update data:
            self.missesVector[self.trialsCount] = self.clusterMisses
            self.trialsCount += 1   
        #search all of the columns        
        for column in range(0, self.length):
            self.clusterMisses += 1#assume the colunm we're about to observe has no cluster
            streak = 0 #keeps track of the current number of consecutive binaryDigits 
            for nextDigit in self.matrix[0:self.length, column]:                
                if nextDigit == binaryDigit:
                    streak += 1
                    if streak >= self.n:#true when a cluster is found
                        self.clusterMisses -= 1#make up for assuming it had no cluster
                        break#no need to continue checking the same column when a cluster is found
                else: streak = 0 
            #update data:
            self.missesVector[self.trialsCount] = self.clusterMisses
            self.trialsCount += 1       
        
    def getTitleForGraph(self):
        firstTitleLine = 'Experimental Estimation of e with a Random Binary ' + str(self.length) + \
        ' X ' +str(self.length) + ' Matrix' + ' (n = ' + str(self.n) + ')\n\n' 
        secondTitleLine = '(final estimation:  e ~ ' + self.getFinalEstimation() + ')'
        return firstTitleLine + secondTitleLine
    
    def getFinalEstimation(self, decimals=5):
        return str(format(self.totalTrials/self.clusterMisses, '.' + str(decimals) + 'f'))
# instantiate and plot with n = 10:       
m = RandomBinaryMatrix(10)
m.plotResult() 
