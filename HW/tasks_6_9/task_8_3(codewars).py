""" Замена ДЗ № 8_3 (работа с функциями)."""


"""Your task is to make a function that can take any non-negative integer
as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number."""


def max_number(number):
    return int(''.join(sorted(str(number), reverse=True)))


print(max_number(3271))


""" An abundant number or excessive number is a number 
for which the sum of its proper divisors is greater than the number itself.
The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
Derive function abundantNumber(num)/abundant_number(num) 
which returns true/True/.true. if num is abundant, false/False/.false. if not."""


# first solution
def abundant_number(num):
    divisors_sum = 0
    for n in range(1, num):
        if num % n == 0:
            divisors_sum += n
    return divisors_sum > num


# # second solution
# def abundant_number(num):
#     divisors_sum = sum([divisor for divisor in range(1, num) if not num % divisor])
#     return divisors_sum > num


print(abundant_number(12))
