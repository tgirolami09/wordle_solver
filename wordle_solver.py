import csv

def help_user(words:list):
    """
    Gives the user what word(or words)they should play
    """

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    dct = {}
    for letter in alphabet:
        dct[letter] = 0
    for word in words:
        for letter in word:
            dct[letter]+=1
    max_values = [0]*5
    max_values_letter = [""]*5
    for key in dct:
        if dct[key] > min(max_values):
            max_values_letter.pop(max_values.index(min(max_values)))
            max_values.pop(max_values.index(min(max_values)))
            max_values.append(dct[key])
            max_values_letter.append(key)

    tookeep = []
    value = max(max_values)
    letter = max_values_letter[max_values.index(value)]
    for word in words:
        if letter in word:
            tookeep.append(word)


    for value in max_values:
        if value != max(max_values) and len(tookeep) > 1:
            letter = max_values_letter[max_values.index(value)]
            index =-1
            while index != len(tookeep)-1 and len(tookeep) > 1:
                index+=1
                word = tookeep[index]
                if letter not in word:
                    tookeep.pop(index)
                    index-=1

        elif len(tookeep) == 1:
            break

    if len(tookeep) == 1:
        print("You should play :",tookeep[0])
    else:
        print("You should play :" ,end=" ")
        for word in tookeep:
            if word != tookeep[-1]:
                print(word,end=" or ")
            else:
                print(word)

def help_user_second_turn(guess1:list):
    words = get_word_list()
    words = remove_words_with_letter(guess1,words)
    return help_user(words)

def get_word_list():
    """
    Gets the word list
    """
    with open("./Wordle Solvers/wordle_words.csv","r") as file:
        csvreader = csv.reader(file)
        words=file.read().splitlines()
        return words

def remove_words_with_letter(letters_not_in_the_word:set,words:list):
    """
    Returns the second string without all the words containing the letters in the first string
    """
    for letter in letters_not_in_the_word:
            loop = -1
            while loop != len(words)-1:
                loop+=1
                if letter in words[loop]:
                    words.pop(loop)
                    loop -= 1
    return words

with open("./Wordle Solvers/wordle_words.csv","r") as file:
    csvreader = csv.reader(file)
    words=file.read().splitlines()
print("There are",len(words),"words")  
all_the_present_letters = set() 
letter_max_count = []
help_user(words)
for turn in range(10):
    #------------------INPUT----------------------------------------------
    guess = list(input("Give me your guess in lowercase letters : ").replace(" ",""))
    states = list(input("Give me the color of the letters in your guess 'w for grey' 'y for yellow' and 'g for green' : ").replace(" ",""))
    letters_not_in = set()
    letters_in = list()
    positioning_right = list()
    positioning_wrong  = list()
    index =-1
    for state in states:
        index+=1
        if state == "w":
            positioning_right.append("-")
            positioning_wrong.append("-")
            letters_not_in.add(guess[index])
        elif state == "y":
            positioning_wrong.append(guess[index])
            positioning_right.append("-")
            letters_in.append(guess[index])
        elif state == "g":
            positioning_wrong.append("-")
            positioning_right.append(guess[index])
            letters_in.append(guess[index])
    #------------------------------------------------------------------------
    letters_to_get_rid = set()
    for letter in letters_in:
        all_the_present_letters.add(letter)
        if letters_in.count(letter) != 1 and letter not in letter_max_count:
            letter_max_count.append(letter)
            letter_max_count.append(str(letters_in.count(letter)))
    
    for letter in letters_not_in:
        if letter in all_the_present_letters:
            if letter in letter_max_count:
                if letter_max_count[letter_max_count.index(letter)+1].isnumeric():
                    if letter_max_count[letter_max_count.index(letter)+1] ==2:
                        letter_max_count[letter_max_count.index(letter)+1] = "é"
                    elif letter_max_count[letter_max_count.index(letter)+1] == 3:
                        letter_max_count[letter_max_count.index(letter)+1] = '"'
            else:
                letter_max_count.append(letter)
                letter_max_count.append("&")
        else:
            letters_to_get_rid.add(letter)

    if len(letter_max_count) != 0:
        pos =-1
        while pos != len(words)-1:
            pos+=1
            for index in range(0,len(letter_max_count),2):
                if letter_max_count[index+1].isnumeric():
                    if words[pos].count(letter_max_count[index]) < int(letter_max_count[index+1]):
                        words.pop(pos)
                        pos-=1
                        break
                elif letter_max_count[index+1] == "&":
                    if words[pos].count(letter_max_count[index]) != 1:
                        words.pop(pos)
                        pos-=1
                        break
                elif letter_max_count[index+1]== "é":
                    if words[pos].count(letter_max_count[index]) != 2:
                        words.pop(pos)
                        pos-=1
                        break
                elif letter_max_count[index+1]=='"':
                    if words[pos].count(letter_max_count[index]) != 3:
                        words.pop(pos)
                        pos-=1
                        break

    #-----------------------------------------------
    for letter in letters_to_get_rid:
        loop = -1
        while loop != len(words)-1:
            loop+=1
            if letter in words[loop]:
                words.pop(loop)
                loop -= 1


    #---------------------------------------------
    for letter in letters_in:
        loop  = -1
        while loop != len(words)-1:
            loop+=1
            if letter not in words[loop]:
                words.pop(loop)
                loop -= 1
    #-----------------------------------------------------)
    position = -1
    for item in positioning_right:
        position +=1
        if item.isalpha():
            loop = -1
            while loop != len(words)-1: 
                loop += 1
                mot = list(words[loop])
                if item != mot[position]:
                    words.pop(loop)
                    loop -= 1
    #----------------------------------------------------------
    position = -1
    for item in positioning_wrong:
        position +=1
        if item.isalpha():
            loop = -1
            while loop != len(words)-1: 
                loop += 1
                mot = list(words[loop])
                if item == mot[position]:
                    words.pop(loop)
                    loop -= 1
    #-------------------------------------------------------------
    if len(words) != 1:
        print(words)
        print("There are",len(words),"words left")
        help_user(words)
    elif len(words) == 1:
        print("The solution should be :",words[0])
        break
    elif len(words) == 0:
        print("I can't find a solution")
        break
