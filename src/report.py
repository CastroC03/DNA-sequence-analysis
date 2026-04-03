import os

def save_report(records, differences, similarity, mutations, silent, missense):
    os.makedirs("results", exist_ok=True)

    with open("results/resultados.txt", "w") as f:
        f.write("=== DNA ANALYSIS REPORT (FIRST 1000 BASES) ===\n\n")

        f.write("Sequences:\n")
        for r in records:
            f.write(f"- {r.id} | Length: {len(r.seq)}\n")

        f.write("\nComparison:\n")
        f.write(f"Differences: {differences}\n")
        f.write(f"Similarity (%): {similarity:.2f}\n")

        f.write("\nMutations:\n")
        for m in mutations:
            f.write(
                f"Position: {m['position']} | "
                f"{m['codon1']} -> {m['codon2']} | "
                f"{m['aa1']} -> {m['aa2']} | "
                f"{m['type']}\n"
            )

        f.write("\nSummary:\n")
        f.write(f"Silent: {silent}\n")
        f.write(f"Missense: {missense}\n")