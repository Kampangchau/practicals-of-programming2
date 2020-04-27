import random
print(random.randint(5, 20))  # line 1 the smallest number is 5, the largest is 20.
print(random.randrange(3, 10, 2))  # line 2 the smallest is 3, the largest is 9.
# line 2 could not have produced a 4, because the step is 2.
print(random.uniform(2.5, 5.5))  # line 3 the smallest is 2.500000000000000. the largest is 5.500000000000000.