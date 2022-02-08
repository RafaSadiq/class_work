# def full_name(first, last):
#       print(f'{first} {last}')


# full_name('Kristine', 'Hudgens')
# full_name(first = 'Kristine', last = 'Hudgens')
# full_name(last = 'Hudgens', first = 'Kristine')


# Coding Exercise

# Behind the scenes of the code test is a function called sequence that accepts 5 arguments: first, second, third, fourth, and fifth. Unfortunately, they are not in sequential order. Using named arguments, call the sequence function and pass in the 5 arguments, setting their values to 1, 2, 3, 4, 5 respectively.

def named_arguments_practice(sequence):
    sequence(first = 1, second = 2, third = 3, fourth = 4 , fifth = 5)