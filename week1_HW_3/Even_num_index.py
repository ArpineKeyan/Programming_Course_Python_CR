"""
4. Գրել ծրագիր, որը տպում է տրված ծանգվածի զույգ էլեմենտների ինդեքսները:
"""

given_list = [1, 2, 5, 7, 8, 99, 44, 126]

index_list = []

for index in range(len(given_list)):

    if given_list[index] % 2 == 0:
        index_list.append(index)

print("The indexes with even numbers in list are: ", index_list)

