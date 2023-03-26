"""
Words Score

Consider that vowels in the alphabet are a, e, i, o, u and y.

Function score_words takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function score_words such that it returns a correct score.

Your function will be tested on several cases by the locked template code.
"""

vowelList = {"a", "e", "i", "o", "u"}

sentence = "This is a big sentenc"  #score should be 5
list2 = sentence.split(" ")

mainscore = 0
for x in list2:
    #print(x)
    score = 0
    for y in vowelList:
        if y in x:
            print(x)
            score = score+1
        if score%2==0:
            mainscore = mainscore+2
        else:
            mainscore = mainscore+1

print(f"Total score is {mainscore}")


#Another was of doing it, the below one is giving correct output

sentence = "This is a big sentenc"

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    words = words.split(" ")
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score = score + 2
        else:
            score = score + 1
    return score

print(score_words(sentence))