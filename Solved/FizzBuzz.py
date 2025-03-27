nums = input().split(" ")
first = int(nums[0])
second = int(nums[1])
for i in range(1, int(nums[-1])+1):
    if i % first == 0 and i % second == 0:
        print("FizzBuzz")
    elif i % first == 0:
        print('Fizz')
    elif i % second == 0:
        print("Buzz")
    else:
        print(i)