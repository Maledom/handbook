a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
c = float(input().replace(',', '.'))
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c == 0:
    print('0.00')
elif a == 0 and b != 0 and c != 0:
    print(f'{-c / b:.2f}')
elif a == 0 and b == 0 and c != 0:
    print('No solution')
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print('No solution')
    elif D == 0:
        if a == 0:
            print(f'{-c / b:.2f}')
        else:
            print(f'{-b / (2 * a):.2f}')
    elif D > 0:
        if a == 0:
            print(f'{-c / b:.2f}')
        else:
            x1 = (-b + D**(0.5)) / (2 * a)
            x2 = (-b - D**(0.5)) / (2 * a)
            if x1 > x2:
                print(f'{x2:.2f} {x1:.2f}')
            else:
                print(f'{x1:.2f} {x2:.2f}')
