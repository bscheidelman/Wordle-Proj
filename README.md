# inpso:
hi, this was a for-fun project that I started because I was bored on a train ride!
while I garuntee most of the solutions are extremly inefficent, I had a lot of time making them.

# notes:
the sgb-words.txt is the word list used for this project.
the current final iteration is correlationsolver.py.
solvertester.py can be used to test the average solve times of each solution
current best average: ~5.231 guesses per solve over 1k itterations. PS: You can actualy play wordle remake!

# improvments:
the filtdata function in all versions is extremely underveloped and of ten results in vast underfiltering

# problems
for wordleremake.py, which is the basis that I made for which all of the code runs on, there is most likely some problem when solving for words that have 3 of one letter such as "daddy."
Sorry :(

# scoring system
the basis for the [+8, +3] scoring system used in corelation coeficent based solver can be found in "ss.png" as that combination netted the lowest avg guess time over 500 iterations of each combo
