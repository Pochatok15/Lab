import random

def create_array(length):
    return [random.randint(0, 9) for _ in range(length)]

array1 = create_array(5)
array2 = create_array(7)


min_length = min(len(array1), len(array2))
array3 = [array1[i] + array2[i] for i in range(min_length)]


if len(array1) > min_length:
    array3 += array1[min_length:]
elif len(array2) > min_length:
    array3 += array2[min_length:]

print("зліва направо",array3)

if any(num > 10 for num in array3):
    reversed_array3 = list(reversed(array3))
    for num in reversed_array3:
        print(num)
else:
    for num in array3:
        print(num)
