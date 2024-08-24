import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


generated_pass = []

num_letters = int(input("How much letters for your password: "))
for _ in range(num_letters):
    rand_let = random.choice(letters)
    generated_pass.append(rand_let)

num_numbers = int(input("How much numbers for your password: "))
for i in range(num_numbers):
    rand_num = random.choice(numbers)
    generated_pass.append(rand_num)

num_symbols = int(input("How much symbols for your password: "))
for _ in range(num_symbols):
    rand_symb = random.choice(symbols)
    generated_pass.append(rand_symb)


print(f"Initial pass: {''.join(generated_pass)}")
shuffle(generated_pass)
print(f"After using shuffle function: {''.join(generated_pass)}")


# for i in generated_pass:
#     print(i, end="")

