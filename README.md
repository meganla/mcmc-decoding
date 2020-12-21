# Markov Chain Monte Carlo Algorithms and Decryption

## Project Description
Application that decodes files encrypted with a simple substitution cipher using Markov chain Monte Carlo algorithms. 

## How do I run it?
In terminal, run 
```main.py ``` 
to run the application with the default encoded message, iterations, and accepted likelihood. If you would like to experiment with your own values, run 
```main.py -i DESIRED ITERATIONS -l  DESIRED LIKELIHOOD -f DESIRED FILE NAME```

## What do those parameters do?
The iterations value will indicate the number of iterations the MCMC algorithm should run. The more iterations, the more likely you'll achieve a message that reaches the given accepted likelihood. The default is 10,000. The accepted likelihood value shows how readable the returned message should be. The default is 4. The program will run MCMC for the desired amount of iterations until it achieves a guess of the accepted likelihood or higher. If you have a secret message you'd like to reveal, specify it with the -f parameter.  
