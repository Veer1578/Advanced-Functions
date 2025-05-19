num1 = [1, 2, 3]
num2 = [4, 5, 6]
result = map(lambda x, y: x + y ,num1, num2)
print(f'The addition of the 2 lists is {list(result)}')

num = [1, 2, 3, 4, 5]
def square(n):
    return n**2
ans = map(square, num)
print(f'Squares of first 5 numbers are {list(ans)}')