"""reverse(data) - շրջում է data-ն հակառակ դասավորությամբ"""

def reverse_v1(data):
    """reverses given data

    """
    data = data[::-1]
    return data


data = ("hi", "bye", "hey")
print(reverse_v1(data))



def reverse_v2(data):
    """reverses given data

    """
    new_data = []
    i = len(data) - 1
    while i >= 0:
        new_data.append(data[i])
        i -= 1 
    return new_data


data = [8, 9, 10]
print(reverse_v2(data))
