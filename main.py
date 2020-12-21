from optparse import OptionParser
from decoder import *
import sys

"""
Markov Chain Monte Carlo Algorithms and Decryption

"""

def main(argv):
   parser = OptionParser()
   parser.add_option("-f", "--filename", dest="filename", 
                     help="the secret message to be decoded", default="SecretMessage.txt")

   parser.add_option("-i", "--iterations", dest="iterations",  type="int", 
                     help="the number of iterations to run MCMC for- the more iterations the more likely you'll get a readable guess", default=100000)

   parser.add_option("-l", "--acceptedlikelihood", dest="acceptedlikelihood", type="float",
                     help="the desired likelihood that the guess is English- start low and build up", default=4.0)
   
   (options, args) = parser.parse_args(argv)

   secret_message = options.filename
   iterations = options.iterations
   accepted_likelihood = options.acceptedlikelihood

   guess, guess_likelihood, guess_iterations = decode(secret_message, accepted_likelihood, iterations)

   print('after ' + str(iterations) + ' and an accepted likelihood of ' + str(accepted_likelihood))
   if (guess_iterations < iterations):
      print('the final guess is: ' + guess + ' achieved at iteration ' + str(guess_iterations))
   else:
      print('no guess of that likelihood was achieved in that number of iterations. the final guess is: ' + guess)
   
if __name__ == "__main__":
   main(sys.argv)