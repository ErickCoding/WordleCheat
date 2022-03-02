'''wordle solution
1. create a  list for each letter in the alphabet. Each list contains every 5 letter word that has its letter.
ex. a=(apple,drake,atoms,etc)
2. for each word + each list then set so it removes all duplicates then len() the list to find length
the longest length will be the word(s) i can choose from to use. code to identify the largest number
 print(word with the longest list)
3. input section for which letter were correct. im thinking loop if statements
if does not have the word:
    remove all words with that letter with a for loop if it has the letter then remove the word from the list
    and have it equal to a new list
if has the word wrong position:
    remove all words without the letter in the new list with for loop if it...;
    remove all words with the letter in the same position from the new list if it...
if the word is in the right position(probably do this first as it removes more stuff):
    remove all word with if it does not [,position]=letter remove it
this creates a smaller list of words
4. repeat the steps 1&2 with the remaining words in the new list find the word with the longest list.
and input it in the thing.
5.repeat step 3 to remove things from the list and limit the words downs repeat till the last chance.

extras
-probably to reduce calculations i would rewrite each word so that it has no duplicate letters in the word then
calculate length since if the results for a letter doesnt change even if position changes in this case.
-maybe i turn the guessed word into a single item list need to test out
-so the first word should always be the same as long as there is a clear cut word with the longest list.
-set variable = to multiple choice input for the user to select which letters were wrong,correct,
correct but wrong placement. lazy way would be do it five times but theres probably code to make it easier
-have the if statements be if correct then do this to remove words from the list. something like
if first word=correct: if guessed_word[0,1] != new_list[:,1]: remove same concept for all the other choices
-i dont want to make a new list everytime so the first step will be the longest as it has to find all distinct
words for each letter in a 5 letter word. and as we continue to chop down choices the processing time should be
significantly faster.
-this is just a glorified guess who game. So next step over this would probably sql then python. Find the longest join
since if theres 2500 words and the max is 1000 words that have s but majority of words have s in the beginning itll
provide extra info.
-questions to think about
-position
-if there are multiple words with the longest list how does position help me choose
-word with longest list vs word with better letter postioning
-at one point is positioning more important then length of list if there ever is

orignal list with all words in database----chopped down list after first word----find the next longest list------
get results-------chop down the list even more--------till all 6 guesses are done.

tune ups
1. add a break measure when they guess the right word that breaks all the loops.
2. check if there is a more effective way to map the stuff
3. its definetly faster if i ask the responses for the words all at once. so have 5 input for asking the wordle response
for all five letters in the word.
I can think group it by the letters with a for loop. then i can do the same coding but instead of searching for one letter
at a time i can just do multiple. so if letters 1 and 3 were correct i could do if f[0]!=f[0] and f[2]!=f[2] apend etc
the issue is thinking about how to filter it out before i should think about using what method list, dictionary, and the
the uses of map instead of 4 loop as said before
4. also should have an ending message if i can't get it right or something'''


word_list=["apple", "bbbbb","raise","fried","apleb", "dasga", "helas" ]
dictionary={}
result=list(map(lambda x: set(x), word_list))
for x in range(0,len(word_list)-1):
    y=0
    for word in result:
        if result[x]&word:
            y+=1
    dictionary[word_list[x]]=y
print(max(dictionary, key=dictionary.get))
optimal_word=max(dictionary, key=dictionary.get)
for t in range (1,7):
    for v in range(0,5):
        deleted_list = []
        wordle_response=input("Guess number "+str(t)+" and letter number "+str(v+1)+" response: \na. Wrong letter \nb. Right letter and placement \nc. Right letter wrong placement \nd. Entire Word Correct \n" )
        if wordle_response=="d":
            print("your welcome")
            #break
        elif wordle_response=="a":
            for entry in dictionary:
                if optimal_word[v] in entry:
                    deleted_list.append(entry)
        elif wordle_response=="b":
            for entry in dictionary:
                if optimal_word[v] != entry[v]:
                    deleted_list.append(entry)
        elif wordle_response=="c":
            for entry in dictionary:
                if optimal_word[v] == entry[v]:
                    deleted_list.append(entry)
                if optimal_word[v] not in entry:
                    deleted_list.append(entry)
        for deletes in deleted_list:
            dictionary.pop(deletes)
    print(max(dictionary, key=dictionary.get))
