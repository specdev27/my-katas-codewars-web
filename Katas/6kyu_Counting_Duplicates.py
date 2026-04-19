#6 kyu kata...

#Take and string value and count how many letters or numbers apears more than one time in the string, and then return the number of characters that occurs more than one time. For example, if 'a' appear 3 times, the output will be one, because only one character repeats.

def duplicate_count(text):

    text = text.lower()

    characters_repeated = []

    for i in text:
        if text.count(i) >= 2:
            if i not in characters_repeated:
                characters_repeated.append(i)
            
            else:
                pass

        else:
            pass
    
    return characters_repeated

key = duplicate_count("Indivisibilities")

print(key)