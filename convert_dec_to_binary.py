#convert pos integers
def convertToBinary(n):
    # Function to print binary number for the input decimal using recursion
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')
# convert decimal fraction:
def fraction(num, digit):
    product = num
    binary = 0
    count = 0
    print('.', end = '')
    while product != 0.0 and count < digit:
        product = product*2
        if product >= 1:
            binary = 1
            product = product - 1
        else:
            binary = 0
        count += 1
        print(binary, end = '')

#convert real number:
def real(num):
    integer = int(num)
    frac = num - integer
    if frac == 0:
        convertToBinary(integer)
    else:
        ask = input("Do you wish to limit your digits after decimal? Y/N\n")
        try:
            if ask == "Y" or ask == "y":
                digit = int(input("Enter the number of digits you want to see after the decimal: "))
            else:
                digit = 10**10
        except:
            print("Your input is invalid and digit range considered 10**10")
            digit = 10**10
        convertToBinary(integer)
        fraction(frac, digit)

dec = float(input("Enter real decimal number to convert into binary: "))
real(dec)
print()

