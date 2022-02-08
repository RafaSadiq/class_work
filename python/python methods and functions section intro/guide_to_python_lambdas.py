# full_name = lambda first, last: f'{first} {last}'


# def greeting(name):
#   print(f'Hi there {name}')


# greeting(full_name('Kristine', 'Hudgens'))



# In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

# Example: If you pass in the name "Jordan", it should return "Hi, Jordan".


def greeting(answer):
    print(f'the sum of 3 + 4 is {answer}')
    
sum_nums = lambda num_one, num_two: num_one + num_two

greeting(sum_nums(2,5))