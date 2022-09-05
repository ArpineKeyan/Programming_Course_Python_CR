print("Hey there, do you want to compress or decompress your file?")
user_input = input("Please enter 'compress' or 'decompress' to continue: ")

with open("Sample_text.txt", "r") as file1:    #opening file for reading
    lines = file1.readlines()                  #reading file content into lines
    dict_of_words = {}                         #will keep here words:specific number /string size is greater than int size,
                                               #so replacing words with numbers will make file smaller
    index = 1
    for line in lines:
        for item in line.split():              #splitting words to make indexing for them
            dict_of_words[item] = index        #keeping words and related numbers in dict
            index += 1



if user_input == 'compress':                  #generating file in which strings are replaced with integers

    with open("Sample_text_compressed.txt", "w") as file2:
        for value in dict_of_words.values():
            file2.writelines(f'{value} ')


elif user_input == 'decompress':           #generating file in which integers replaced back with strings

    decomp_dict = {v: k for k, v in dict_of_words.items()}
    print(decomp_dict)

    with open("Sample_text_decompressed.txt", "w") as file3:
        for value in decomp_dict.values():
            file3.writelines(value)
            file3.writelines(" ")
