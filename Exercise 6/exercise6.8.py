hewan_1 = {'jenis': 'kucing persia', 'pemilik': 'ndaru'}
hewan_2 = {'jenis': 'anjing golden', 'pemilik': 'ayu'}
hewan_3 = {'jenis': 'burung beo', 'pemilik': 'bima'}

hewan_peliharaan = [hewan_1, hewan_2, hewan_3]

for hewan in hewan_peliharaan:
    print(f"Hewan peliharaan berjenis {hewan['jenis'].title()} ini dimiliki oleh {hewan['pemilik'].title()}.")