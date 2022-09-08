"""
Write a program that works with a text file. The aim of the program is to read a
text from the text file and analyze it. Specifically it should count and print:
1.the number of words
2.the number of letters
3.the number of sentences
4.the most used letter in a text
5.the most used word in a text
For example if out text file contains this text:
“Hello from Python world”
the program should give the following output:
Words: 4
Letters: 15 (special characters and space are not counted)
Sentences: 1
Letter frequency: o (both o and l are used 3 times so any of the letters is
considered as a right answer)
Word frequency: 0 (there is no word that is used more than once)
The result should be kept in a separate text file.
"""

with open("Sample_text.txt", "r") as file1:
    text = file1.readlines()
#print(text)

def word_count(text):
    #numbers are also considered as separate words
    whole_text = []
    for item in text:
        whole_text.append(item.strip("\n"))
        joined = "".join(whole_text)
    return len(joined.split()) - 1

def letter_count(text):
    whole_text = []
    for item in text:
        whole_text.append(item.strip("\n"))
        joined = "".join(whole_text)
    lst = []
    for i in joined:
        if i.isalpha():
            lst.append(i)
    #print(lst)
    return len(lst)

def sentence_count(text):
    #assuming that sentence ends with "." or "!" or "?"
    sentence_count = 0
    for item in text:                         #reading file content line by line
        for i in item:                        #reading line content
            if "." in i:
                sentence_count += 1
            elif "!" in i:
                sentence_count += 1
            elif "?" in i:
                sentence_count += 1
    return sentence_count


def most_used_letter_count(text):
    whole_text = []
    for item in text:
        whole_text.append(item.strip("\n"))
        joined = "".join(whole_text)
    lst = []
    for i in joined:
        if i.isalpha():
            lst.append(i)
    max_count = lst.count(lst[0])
    elm = lst[0]
    for i in range(1, len(lst)):
        if max_count < lst.count(lst[i]):
            max_count = lst.count(lst[i])
            elm = lst[i]
    return lst[i]

def most_used_word_count(text):
    #numbers are also considered as separate words
    whole_text = []
    for item in text:
        whole_text.append(item.strip("\n"))
        joined = "".join(whole_text)
    lst_joined = joined.split()
    max_count = lst_joined.count(lst_joined[0])
    elm = lst_joined[0]
    for i in range(1, len(lst_joined)):
        if max_count < lst_joined.count(lst_joined[i]):
            max_count = lst_joined.count(lst_joined[i])
            elm = lst_joined[i]

    #print(max_count)
    #print(elm)
    return len(joined.split()) - 1


#print(f"Sentences: {sentence_count(text)}.")
#print(f"Words: {word_count(text)}.")
#print(f"Letters: {letter_count(text)}.")
#print(f"Letter frequency: {most_used_letter_count(text)}.")
#print(f"Word frequency: {most_used_word_count(text)}.")

sentences = f"Sentences: {sentence_count(text)}."
words = f"Words: {word_count(text)}."
letters = f"Letters: {letter_count(text)}."
letter_freq = f"Letter frequency: {most_used_letter_count(text)}."
word_freq = f"Word frequency: {most_used_word_count(text)}."


with open("The_summary.txt", "w") as file2:
    file2.write(sentences)
    file2.write('\n')
    file2.write(words)
    file2.write('\n')
    file2.write(letters)
    file2.write('\n')
    file2.write(letter_freq)
    file2.write('\n')
    file2.write(word_freq)


