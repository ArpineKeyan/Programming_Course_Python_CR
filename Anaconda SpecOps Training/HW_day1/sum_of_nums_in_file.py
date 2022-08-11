"""
Տրված ֆայլում պարունակվում են թվեր։
Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը
"""

_sum = 0
with open ("text_with_nums.txt", "r") as file:       #opening the file to read
    while True:                                      #while there are lines to read
        line = file.readline()                       #reading line
        splitted_line = line.split(" ")              #splitting lines to items to get numbers separated
        for item in splitted_line:                   #for each item checking if it's numeric'
            if item.isnumeric():
                _sum += int(item)                    #counting the sum


        if not line:                                 #if not line, then exit file
            break


print(_sum)


