"""
Իրականացնել strmove() ֆունկցիան, որը տրված տողը ցիկլիկ տեղաշարժում է
դեպի աջ տրված քանակով։ Օրինակ, strmove(“hello”, 2);
կտեղաշարժի “hello”-ն 2 դիրքով դեպի աջ և կստանա “lohel”։
"""

def strmove(string, count):
    moved_string = string[count + 1::] + string[:count + 1]
    return moved_string


print(strmove("hello", 2))    
