def str_rev(word):
    old_word = word
    word = word.lower()

    new_str = ""
    for letter in word:
        new_str = letter + new_str

    new_str = new_str.capitalize()
    print(old_word + " : " + str(new_str))


str_rev('Desserts')
str_rev("Live") 
str_rev('Pals')
str_rev('God')
str_rev('Raw')
