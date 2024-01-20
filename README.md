# N-Gram-Project
n-gram predict project.

Introduction
The goal of our project was to create word-based and character-based n-gram language
models on our dataset and use these models to calculate the probability of sentences,
paragraphs, or documents, and to use them for spell checking. In this report, we will describe
our approach, the methods and libraries we used, and the results we obtained on our own
dataset.
The spell checking application can be used to improve the quality of written content, such as
in the case of legal documents, academic papers, or any other text-heavy material. By
implementing these language models, we can accurately predict the likelihood of words and
phrases in a given context, thereby providing suggestions for the correct spelling of words or
phrases that are not recognized by the model. Additionally, this approach can be extended to
other natural language processing tasks, such as machine translation or sentiment analysis.
Overall, this project has demonstrated the effectiveness of using n-gram language models for
spell checking and other natural language processing tasks. By continuing to improve these
models and expand their applications, we can continue to improve the quality of written
communication in various domains.
Datasets
The dataset used in the project contains 8617 JSON files, which approximately consist of
596.125 words in total. We used around 80% of these files to train our model, and the
remaining portion was used to test our model's performance. This dataset contains data used
in the field of law.
Our approach
In our project, we created language models using the Python programming language. First,
we subjected our dataset to preprocessing steps, which included text cleaning, removal of
punctuation marks, converting to lowercase/uppercase, and removing unnecessary words
such as stop-words. Then, we created word-based and character-based n-gram language
models.
For the word-based n-gram model, we split the words in our dataset into n-grams and
calculated the probability of each n-gram. Then, we used these n-gram probabilities to
calculate the perplexity value in order to determine the probability of a sentence, paragraph,
or document. The perplexity value measures how well the language model predicts the next
word in a sequence based on the context of the previous words. A lower perplexity value
indicates better predictive performance.
For the character-based n-gram model, we split the words in our dataset into individual
characters and calculated the probability of each character. Then, we used these character
probabilities to calculate the perplexity value in order to determine the probability of a word
or short phrase. This model is particularly useful in situations where the words are misspelled
or the dataset contains a lot of noise, as it can still accurately predict the next character in the
sequence based on the context of the previous characters. However, the downside of this
model is that it requires a larger amount of training data and can be computationally
expensive.
Methods and Libraries Used
Libraries and tools:
● Python programming language was used.
● String manipulation and list operations were used for data preprocessing steps.
● nltk (Natural Language Toolkit) library was used to create language models.
● Numpy libraries were used for dataset processing operations.
Methods:
● _tokenize(self, text): Tokenizes the input text based on the value of model_type. If
model_type is "word", it tokenizes the text into sentences and then into words. If
model_type is "char", it tokenizes the text into characters.
● train(self, text): Trains the language model on the input text.
● prob(self, word, context): Calculates the probability of the word given the context.
The context is a tuple of tokens that precede the word.
● score(self, sentence): Calculates the log probability of the input sentence.
● perplexity(self, text): Calculates the perplexity of the input text


**Screenshots of output:**

Trigram for word
![image](https://github.com/hakansndkc5/N-Gram-Project/assets/93510323/5cb65b87-2e6d-4545-bc6b-efe8ef99cd11)


Bigram for word
![image](https://github.com/hakansndkc5/N-Gram-Project/assets/93510323/9373dbd3-8fcb-442d-ae2d-96afb0c1008d)




