import wordplay.scrabble as sbl

is_longest_word = 0
for word in sbl.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index+1)]:
            is_palindrome = False
    if is_palindrome and is_longest_word < len(word):
        longest_word = word
        is_longest_word = len(word)
print("longest Palindrome in Scrabble is : " + longest_word)    
 
        
