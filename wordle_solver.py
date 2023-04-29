import csv
with open("./wordle_words.csv","r") as file:
    csvreader = csv.reader(file)
    words=file.read().splitlines()
print("There are",len(words),"words")  
all_the_present_letters = set()
letter_max_count = []
for loop in range(10):
    #------------------INPUT------------------------------
    letters_not_in = set(input("Give me all the letters that are in grey : ").replace(" ",""))
    letters_in = list(input("Give me all the letters that are in grenn or yellow (duplicates included) : ").replace(" ",""))
    positioning_right = list(input("Write the word with '-' for the letters that are in grey or yellow and the LETTER when the letter is in green : ").replace(" ",""))
    positioning_wrong  = list(input("Write the word with '-' for the letters that are green or grey and the LETTER when the letter is in yellow : ").replace(" ",""))
    #------------------------------------------------------
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
    print(words)
    print("There are",len(words),"words left")