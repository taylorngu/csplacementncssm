from string import ascii_lowercase, punctuation
from collections import Counter
import re

#1

def split_count():

    file = open("loremipsum.txt")
    sent_arr = filter(None, re.split(r'(?<=\.) ', file.read().replace('\n', ' ')))

    count = 1
    for sentence in sent_arr:
        
        count = len(sentence.split());
    
        print('"{0}" contains {1} words'.format(sentence.lstrip(), str(count)))


#2

def avg_pos():

    file = open("loremipsum.txt")
    sent_arr = re.split(r'(?<=\.) ', file.read().lower().replace('\n', ' '))

    for char in ascii_lowercase:

        occur = 0
        pos = 0
        av_pos = 0
        
        for sentence in sent_arr:
            
            if sentence.find(char) != -1:
                
                occur += 1
                pos += sentence.find(char)

        if occur != 0:
            
            av_pos = pos/occur
            print('"{0}" was found at position {1}.'.format
                 (char.upper(), str(round(av_pos))))

        else:
            
            print('"{0}" was not found.'.format(char.upper()))

#3

def max_letter():

    file = open("loremipsum.txt")
    trans_tbl = str.maketrans('', '', punctuation)
    word_arr = file.read().lower().translate(trans_tbl).split()
    
    for char in ascii_lowercase:
        prev = ''
        for word in word_arr:

            letter_count = word.count(char)

            if letter_count > prev.count(char):

                prev = word
        
        if prev:
            print('"{0}" contains the most "{1}"'.format(prev, char.upper()))
        else:
            print('"{0}" was not found.'.format(char.upper()))

#4

def common_pre():

       file = open("loremipsum.txt")
       trans_tbl = str.maketrans('', '', punctuation)
       word_arr = file.read().translate(trans_tbl).split()

       match = []

       for word in word_arr:
           
           if word not in match and word.lower() not in match:
               
               match.append(word)
               
    
       for word in match:

            prec_words = []
            
            for word_index, orig_word in enumerate(word_arr):

                if orig_word.lower() == word.lower():

                    if word_index - 1 >= 0:

                        prec_words.append(word_arr[word_index - 1].lower())

 
            unique = set(prec_words)
                
            if len(prec_words) == len(unique):
                
                data = Counter(prec_words)
                print('"{0}" is most commonly preceded by "{1}".'.format
                     (word, data.most_common(1)[0][0]))
                
            elif len(prec_words) != len(unique):
                
                print('"{0}" is most commonly preceded by "{1}".'.format
                     (word, prec_words[0]))
                
            else:
                print('"{0}" is not preceeded by anything'.format(word))

#5

def recur_exp(base, power):

    if power == 0:
        return 1
    elif power < 0:
        return recur_exp(base, power + 1) / base
    elif power % 2 == 0:
        return recur_exp(base ** 2, power / 2)
    else:
        return base * recur_exp(base ** 2, (power - 1) / 2)

#6

def iter_exp(base, power):

    total = 1

    for i in range(0, abs(power)):
        total *= base

    if power < 0:
        return 1 / total
    elif base == 0:
        return 0
    else: 
        return total

    
