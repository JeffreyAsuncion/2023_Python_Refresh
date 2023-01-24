# Takes a string and replaces 
# the words in the string with another word


def replace_word():
    
    str = "Hi guys, My Name is Jeff, and hi hi hi hi hi hi"
    word_to_replace = input("Enter the word to replace : ")
    word_replacement = input("Enter the word replacement : ")
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()