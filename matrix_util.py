import numpy as numpy 
import re

"""
This file contains the methods necessary to building the transitional probability matrix
used by the MCMC algorithm to calculate the likelihood of a guess

"""
	
def computeMatrix(fileName):
    """
    This method reads the given file and builds a matrix of transitional probabilities from it. A first
    order transition probability is the likelihood that one letter will lead to the next.

    """
    text = open(fileName, errors='ignore').read().lower()

    accepted_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = ''.join([i for i in text if i in accepted_alphabet])

    # this is the alphabet (set of all characters)
    alphabet = list(set(text))

    # initialize matrix using laplace smoothing (needed to avoid probabilities of zero)
    probability_matrix = numpy.zeros((len(alphabet), len(alphabet)))

    for i in range(len(text) - 1):
    	c1 = text[i]
    	c2 = text[i + 1]
    	i1 = alphabet.index(c1)
    	i2 = alphabet.index(c2)
    	probability_matrix[i1, i2] += 1

    probability_matrix /= numpy.sum(probability_matrix)

    # make sure that no probability is zero
    probability_matrix += 1
    
    return probability_matrix, alphabet



# computeMatrix('WarAndPeace.txt')