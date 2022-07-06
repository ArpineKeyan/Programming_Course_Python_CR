#replace(source, old, new, count) ֆունկցիան, որը source տողի բոլոր old ենթատողերը փոխարինում է new ենթատողով

def replace(source, old, new, count):
    j = len(old)
    lst = []
    for i in range(len(source)):
        if source[i:j] == old and count > 0:
            lst.append(new)
            i = i + len(new) + len(old)
            count -= 1
        else:
            lst.append(source[i])
    return str("".join(lst))



string = "All of the projects will be peer reviewed. All. All. All."
old_substring = "All"
new_substring = "None"
count = 10

print(replace(string, old_substring, new_substring, count))