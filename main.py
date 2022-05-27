# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    open_file = open(filename, "r")
    read_file = open_file.read()
    read_file = read_file.split(" ")
    # [assignment] Add your code here 
    
    return read_file


def count_words():
    text = read_file_content("./story.txt")
    word_count = {}
    for word in text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
    # [assignment] Add your code here


print(count_words())