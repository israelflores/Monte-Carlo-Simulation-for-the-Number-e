"""
@author: Israel Flores

This program estimates the number e with a random binary matrix. This program is free software. 
"""

import numpy as np
import matplotlib.pyplot as plt   

class RandomBinaryMatrix(object):
    
    def __init__(self, n):           
        self.n = n
        self.length = 2**(n+1)#side length of square matrix   
        self.matrix = np.random.randint(2, size=(self.length, self.length))
        self.totalTrials = 2**(n+3)# (rows + columns)*2     
        
    def plotResult(self):
        #declare x-axis for graph
        self.trialsVector = np.linspace(1, self.totalTrials, self.totalTrials) 
        #plot the real value of e as a horizontal line                     
        plt.plot([0, self.totalTrials],[np.e, np.e],'m',ls='dashed',label=('Real value of e = 2.71828...')) 
        #plot trials/(trials - hits)
        plt.plot(self.trialsVector, self.getResultsVector(), label='Estimation of e')        
        plt.title(self.getTitleForGraph())
        plt.xlabel("Trials\n(i.e. rows and columns observed)")
        plt.ylabel("Trials/(Trials - Hits)")
        plt.legend()
        plt.show()
        print("Final result is e ~ " + self.getFinalEstimation(8) + " (see graph)\n")
        
    #this method returns the ratio trials/(trials - hits) at each step (i.e. at each trial number)         
    def getResultsVector(self):
        self.hitsVector = np.empty(self.totalTrials)#keeps track of the "hits" in vector format
        self.trialsCount = 0
        self.hitsCount = 0 
        self.searchMatrix(1)#find clusters of ones
        self.searchMatrix(0)#find clusters of zeros        
        return self.trialsVector/(self.trialsVector - self.hitsVector)        
        
    def searchMatrix(self, binaryDigit):#binaryDigit must be a one or a zero
        #search rows    
        for row in range(0, self.length):
            clusterSize = 0
            for nextDigit in self.matrix[row, 0:self.length]:
                if nextDigit == binaryDigit:
                    clusterSize += 1
                    if clusterSize >= self.n:#true when a cluster is found
                        self.hitsCount += 1
                        break#no need to continue checking the same row when a cluster is found
                else: clusterSize = 0 
            #update data:
            self.hitsVector[self.trialsCount] = self.hitsCount
            self.trialsCount += 1   
        #search columns        
        for column in range(0, self.length):
            clusterSize = 0
            for nextDigit in self.matrix[0:self.length, column]:
                if nextDigit == binaryDigit:
                    clusterSize += 1
                    if clusterSize >= self.n:#true when a cluster is found
                        self.hitsCount += 1
                        break#no need to continue checking the same column when a cluster is found
                else: clusterSize = 0 
            #update data:
            self.hitsVector[self.trialsCount] = self.hitsCount
            self.trialsCount += 1       
        
    def getTitleForGraph(self):
        firstTitleLine = 'Experimental Estimation of e with a Random Binary ' + str(self.length) + \
        ' X ' +str(self.length) + ' Matrix' + ' (n = ' + str(self.n) + ')\n\n' 
        secondTitleLine = '(final estimation:  e ~ ' + self.getFinalEstimation() + ')'
        return firstTitleLine + secondTitleLine
    
    def getFinalEstimation(self, decimals=5):
        return str(format(self.totalTrials/(self.totalTrials - self.hitsCount), '.' + str(decimals) + 'f'))
# instantiate and plot with n = 10:       
m = RandomBinaryMatrix(10)
m.plotResult() 