# Jan 25 warmup
import math

#   Write a function that takes 1 string as an argument and returns True if the string starts with "secret" and False otherwise
def start_with_secret(string):
    return string.startswith('secret')

#  Write a function that takes in an array/list of strings and returns True if ANY string starts with "secret" and False otherwise
def start_w_secret_array(strings):
    for string in strings:
        if string.startswith('secret'):
            return True
    return False

#  Write a function that takes in a number and return True if the number is prime (only divisible by 1 and itself) and False otherwise
def prime_number(number):
    for i in range(2, math.ceil(number/2)):
        if number % i == 0:
            return False
    return True

#  Write a function that given an array of numbers, where each number represents the price of a stock each day: 
#      return the maximum profit (or smallest loss) a stock trader could achieve by buying the stock on ONE day and selling on ONE other day



# test 
print(start_with_secret('secret dhfaghegah;ghegag'))
print(start_with_secret('Esecret dhfaghegah;ghegag'))

print(start_w_secret_array(['sdsecret dhfaghegah;ghegag','esecret dhfaghegah;ghegag','secret dhfaghegah;ghegag','rsecret dhfaghegah;ghegag']))
print(start_w_secret_array(['sdsecret dhfaghegah;ghegag','esecret dhfaghegah;ghegag','tsecret dhfaghegah;ghegag','rsecret dhfaghegah;ghegag']))

print(prime_number(3))
print(prime_number(13))
print(prime_number(30))
print(prime_number(8))
print(prime_number(11))