angka_ordinal = list(range(1, 10))

for angka in angka_ordinal:
    if angka == 1:
        print(f"{angka}st")
    elif angka == 2:
        print(f"{angka}nd")
    elif angka == 3:
        print(f"{angka}rd")
    else:
        print(f"{angka}th")