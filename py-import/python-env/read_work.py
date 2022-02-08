print('\n')
print('Reading and Working with File Data in Python')
print('\n')

def get_file_contents(filename):
    queried_file = open(filename, 'r')

    if queried_file.mode == 'r':
        return queried_file.read()


content = get_file_contents('file-section/text_content.txt')

print(content)

print("Number of words", len(content.split()))