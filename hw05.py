"""
Name: Lina Cubie
Peers: None
References: I googled syntax and list iteration review when struggling with using the correct types of variables for slicing or function usage
"""

def get_letter():
    """ Returns the letters "A", "B", or "C" if the user inputs it, otherwise the loop continues """
    while True:
        letter = input("Give an single uppercase letter: ")
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        elif letter != "A" and letter != "B" and letter != "C":
            print("Error: You provided the wrong character.")
            continue
        else:
            return letter

def get_digit():
    """ Returns a digit in range [1,3] if the user inputs it, otherwise the loop continues"""
    while True:
        digit = input("Give an single number character: ")
        if digit.isdigit() == False:
            print("Error: your input should be only digits.")
            continue
        elif int(digit) not in [1,2, 3]:
            print("Error: a single digit needs to be in [1,3].")
            continue
        else:
            return digit
            
        


def check_pattern(letter, digit, lst):
    """ Uses the letter and digit inputs from the user and checks/prints if they are in that order within strings in the st_list"""
    print("Strings with the pattern:")
    for word in lst: #iterates through each word in the input list
        printed = False #The current word has not been printed yet
        if word.find(f"{letter}") != -1 and word.find(f"{digit}") != -1 : #Verifies if the word has the letter or digit
            index = 0
            for i in range(index, len(word)): #iterates through the letter in each word
                let = word[i]
                if printed == True: #If the correct letter-digit order has occured, then the word has printed, there is no need to check next let, so we break to check the next word  
                    break
                elif let != letter: #if the let in the word is not the letter continue to check the next let in the word
                    i+=1
                    continue
                elif let == letter: #if the let is letter, check if digit follows anywhere in the word
                    word2 = word[i:] #splices word for a new string (word2) to iterate through
                    for let2 in word2: #iterates through the remaining let in the word (let2) (uses a splice from the word_iterator value to the end of the word)
                        if let2 != digit: #if the let2 is not the digit it continues to check the next let2 in word2 
                            continue                            
                        elif let2==digit: #if the let2 is the digit, it breaks the modified word loop, and prints the word
                            print(word, end=" ")
                            printed = True #This word has printed, so the origional let loop needs to know 
                            break
        else:
            continue #If the letter or digit are not in the word, it continues


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        print()
        repeat = input("Try Again? (y/n): ")
        if repeat == "y":
            continue
        elif repeat == "n":
            break
        else:
            continue

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()