# N-Gram-Project
n-gram predict project.

# CSE4095S23_Grp10

N-Gram Model

This is a Python implementation of an N-Gram Model, which is a statistical language model based on the probability distribution of sequences of words in a text. This model can be used to calculate the likelihood of a given sentence or to generate new sentences based on the probability distribution of word sequences.

Usage


To use the N-Gram model, you will need to have Python 3 installed along with the nltk package.

Clone the repository or download the code as a ZIP file and extract it to a directory of your choice.
Open a terminal or command prompt in the directory where you extracted the code.
Install the required dependencies by running pip install -r requirements.txt in the terminal or command prompt.
Run the ngram.py file by running python ngram.py in the terminal or command prompt.
You will then be prompted to enter the value of n for the N-Gram model and whether you want to use character-level or word-level N-Grams. Next, the program will read in a text file named processed_ictihats.txt, tokenize the text into N-Grams, and calculate their probabilities.

After the model has been trained, you will be prompted to enter a sentence for which you want to calculate the likelihood or generate new sentences. The program will output the probability of the input sentence and a list of predicted next words for each N-Gram in the sentence.

Implementation Details


The NGramModel class in ngram.py is responsible for training the N-Gram model and calculating probabilities. The constructor of this class takes two arguments: n, the value of n for the N-Gram model, and model_type, which can be set to either "word" or "char" to indicate whether you want to use word-level or character-level N-Grams.

The train method of the NGramModel class is responsible for training the model. It takes a string text as input, tokenizes the text into N-Grams, and calculates their probabilities. The _tokenize method is used to tokenize the input text based on the value of model_type.

The prob method of the NGramModel class is responsible for calculating the probability of a given word given a context. It takes two arguments: word, the word for which to calculate the probability, and context, a tuple representing the context in which the word occurs. This method returns the probability of the word given the context.

The score method of the NGramModel class is responsible for calculating the log probability of a given sentence. It takes a string sentence as input, tokenizes the sentence into N-Grams, and calculates the log probability of each N-Gram using the prob method. It then returns the sum of the log probabilities divided by the length of the tokenized sentence.

The perplexity method of the NGramModel class is responsible for calculating the perplexity of a given text. It takes a string text as input, tokenizes the text into N-Grams, and calculates the log probability of each N-Gram using the prob method. It then returns the perplexity of the text.

The predict dictionary is used to store the predicted next words for each N-Gram in the input sentence. This dictionary is updated as the score method is called for each N-Gram in the sentence. The predicted next word is the word with the highest probability given the N-Gram context.



**Screenshots of output:**

Trigram for word
![image](https://github.com/hakansndkc5/N-Gram-Project/assets/93510323/5cb65b87-2e6d-4545-bc6b-efe8ef99cd11)


Bigram for word
![image](https://github.com/hakansndkc5/N-Gram-Project/assets/93510323/9373dbd3-8fcb-442d-ae2d-96afb0c1008d)




