#current personal best solver
#lot of inefficeny in "filtdata"
#first guess is preset to "tares" in order to speed up solve time as that will always be the result of the solver
#Average over 1k itterations in solvertester.py is 5.231 guesses per solve


#import colors
from colorama import Fore, Back, Style

#import random
import random

#make alphabet:
alphabet = []
inital_val = ord("a")
end_val = ord("z")
while inital_val <= end_val:
    alphabet.append(chr(inital_val))
    inital_val += 1

#init functions
def convert_to_list(input_string):
    eli = []
    for i in range(len(input_string)):
        eli.append(input_string[i])
    return eli

def fill_empty_list(input_list):
    eli = []
    for i in range(len(input_list)):
        eli.append(0)
    return eli

def remake_data(input_data):
    my_file = open(input_data, 'r')

    #read text file into list
    data = my_file.read()
    new_data = []
    temp = ""
    for i in data:
        if i == "\n":
            new_data.append(temp)
            temp = ""
        else:
            temp += i
    return new_data

def filtdata(dimensions, guess_pair):
    init = len(ds)
    for val in range(len(dimensions)):
        if dimensions[val] == 0:
            for word in ds:
                if word.__contains__(guess_pair[val]):
                    if guess_pair.count(guess_pair[val]) == 1:
                            ds.remove(word)
                    elif guess_pair.count(guess_pair[val]) == 2:
                        a = 0
        elif dimensions[val] == 1: 
            for word in ds:
                if word.__contains__(guess_pair[val]):
                    if word[val] == guess_pair[val]:
                        ds.remove(word)
                else:
                    ds.remove(word)
        else:
            for word in ds:
                if word.__contains__(guess_pair[val]):
                    if word[val] != guess_pair[val]:
                        ds.remove(word)
                else:
                    ds.remove(word)
    exit = len(ds)
    diff = init - exit
    print("Removed", diff, "values")
    print(len(ds), "values remaning")
    if len(ds) < 10:
        print("Remaning values:", ds)

def next_guess(guess_total):
    if guess_total == 1:
        temp = "tares"
    else:
        coreCoef = []
        for val in ds:
            num = 0
            for oval in ds:
                for let in range(len(val)):
                    if val[let] == oval[let]:
                        num += 8
                        if val.count(val[let]) > 1:
                            num -= 4
                    elif oval.__contains__(val[let]):
                        num += 3
                        if val.count(val[let]) > 1:
                            num -= 1.5
            num = num/len(ds)
            coreCoef.append(num)
            if len(ds) < 50:
                print(val, num)
        maxval = max(coreCoef)
        temp = ds[coreCoef.index(maxval)]
    
        print("average:", sum(coreCoef)/len(coreCoef))
        print("Max Corecoeff: ", maxval)
    return temp
ds = remake_data('sgb-words.txt')

