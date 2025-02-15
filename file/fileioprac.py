# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.


# f =  open("poem.txt")
# content = f.read()
# f.close()

# if ('twinkle' in content.lower):
#     print("yes, it contains")

# else:
#     print("it doesn't contain")



# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random


def game():
    print("you are playing a game !!!!!")
    score = random.randint(1,62)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score: {score}")

    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))


    return score
game()
    







# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year old.

# 4. A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.

# 5. Repeat program 4 for a list of such words to be censored.

# 6. Write a program to mine a log file and find out whether it contains 'python'.

# 7. Write a program to find out the line number where python is present from ques 6.

# 8. Write a program to make a copy of a text file "this. txt"

# 9. Write a program to find out whether a file is identical & matches the content of another file.

# 10. Write a program to wipe out the content of a file using python.

# 11. Write a python program to rename a file to "renamed_by_python.txt.