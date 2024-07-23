from random import randint

plain_text = input('Provide a piece of text: ')

#pick anything from 10^(n-1) until just before 10^n
def random_cal(n):
    return randint((10**(n-1)), ((10**n)-1))

#convert to ASCII, precceding with "0" if <100
def encrypt_magic(text):
    return ''.join(f'0{ord(i)}' if ord(i) < 100 else f'{ord(i)}' for i in text)

x1, x2 = 1, 2
c = encrypt_magic(plain_text)
#m is slope
m = random_cal(len(c))
y1 = (m * x1) + int(c)
y2 = (m * x2) + int(c)

if c[0] == '0':
    print('0 detected at the beginning')

print(f'Pass1 (y1): {y1}')
print(f'Pass2 (y2): {y2}')


