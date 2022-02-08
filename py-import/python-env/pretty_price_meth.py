print('\n')
print('Build a Pretty Price Method in Python')
print('\n')

def pretty_price(gross, ext):
    if isinstance(ext, int):
        ext = ext * 0.01

    return int(gross) + ext


print(pretty_price(3.20, 99))
# print(pretty_price(3.99, 0.20))
# print(pretty_price(3.20, .95))
# print(pretty_price(3, 95))
# print(pretty_price(3, 2))