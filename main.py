
#Adds the amount of words in a text
def count_words(text):
    words = len(text.split())
    return words

#Counts occurrance of each letter in a text
def count_letters(text):
    word_array = text.split()
    letter_count = {}
    for word in word_array:
        for letter in word:
            if(letter.isalpha() == False):
                if("undefined_letters" in letter_count.keys()):
                    letter_count["undefined_letters"] += 1
                    continue
                elif("undefined_letters" not in letter_count.keys()):
                    letter_count["undefined_letters"] = 1
                    continue
            if(letter.lower() not in letter_count.keys()):
                letter_count[letter.lower()] = 1
            elif(letter.lower() in letter_count.keys()):
                letter_count[letter.lower()] += 1
    
    return letter_count

def main():
    #opens the file and counts words
    file_to_open = "books/frankenstein.txt"
    with open(file_to_open) as f:
        file_contents = f.read()
        sorted_list = []
        print("--- Begin report of " + file_to_open + " ---")
        print(str(count_words(file_contents)) + " words found in the document")
        print("")
        letter_count = count_letters(file_contents)
        sorted_list = list((count_letters(file_contents)).keys())
        sorted_list.sort()
        for letter in sorted_list:
            print("The '" + letter + "'character was found " + str(letter_count[letter]) + " times")
        print("--- End report ---")
main()