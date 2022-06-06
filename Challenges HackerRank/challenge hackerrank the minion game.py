""" Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
Your task is to determine the winner of the game and their score.

minion_game has the following parameters:
string string: the string to analyze

Prints
string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format
A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Sample Input
BANANA

Sample Output
Stuart 12"""


vowels = 'AEIOU'

def minion_game(full_str):
    # your code goes here
    score_Kevin, score_Stuart = 0, 0
    for i in range(len(full_str)):
        if full_str[i] in vowels:
            score_Kevin += len(full_str) - i
        else:
            score_Stuart += len(full_str) - i

    if score_Kevin > score_Stuart:
        print(f'Kevin {score_Kevin}')
    elif score_Stuart > score_Kevin:
        print(f'Stuart {score_Stuart}')
    else:
        print('Draw')
    return



if __name__ == '__main__':
    full_str = input()
    minion_game(full_str)