all_words = remake_data('sgb-words.txt')
#mystery_word = "askew"
mystery_word = random.choice(remake_data('sgb-words.txt'))
print(mystery_word)
#Convert to list
mystery_list = convert_to_list(mystery_word)
num_guess = 1
correct_check = False
while num_guess > 0:
    #Choose Guess
    guess_word = next_guess(num_guess)

    #Make sure the length is always 5
    valid_check = False
    if all_words.__contains__(guess_word):
        valid_check = True
    while len(guess_word) != 5 or valid_check == False:
        guess_word = input("Enter Guess Word (The length must be 5):")
        valid_check = False
        if all_words.__contains__(guess_word):
            valid_check = True
    guess_word = guess_word.lower()
    #Convert to list
    guess_list = convert_to_list(guess_word)

    #check if correct
    if guess_list == mystery_list:
        correct_check = True
        break
    else:
        #fill output list for later
        output = fill_empty_list(guess_list)

        #calculate for duplicate values within both guess and mystery
        duplicates_guess = [letter for letter in guess_list if guess_list.count(letter) > 1]
        unique_duplicates_guess = list(set(duplicates_guess))
        duplicates_mystery = [letter for letter in mystery_list if mystery_list.count(letter) > 1]
        unique_duplicates_mystery = list(set(duplicates_mystery))
        #Check which case it is
        if duplicates_guess == [] and duplicates_mystery == []:
            for i in range(len(guess_list)):
                if guess_list[i] == mystery_list[i]:
                    output[i] = 2
                elif mystery_word.__contains__(guess_word[i]):
                    output[i] = 1
        elif unique_duplicates_guess != [] and unique_duplicates_mystery != []:
            if len(unique_duplicates_mystery) + len (unique_duplicates_guess) == 2:
                if unique_duplicates_mystery[0] == unique_duplicates_guess[0]:
                    for i in range(len(guess_list)):
                        if guess_list[i] == mystery_list[i]:
                            output[i] = 2
                        elif mystery_word.__contains__(guess_word[i]):
                            output[i] = 1
                else:
                    guess_list_index_one = []
                    temp_list = guess_list.copy()
                    for i in range(temp_list.count(unique_duplicates_guess[0])):
                        guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                        temp_list[guess_list_index_one[i]] = "*"
                    for i in range(len(guess_list)):
                        if str(guess_list_index_one).__contains__(str(i)):
                            if mystery_word.__contains__(guess_word[i]):
                                if guess_list[i] == mystery_list[i]:
                                    output[i] = 2
                                else:
                                    for x in range(len(guess_list_index_one)):
                                        if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                            output[i] = 0
                                            break
                                        else:
                                            output[i] = 1
                        elif guess_list[i] == mystery_list[i]:
                            output[i] = 2
                        elif mystery_word.__contains__(guess_word[i]):
                            output[i] = 1  
            elif len(unique_duplicates_mystery) > len (unique_duplicates_guess):
                if unique_duplicates_mystery[0] != unique_duplicates_guess[0]:
                    if unique_duplicates_mystery[1] != unique_duplicates_guess[0]:
                        guess_list_index_one = []
                        temp_list = guess_list.copy()
                        for i in range(temp_list.count(unique_duplicates_guess[0])):
                            guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                            temp_list[guess_list_index_one[i]] = "*"
                        for i in range(len(guess_list)):
                            if str(guess_list_index_one).__contains__(str(i)):
                                if mystery_word.__contains__(guess_word[i]):
                                    if guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    else:
                                        for x in range(len(guess_list_index_one)):
                                            if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                output[i] = 0
                                                break
                                            else:
                                                output[i] = 1
                            elif guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1  
                    else:
                        for i in range(len(guess_list)):
                            if guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1
                else:
                    for i in range(len(guess_list)):
                        if guess_list[i] == mystery_list[i]:
                            output[i] = 2
                        elif mystery_word.__contains__(guess_word[i]):
                            output[i] = 1
            elif len(unique_duplicates_mystery) < len (unique_duplicates_guess):
                if unique_duplicates_guess[0] != unique_duplicates_mystery[0]:
                    if unique_duplicates_guess[1] != unique_duplicates_mystery[0]:
                        guess_list_index_one = []
                        guess_list_index_two = []
                        temp_list = guess_list.copy()
                        for i in range(temp_list.count(unique_duplicates_guess[0])):
                            guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                            temp_list[guess_list_index_one[i]] = "*"
                        for i in range(temp_list.count(unique_duplicates_guess[1])):
                            guess_list_index_two.append(temp_list.index(unique_duplicates_guess[1]))
                            temp_list[guess_list_index_two[i]] = "*"
                        for i in range(len(guess_list)):
                            if str(guess_list_index_one).__contains__(str(i)) or str(guess_list_index_two).__contains__(str(i)):
                                if mystery_word.__contains__(guess_word[i]):
                                    if guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    else:
                                        for x in range(len(guess_list_index_one)):
                                            if guess_list[i] == unique_duplicates_guess[0]:
                                                if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                    output[i] = 0
                                                    break
                                                else:
                                                    output[i] = 1
                                            elif guess_list[i] == unique_duplicates_guess[1]:
                                                if guess_list[guess_list_index_two[x]] == mystery_list[guess_list_index_two[x]]:
                                                    output[i] = 0
                                                    break
                                                else:
                                                    output[i] = 1
                            elif guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1
                    else:
                        guess_list_index_one = []
                        temp_list = guess_list.copy()
                        for i in range(temp_list.count(unique_duplicates_guess[0])):
                            guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                            temp_list[guess_list_index_one[i]] = "*"
                        for i in range(len(guess_list)):
                            if str(guess_list_index_one).__contains__(str(i)):
                                if mystery_word.__contains__(guess_word[i]):
                                    if guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    else:
                                        for x in range(len(guess_list_index_one)):
                                            if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                output[i] = 0
                                                break
                                            else:
                                                output[i] = 1
                            elif guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1         
                else:
                    guess_list_index_one = []
                    temp_list = guess_list.copy()
                    for i in range(temp_list.count(unique_duplicates_guess[1])):
                        guess_list_index_one.append(temp_list.index(unique_duplicates_guess[1]))
                        temp_list[guess_list_index_one[i]] = "*"
                    for i in range(len(guess_list)):
                        if str(guess_list_index_one).__contains__(str(i)):
                            if mystery_word.__contains__(guess_word[i]):
                                if guess_list[i] == mystery_list[i]:
                                    output[i] = 2
                                else:
                                    for x in range(len(guess_list_index_one)):
                                        if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                            output[i] = 0
                                            break
                                        else:
                                            output[i] = 1
                        elif guess_list[i] == mystery_list[i]:
                            output[i] = 2
                        elif mystery_word.__contains__(guess_word[i]):
                            output[i] = 1    
            else:
                if unique_duplicates_guess[0] != unique_duplicates_mystery[0]:
                    if unique_duplicates_guess[0] != unique_duplicates_mystery[1]:
                        if unique_duplicates_guess[1] != unique_duplicates_mystery[0]:
                            if unique_duplicates_guess[1] != unique_duplicates_mystery[1]:
                                guess_list_index_one = []
                                guess_list_index_two = []
                                temp_list = guess_list.copy()
                                for i in range(temp_list.count(unique_duplicates_guess[0])):
                                    guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                                    temp_list[guess_list_index_one[i]] = "*"
                                for i in range(temp_list.count(unique_duplicates_guess[1])):
                                    guess_list_index_two.append(temp_list.index(unique_duplicates_guess[1]))
                                    temp_list[guess_list_index_two[i]] = "*"
                                for i in range(len(guess_list)):
                                    if str(guess_list_index_one).__contains__(str(i)) or str(guess_list_index_two).__contains__(str(i)):
                                        if mystery_word.__contains__(guess_word[i]):
                                            if guess_list[i] == mystery_list[i]:
                                                output[i] = 2
                                            else:
                                                for x in range(len(guess_list_index_one)):
                                                    if guess_list[i] == unique_duplicates_guess[0]:
                                                        if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                            output[i] = 0
                                                            break
                                                        else:
                                                            output[i] = 1
                                                    elif guess_list[i] == unique_duplicates_guess[1]:
                                                        if guess_list[guess_list_index_two[x]] == mystery_list[guess_list_index_two[x]]:
                                                            output[i] = 0
                                                            break
                                                        else:
                                                            output[i] = 1
                                    elif guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    elif mystery_word.__contains__(guess_word[i]):
                                        output[i] = 1
                            else:
                                guess_list_index_one = []
                                temp_list = guess_list.copy()
                                for i in range(temp_list.count(unique_duplicates_guess[1])):
                                    guess_list_index_one.append(temp_list.index(unique_duplicates_guess[1]))
                                    temp_list[guess_list_index_one[i]] = "*"
                                for i in range(len(guess_list)):
                                    if str(guess_list_index_one).__contains__(str(i)):
                                        if mystery_word.__contains__(guess_word[i]):
                                            if guess_list[i] == mystery_list[i]:
                                                output[i] = 2
                                            else:
                                                for x in range(len(guess_list_index_one)):
                                                    if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                        output[i] = 0
                                                        break
                                                    else:
                                                        output[i] = 1
                                    elif guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    elif mystery_word.__contains__(guess_word[i]):
                                        output[i] = 1
                        else:
                            guess_list_index_one = []
                            temp_list = guess_list.copy()
                            for i in range(temp_list.count(unique_duplicates_guess[1])):
                                guess_list_index_one.append(temp_list.index(unique_duplicates_guess[1]))
                                temp_list[guess_list_index_one[i]] = "*"
                            for i in range(len(guess_list)):
                                if str(guess_list_index_one).__contains__(str(i)):
                                    if mystery_word.__contains__(guess_word[i]):
                                        if guess_list[i] == mystery_list[i]:
                                            output[i] = 2
                                        else:
                                            for x in range(len(guess_list_index_one)):
                                                if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                    output[i] = 0
                                                    break
                                                else:
                                                    output[i] = 1
                                elif guess_list[i] == mystery_list[i]:
                                    output[i] = 2
                                elif mystery_word.__contains__(guess_word[i]):
                                    output[i] = 1
                    elif unique_duplicates_guess[1] == unique_duplicates_mystery[0]:
                        for i in range(len(guess_list)):
                            if guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1
                    else:
                        guess_list_index_one = []
                        temp_list = guess_list.copy()
                        for i in range(temp_list.count(unique_duplicates_guess[1])):
                            guess_list_index_one.append(temp_list.index(unique_duplicates_guess[1]))
                            temp_list[guess_list_index_one[i]] = "*"
                        for i in range(len(guess_list)):
                            if str(guess_list_index_one).__contains__(str(i)):
                                if mystery_word.__contains__(guess_word[i]):
                                    if guess_list[i] == mystery_list[i]:
                                        output[i] = 2
                                    else:
                                        for x in range(len(guess_list_index_one)):
                                            if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                                output[i] = 0
                                                break
                                            else:
                                                output[i] = 1
                            elif guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1    
                elif unique_duplicates_guess[1] == unique_duplicates_mystery[1]:
                        for i in range(len(guess_list)):
                            if guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            elif mystery_word.__contains__(guess_word[i]):
                                output[i] = 1
                else:
                    guess_list_index_one = []
                    temp_list = guess_list.copy()
                    for i in range(temp_list.count(unique_duplicates_guess[1])):
                        guess_list_index_one.append(temp_list.index(unique_duplicates_guess[1]))
                        temp_list[guess_list_index_one[i]] = "*"
                    for i in range(len(guess_list)):
                        if str(guess_list_index_one).__contains__(str(i)):
                            if mystery_word.__contains__(guess_word[i]):
                                if guess_list[i] == mystery_list[i]:
                                    output[i] = 2
                                else:
                                    for x in range(len(guess_list_index_one)):
                                        if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                            output[i] = 0
                                            break
                                        else:
                                            output[i] = 1
                        elif guess_list[i] == mystery_list[i]:
                            output[i] = 2
                        elif mystery_word.__contains__(guess_word[i]):
                            output[i] = 1    
        elif unique_duplicates_guess != []:
            if len(unique_duplicates_guess) > 1:
                guess_list_index_one = []
                guess_list_index_two = []
                temp_list = guess_list.copy()
                for i in range(temp_list.count(unique_duplicates_guess[0])):
                    guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                    temp_list[guess_list_index_one[i]] = "*"
                for i in range(temp_list.count(unique_duplicates_guess[1])):
                    guess_list_index_two.append(temp_list.index(unique_duplicates_guess[1]))
                    temp_list[guess_list_index_two[i]] = "*"
                for i in range(len(guess_list)):
                    if str(guess_list_index_one).__contains__(str(i)) or str(guess_list_index_two).__contains__(str(i)):
                        if mystery_word.__contains__(guess_word[i]):
                            if guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            else:
                                for x in range(len(guess_list_index_one)):
                                    if guess_list[i] == unique_duplicates_guess[0]:
                                        if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                            output[i] = 0
                                            break
                                        else:
                                            output[i] = 1
                                    elif guess_list[i] == unique_duplicates_guess[1]:
                                        if guess_list[guess_list_index_two[x]] == mystery_list[guess_list_index_two[x]]:
                                            output[i] = 0
                                            break
                                        else:
                                            output[i] = 1
                    elif guess_list[i] == mystery_list[i]:
                        output[i] = 2
                    elif mystery_word.__contains__(guess_word[i]):
                        output[i] = 1
            else:
                guess_list_index_one = []
                temp_list = guess_list.copy()
                for i in range(temp_list.count(unique_duplicates_guess[0])):
                    guess_list_index_one.append(temp_list.index(unique_duplicates_guess[0]))
                    temp_list[guess_list_index_one[i]] = "*"
                for i in range(len(guess_list)):
                    if str(guess_list_index_one).__contains__(str(i)):
                        if mystery_word.__contains__(guess_word[i]):
                            if guess_list[i] == mystery_list[i]:
                                output[i] = 2
                            else:
                                for x in range(len(guess_list_index_one)):
                                    if guess_list[guess_list_index_one[x]] == mystery_list[guess_list_index_one[x]]:
                                        output[i] = 0
                                        break
                                    else:
                                        output[i] = 1
                    elif guess_list[i] == mystery_list[i]:
                        output[i] = 2
                    elif mystery_word.__contains__(guess_word[i]):
                        output[i] = 1         
        elif unique_duplicates_mystery != []:
            for i in range(len(guess_list)):
                if guess_list[i] == mystery_list[i]:
                    output[i] = 2
                elif mystery_word.__contains__(guess_word[i]):
                    output[i] = 1

        colored_output = [0,0,0,0,0]
        for i in range(len(output)):
            if output[i] == 2:
                colored_output[i] = Fore.GREEN
            elif output[i] == 1:
                colored_output[i] = Fore.YELLOW
            else:
                colored_output[i] = Fore.RED

        output_string = ""
        for i in guess_list:
            output_string += str(i)
        print(colored_output[0]+ output_string[0] + colored_output[1] + output_string[1] + colored_output[2] + output_string[2] + colored_output[3] + output_string[3] +  colored_output[4] + output_string[4])
        if ds.__contains__(next_guess(num_guess)):
            ds.remove(next_guess(num_guess))
        filtdata(output,guess_list)
    num_guess += 1
if correct_check == True:
    print(Fore.GREEN + f'You got it in {num_guess} guesses!')
    print(f'The mystery word was {mystery_word}!')
else:
    print(Fore.YELLOW + f"You did not guess {mystery_word} in 6 guesses!")
