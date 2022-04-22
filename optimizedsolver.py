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

def next_guess(guess_total):
    if guess_total == 1:
        temp = "crane"
    elif guess_total == 2:
        temp = "godly"
    elif guess_total == 3:
        temp = "swift"
    elif guess_total ==4:
        temp = "bumph"
    else:
        temp = ds[0]
    return temp
ds = remake_data('sgb-words.txt')

iteration = 0
average_list = []
while iteration < 100:
    ds = remake_data('sgb-words.txt')
    iteration += 1
    all_words = remake_data('sgb-words.txt')
    mystery_word = random.choice(remake_data('sgb-words.txt'))
    #Convert to list
    mystery_list = convert_to_list(mystery_word)
    print(mystery_word)
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
                        print(1)
                        if unique_duplicates_guess[0] != unique_duplicates_mystery[1]:
                            print(2)
                            if unique_duplicates_guess[1] != unique_duplicates_mystery[0]:
                                print(3)
                                if unique_duplicates_guess[1] != unique_duplicates_mystery[1]:
                                    print(4)
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
        if ds.__contains__(next_guess(num_guess)):
            ds.remove(next_guess(num_guess))
        filtdata(output,guess_list)
        num_guess += 1

    print("Guessed", mystery_word, "in", num_guess)
    average_list.append(num_guess)
    print("Current Itteration:", iteration)
sum = 0
for val in average_list:
    sum += val
final_avg = sum/len(average_list)
print("Final Avg = ", final_avg)