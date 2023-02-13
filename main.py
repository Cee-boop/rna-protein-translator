with open(file='data.txt') as file:
    data = file.read()
    protein_alphabet = "acdefghiklmnpqrstvwy".upper()
    rna_codon_table = {}

    with open(file='table.txt') as cache:
        sample_table = cache.read().split("\n")
        for entry in sample_table:
            key, value = entry.split(" ")
            rna_codon_table[key] = value

    start = 0
    protein_string = ""
    for end in range(0, len(data) + 3, 3):
        sub_string = data[start:end]
        if sub_string and rna_codon_table[sub_string] == "Stop":
            break
        if sub_string:
            protein_string += rna_codon_table[sub_string]

        start = end

    print(protein_string)
