y1 = int(input('Pass1: '))
y2 = int(input('Pass2: '))
x1, x2 = 1, 2

def decrypt_func(text):
    #convert ASCII to char, concatenate them
    return ''.join([chr(int(text[i:i+3])) for i in range(0, len(text), 3)])

#check if y1, y2 start with '0'
is_zero = (input('Was there a zero at the start? (y/n): ')).lower()

is_zero = True if is_zero == 'y' else False

#converting var to mathematical form
m = y2-y1
c = int(y1 - m*x1)
plain_text = str(c)

plain_text = f"0{plain_text}" if is_zero else plain_text

plain_text = decrypt_func(plain_text)
print(f'Slope (m): {m}')
print(f'Original Text: {plain_text}')

