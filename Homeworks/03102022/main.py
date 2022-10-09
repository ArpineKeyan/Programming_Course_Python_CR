#Իրականացնել պարզագույն բառարան, որը ֆայլից կկարդա բառերի համախումբ՝ անգերեն-հայերի բառերի թարգմանությամբ։
#Բառերը կարող են լինել Python keyword-ներ, statement-ներ և այլ համակարգչային գիտությանը վերաբերվող բառեր։
#Օբյեկտը, որի մեջ պետք է պահեք բառերը, կարող է լինել dictionary։

user_input = input('Please enter your Python keyword: ')
with open("eng_arm_dict.txt", mode="r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        if user_input in line:
            print(line)
            break
        else:
            print('That keyword doesn\'t exist in our dictionary.')
            break



#Տրված է հետևյալ ֆունկցիան
#   def myfunc(alist):
#    . . . . return len(alist)
#dis module-ի օգնությամբ դուրս բերել բայթ կոդի ներկայացումը և նկարագրել բոլոր դաշտերը (Python byte-code)։

def myfunc(alist):
    return len(alist)

from dis import dis
print(dis(myfunc))

# 24           0 LOAD_GLOBAL              0 (len)
#tells Python to look up the global object
# referenced by the name at index 0 of co_names
# (which is the print function) and push it onto
# the evaluation stack


#              2 LOAD_FAST                0 (alist)
#the LOAD_FAST takes the value as the argument

#              4 CALL_FUNCTION            1
#tells Python to call a function;
# it will need to pop one positional argument
# off the stack, then the new top-of-stack
# will be the function to call.

#              6 RETURN_VALUE
#the RETURN_VALUE returns the result

#None
