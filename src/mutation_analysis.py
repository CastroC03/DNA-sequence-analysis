def analyze_mutations(seq1, seq2):
    silent = 0
    missense = 0

    results = []

    for i in range(0, min(len(seq1), len(seq2)), 3):
        codon1 = seq1[i:i+3]
        codon2 = seq2[i:i+3]

        if len(codon1) < 3 or len(codon2) < 3:
            continue

        if codon1 != codon2:
            aa1 = codon1.translate()
            aa2 = codon2.translate()

            mutation_type = "silent" if aa1 == aa2 else "missense"

            if mutation_type == "silent":
                silent += 1
            else:
                missense += 1

            results.append({
                "position": i,
                "codon1": str(codon1),
                "codon2": str(codon2),
                "aa1": str(aa1),
                "aa2": str(aa2),
                "type": mutation_type
            })

    return results, silent, missense