"""
Իրականացնել map և filter ֆունկցիաները, որոնց միջոցով լուծել հետևյալ խնդիրները

գրել triple(data) ֆունկցիա, որը վերադարձնում է data-ի անդամների եռապատիկները պարունակող լիստ

իրականացնել map3(func, data1, data2, data3) ֆունկցիա, որը վերադարձնում է նոր լիստ,
որի մեջ ներառված են func-ի կանչի արդյունքները data1, data2 և data3-ի համապատասխան անդամների
անդամների վրա,

օրինակ, եթե ունենք sum(a, b, c) ֆունկցիան, որը վերադարձնում է a, b և c թվերի գումարը,
map(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]) կվերադարձնի [111, 222, 333]



իրականացնել map2(func, data1, data2) ֆունկցիա, դրա օգնությամբ գրել ծրագիր,
որը կտպի էկրանին նոր լիստ, որի i-րդ անդամը կլինի bases-ի i-րդ անդամը exp-ի i-րդ անդամով աստիճան
բարձրացրած, որտեղ
base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

def triple(data):
    """returns the list with 3rd powers of  items of given list
    """
    the_list = []
    for item in data:
        the_list.append(item**3)
    return the_list
#print(triple([3, 2, 5]))


def map3(func, data1, data2, data3):
    """returns the list of function call on arguments
    """
    generated_list = []  #list of elements from arguments
    final_list = []
    for index in range(len(data1)):
        generated_list.extend([[data1[index], data2[index], data3[index]]])
    #print(generated_list)
        
    for item in generated_list:    #list of elements after function call
        final_list.append(func(item))

    return final_list
#print("The list of elements after function call is: ", map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))



def map2(data1, data2):
    """returns a list [data1[i]**data2[i]
    """
    generated_list = []
    for i in  range(0, len(data1)):
        generated_list.append(data1[i]**data2[i])

    return generated_list


#base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(map2(base,exp))
