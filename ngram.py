import nltk
import math
import time

predict = {}

class NGramModel:
    def __init__(self, n, model_type="word"):
        self.n = n
        self.counts = {}
        self.total_count = 0
        self.model_type = model_type

    def _tokenize(self, text):
        if self.model_type == "word":
            sents = nltk.sent_tokenize(text)
            return [nltk.word_tokenize(sent.lower()) for sent in sents]
        elif self.model_type == "char":
            return [list(sentence.lower()) for sentence in text.split('\n') if sentence]

    def train(self, text):
        tokenized_sents = self._tokenize(text)

        for sentence in tokenized_sents:
            for i in range(len(sentence) - self.n + 1):
                ngram = tuple(sentence[i:i + self.n])
                if ngram in self.counts:
                    self.counts[ngram] += 1
                else:
                    self.counts[ngram] = 1
                self.total_count += 1

   # def prob(self, word, context):
   #    ngram = context + (word,)
   #    if ngram in self.counts:
   #        return self.counts[ngram] / self.counts.get(context, self.total_count)
   #    else:
   #        return 1 / (self.counts.get(context, self.total_count) + len(self.counts))

    def prob(self, word, context):
        # Combine the context and word into an n-gram
        ngram = context + (word,)

        # If the n-gram exists in the counts dictionary, return its probability
        if ngram in self.counts:
            # Probability of the n-gram is the count of the n-gram divided by the count of the context
            # Count ngram
            ngramCount = self.counts[ngram]

            # Count totalCount
            totalCount = sum([self.counts[key] for key in self.counts.keys() if key[:-1] == context])

            return ngramCount / totalCount
        else:
            # If the n-gram does not exist in the counts dictionary, return the default probability
            # Default probability is the inverse of the count of the context plus the size of the counts dictionary
            # This ensures that unseen n-grams are given a non-zero probability
            return 1 / (self.counts.get(context, self.total_count) + len(self.counts))

    def score(self, sentence):
        global predict
        if self.model_type == "word":
            tokenized_sent = nltk.word_tokenize(sentence.lower())
        else:
            tokenized_sent = list(sentence.lower())

        log_prob = 0
        for i in range(self.n - 1, len(tokenized_sent)):
            context = tuple(tokenized_sent[i - self.n + 1:i])
            word = tokenized_sent[i]
            log_prob += math.log(self.prob(word, context), 2)

            #print(f"Probability of '{word}' given context {context}: {self.prob(word, context)}")
            if (len(predict) == 0):
                predict[context] = {"prob": self.prob(word, context), "predicted_words": word}
            elif context not in predict.keys():
                # Update the dictionary with the new key-value pair
                predict[context] = {"prob": self.prob(word, context), "predicted_words": word}
            elif (predict[context]["predicted_words"] != word):
                if predict[context]["prob"] < self.prob(word, context):
                    predict[context] = {"prob": self.prob(word, context), "predicted_words": word}
            else:
                pass

        return log_prob / len(tokenized_sent)

    def perplexity(self, text):
        tokenized_sents = self._tokenize(text)
        log_prob_sum = 0
        word_count = 0
        for sentence in tokenized_sents:
            for i in range(self.n - 1, len(sentence)):
                context = tuple(sentence[i - self.n + 1:i])
                word = sentence[i]
                log_prob_sum += math.log(self.prob(word, context), 2)
                word_count += 1

        entropy = -log_prob_sum / word_count
        perplexity = (-1 / word_count) * log_prob_sum
        return perplexity


# Example usage
input_n = input("Enter n: ")
n=int(input_n)

charorword=input("char or word search: ")

print("Processing \n", end="", flush=True)
time.sleep(5)



with open("processed_ictihats.txt", "r", encoding="utf-8") as f:
    text = f.read()

model = NGramModel(n, model_type=str(charorword))  # Change model_type to "word" for word-level n-grams
model.train(text)

with open("test.txt", "r", encoding="utf-8") as w:
    text2 = w.read()
test_text = text2

score = model.score(test_text)
perplexity = model.perplexity(test_text)

print("\b" * len("Processing"), end="", flush=True)
print(f"Score: {score}")
print(f"Perplexity: {perplexity}")


input_string = input("Enter a predict word: ")
words = input_string.split()
key = tuple(words)

if(charorword=="char"):
    print("Predicted next char is " + ''.join((predict[(key)]['predicted_words'])))

else:
    print("Predicted next word is " + ''.join((predict[(key)]['predicted_words'])))




