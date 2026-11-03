sungai_dunia = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'kapuas': 'indonesia'
}

# Loop pertama: mencetak kalimat
print("Informasi Aliran Sungai:")
for sungai, negara in sungai_dunia.items():
    print(f"Sungai {sungai.title()} mengalir melewati {negara.title()}.")

# Loop kedua: hanya mencetak nama sungai (keys)
print("\nDaftar Sungai yang tercatat:")
for sungai in sungai_dunia.keys():
    print(f"- Sungai {sungai.title()}")

# Loop ketiga: hanya mencetak nama negara (values)
print("\nDaftar Negara yang dilewati:")
for negara in sungai_dunia.values():
    print(f"- {negara.title()}")