weight = float(input('Weight: '))

while True:
    label = input('(L)bs or (K)g: ').upper()
    if label == 'K' or label == 'L':
        break

if label == 'K':
    weight = weight / 0.45
    label = 'pounds'
else:
    weight = 0.45 * weight
    label = 'Kg'

print(f'You are {weight} {label}')
