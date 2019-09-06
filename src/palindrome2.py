import wordplay.scrabble as sbl

longest_word = ""
for word in sbl.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest_word):
        longest_word = word
print("longest Palindrome in Scrabble is : " + longest_word)
 
        
