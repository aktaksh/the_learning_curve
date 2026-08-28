def count_words(sentence):
     word_count = {}
     wordsplit = sentence.split()
     for word in wordsplit:
          if word in  word_count:
               word_count[word] += 1
          else:
               word_count[word] = 1
     return word_count

text = "python is fun and python is powerful"

result = count_words(text)
