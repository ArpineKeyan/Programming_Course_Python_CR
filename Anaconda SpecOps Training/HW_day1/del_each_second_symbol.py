"""
Իրականացնել ֆունկցիա, որը կհեռացնի ստացված տողի (string) ամեն երրորդ սիմվոլը։

"""

string = "12121212121212121212"
lst = []
for i in range(0, len(string), 2):
    lst.append(string[i])
print("".join(lst))
