import random
import numpy

"""
This file contains all the helper methods involved in the decoding process.

"""

def decodeMessageWithCipher(encrypted_text, cipher):
	"""
	This method decodes the given encrypted_text using the given cipher alphabet. Each word is decrypted 
	separately, and spaces are left in tact.
	"""
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	map_of_characters = {alphabet.pop(0):k for k in cipher}
	decrypted_text = ""
	for char in encrypted_text:
		if (char != ' '):
			decrypted_text = decrypted_text + map_of_characters[char]
		else:
			decrypted_text = decrypted_text + " "

	return decrypted_text


def likelihood(message, english_matrix, alphabet):
	"""
	This method calculates the likelihood of a given message. It does this by summing up the likelihood
	of each individual word in the message. The likelihood of a word is the product of its transitional
	probabilities. 

	"""
	likelihood = 1.0
	words = message.split(' ')
	for word in words:
		word_likelihood = 1.0
		for i in range(len(word) - 1):
			c1 = word[i]
			c2 = word[i + 1]
			i1 = alphabet.index(c1)
			i2 = alphabet.index(c2)
			word_likelihood = word_likelihood * english_matrix[i1, i2]
		likelihood = likelihood * word_likelihood

	return likelihood


def switchCharacters(state):
	"""
	This method serves to swap two characters in the given alphabet, labeled 'state'. The returned
	alphabet is the proposed next state of the Markov chain.

	"""
	i1 = random.randint(1, len(state) - 1)
	i2 = random.randint(1, len(state) - 1)

	c1 = state[i1]
	c2 = state[i2]
	
	new_state = state[:]

	new_state[i1] = c2
	new_state[i2] = c1

	return new_state
