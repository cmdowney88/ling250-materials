import sys

from copy import copy

file_to_open = sys.argv[1]

def process_text(filename):
    raw_text = []
    for line in open(filename, 'r', encoding='utf8'):
        raw_text.append(line)
    stripped_text = [line.strip() for line in raw_text]
    tokenized_text = [line.split() for line in stripped_text]
    
    lowercase_text = []
    
    for sentence in tokenized_text:
        lowercase_sentence = []
        for word in sentence:
            lowercase_sentence.append(word.lower())
        lowercase_text.append(lowercase_sentence)
    
    return lowercase_text

def count_words(list_of_sentences):
    word_count = {}
    for sentence in list_of_sentences:
        for word in sentence:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # final step
    return word_count

tokenized_text = process_text(file_to_open)

word_counts = count_words(tokenized_text)

individual_counts = []
for word in word_counts:
    individual_counts.append(word_counts[word])

sum_of_words = sum(individual_counts)

word_frequency = copy(word_counts)
for word in word_frequency:
    word_frequency[word] /= sum_of_words

sorted_word_counts = sorted(
    word_counts.items(), key=lambda item: item[1], reverse=True
)
sorted_word_frequencies = sorted(
    word_frequency.items(), key=lambda item: item[1], reverse=True
)
print(sorted_word_frequencies[:200])
