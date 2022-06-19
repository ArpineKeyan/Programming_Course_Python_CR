"""
Նյուտոնի մեթոդը խորանարդ արմատ հաշվելու համար հիմնված է հետևյալ քայլերի վրա.
եթե n-ը m թվի մոտարկված արմատն է, ապա մենք կարող ենք էլ ավելի բարելավել
մոտարկումը հետևայլ քայլով
                ((m / (n ** 2)) + (2 * n)) / 3
Այս բանաձևով ստեղծեք ֆունկցիա, որը հաշվում է թվի խորանարդ արմատը։
"""

def qubic_root(num):
    root = 1
    while not guessed(root, num):
        root = improve(root, num)
    return root

def guessed(root, target):
    if abs(root**3 - target) < pow(10, -3):
        return True
    else:
        return False

def improve(m, n):
    return ((m / (n ** 2)) + (2 * n)) / 3

print(qubic_root(1))
        
    
