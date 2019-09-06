import time

#Sonnets using dictionary - is very fast than list as Dict uses Hash to find keys
my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((etl,1) for etl in word_list)

counter = 0
start = time.time()

for word in my_words:
    if word not in word_list:
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d " % counter)
print("Time elapsed: %.1f seconds: " % (stop - start) )