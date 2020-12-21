from matrix_util import *
from decoder_util import *
import random

"""
This file contains the method that runs the MCMC decoding process.

"""


def decode(fileName, accepted_likelihood, iterations):
	"""
	This method decodes a given file under the name fileName using the MCMC algorithm detailed in my paper. The MCMC
	runs until the guess's likelihood is greater than the accepted likelihood.

	"""

	# use this matrix to compute the likelihood of a guess
	english_matrix, alphabet = computeMatrix('WarAndPeace.txt')

	# this is message to be decoded!!!
	secret_message = open(fileName, errors='ignore').read()

	# initialize first STATE (randomize alphabet)
	# a state is the proposed cipheralphabet
	state = alphabet[:]
	random.shuffle(state)

	# decode message
	guess = decodeMessageWithCipher(secret_message, state)

	# calculate likelihood using probability matrix
	l = likelihood(guess, english_matrix, alphabet)

	i = 0
	# begin loop
	while (l < accepted_likelihood and i < iterations):
		i += 1
 		# make random change to STATE to make STATE'
		# do this making random switch of values
		new_state = switchCharacters(state)
	 	# print('new state: ' + str(new_state))

	 	# decode message using STATE'
		new_guess = decodeMessageWithCipher(secret_message, new_state)
	 	# compute likelihood of new guess (l')
		new_likelihood = likelihood(new_guess, english_matrix, alphabet)

		coinFlip = random.random()
	 	# if l' is greater than l, set STATE' to current state
		if (new_likelihood > l):
			state = new_state
			l = new_likelihood
			guess = new_guess
		else:
			# if the new guess was not the 
			if (coinFlip < 0.01):
				state = new_state
				l = new_likelihood
				guess = new_guess
	 	
	
	return guess, likelihood, i

