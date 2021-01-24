def cleanWord(word):
    if len(word) == 1:
        return word

    elif word[0] == word[1]:
        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])


print(cleanWord("hooooww aaarre yooouuuuuu"))

# input ==> hooooww aaarre yooouuuuuu
# output ==>  how are you
