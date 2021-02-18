#Takes a floating point number as input (i.e. n) and return the binary for that number.
import math
import array

def convert_float_binary(n):
    left_math = math.trunc(n)
    right_math = float(n - left_math)
    loop_control = 0
    bin_rep = []

    # Calculate on the left side
    temp = 0
    while left_math >= 1:
        temp = left_math % 2
        if temp == 1:
            left_math = math.trunc(left_math / 2)
        else:
            left_math = left_math / 2
        bin_rep.append(str(math.trunc(temp)))

    bin_rep.append(str('.'))

    # Calculate on the right side
    # Will exit loop after 5 decimal places
    temp = 0
    while right_math <= 1:
        temp = right_math * 2
        if temp < 1:
            right_math = temp
            temp = 0
        elif temp > 1:
            right_math = temp - math.trunc(temp)
            temp = 1
        else:
            temp = 1
            bin_rep.append(str(math.trunc(temp)))
            break
        bin_rep.append(str(math.trunc(temp)))

        if loop_control == 5:
            break
        else:
            loop_control += 1

    print("The Binary representation of the number is : ", ''.join(bin_rep))


#Based on the floating point number generates 1 if the number is negative and 0 if the number is positive.
def calculate_sign_bit(n):
    if n > 1:
        sign = 0
    else:
        sign = 1

    print("The sign is negative with a sign bit : ", sign)


#Takes the binary for the floating-point number and returns the mantissa/fraction and exponent.
def normalize_binary(n):
    mantissa = n
    exp = 0
    while mantissa > 1:
        temp = mantissa / 10
        if temp > 1:
            mantissa = temp
            exp += 1
        else:
            break

    flag = False
    after_dec = 0
    places_after_decimal = str(n)
    for v in places_after_decimal:
        if flag:
            after_dec += 1
        elif v == '.':
            flag = True

    mant_rep = str(mantissa)
    flag = False
    temp = []
    for x in mant_rep:
        if flag:
            temp.append(x)
        elif x == '.':
            flag = True

    mant_final = ''.join(temp)[0:(after_dec + exp)]

    print("Mantissa: ", mant_final, " and biased exponent is : ", exp)


#Takes the exponent from normalized representation and returns the binary of the biased exponenet.
#def calculate_exponent_biased(n):


#Takes the floating point number as an input and generates the IEEE 754 representation.
#def IEEE754_rep(float_number):


#given a binary number in IEEE 754 format it should be able to convert to a floating-point number.
#In this case, make sure that your top-level function name is ieee_754_to_float.
#def ieee_754_to_float(n):


if __name__ == '__main__':

    convert_float_binary(85.125)
    # Output: The Binary representation of the number is : 1010101.001

    calculate_sign_bit(-85.125)
    # Output: The sign is negative with a sign bit : 1

    normalize_binary(1010101.001)
    # Output: Mantissa: 010101001 exponent: 6

    ##calculate_exponent_biased(6)
    # Output: The exponent is : 6 and biased exponent is : 10000101

    ##IEEE754_rep(85.125)
    # Output: The IEEE 754 single precision for 85.125 is : 0-10000101-01010100 100000000000000

    ##ieee_754_to_float('01000010101010100100000000000000')
    # Output: The float number for the given binary is 85.125



