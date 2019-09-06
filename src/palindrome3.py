import wordplay.scrabble as sbl
import string

longest_word = ""
for word in sbl.wordlist:
    if word == word[::-1] and len(word) > len(longest_word):
        longest_word = word
print("longest Palindrome in Scrabble is : " + longest_word)
 
        
