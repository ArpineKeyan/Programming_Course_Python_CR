#given two integers which may be very long
#the task is to sum this integers
#this code covers the case of two positive integers only


a = 123456      #first integer
b = 987654      #secondd integer

lst_a = [int(num) for num in str(a)][::-1]   #getting list of first integer's digits in reversed order
lst_b = [int(num) for num in str(b)][::-1]   #getting list of second integer's digits in reversed order

if len(lst_a) >= len(lst_b):                 #comparing lenghts of integers
    shorter_lst, longer_lst = lst_b, lst_a
else:
    shorter_lst, longer_lst = lst_a, lst_b

     
_sum = ""                                    #empty string to gather digits in later
carry = 0                                    #carry is 0 if sum of digits is <=9 and 1 otherwise


#summing up digits one by one and gathering them inside _sum
for i in range(len(longer_lst)):    
    
    if i < len(shorter_lst):     
        sum_of_digits = shorter_lst[i] + longer_lst[i] + carry
    else:
        sum_of_digits = longer_lst[i] + carry

    if sum_of_digits > 9:
        carry = 1
        sum_of_digits -= 10
    else:
        carry = 0
    
    _sum += str(sum_of_digits)

#if a and b are of the same lenghth, then extra carry may remain,
#and if it is not 0, then it will be added to the string   
if carry != 0:
    _sum += str(carry)

    
print("the sum of given digits is:", _sum[::-1])
#the sum of given digits is: 1111110

#check cases
#a = 123456 b = 987654 -> 1111110
#a = 123456 b =  87654 ->  211110
    

