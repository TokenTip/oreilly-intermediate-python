import wordplay.scrabble as sbl

vowels= "aeiou"
def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in sbl.wordlist:
    if has_all_vowels(word):
        print (word)