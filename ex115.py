def function(word):
    begin = ['a', 'e', 'i', 'o', 'u']
    if word[0] in begin:
        return word + 'way'

    else:
        length = len(word)
        x=0
        while x == 0:
            for letter in range(0,length):
                if word[letter] in begin:
                    x += 1
                    break

        frontletters = word[0:letter]
        lastletters = word[letter:]
        return lastletters + frontletters + 'ay'
