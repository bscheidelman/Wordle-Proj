# inpso:
hi, this was a for-fun project that I started because I was bored on a train ride!
while I guarantee most of the solutions are extremly inefficent, I had a lot of fun making them.

# notes:
the sgb-words.txt is the word list used for this project.
the current final iteration is correlationsolver.py.
solvertester.py can be used to test the average solve times of each solution
current best average: ~5.231 guesses per solve over 1k itterations. PS: You can actualy play wordle remake!

# improvments:
the filtdata function in all versions is extremely underveloped and often results in vast underfiltering.
improving it's manner of handling duplicates within words and a number of other cases could vastly decrease the avg guess time.

# scoring system
the basis for the [+8, +3] scoring system used in corelation coeficent based solver can be found in "ss.png" as that combination netted the lowest avg guess time over 500 iterations of each combo
the subsequent [-4,-1.5] found within the scoring system are to discourage guessing duplicates too early as too not double count scores. 
