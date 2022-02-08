print('\n')
print('How to Create and Write to a File in Python')
print('\n')

file_builder = open("python().py", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")


# file_builder.write("Hey, I'm in a file!")

file_builder.close()