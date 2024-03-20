# Lists comprehensions
numbers=[n for n in range(0,21)]
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

odd_num=[2*n+1 for n in range(0,10)]
print(odd_num)

# Slicing lists
letters="abcdefghijklmnopqrstu"
print(letters[1:3])
print(letters[-4:])
print(letters[:3])
print(letters[0:5:2])

abc=letters[:]
print(abc)