from src.reader import load_sequences
from src.alignment import align_sequences
from src.basic_analysis import compare_sequences
from src.mutation_analysis import analyze_mutations
from src.visualization import plot_nucleotide_composition
from src.report import save_report

# Cargar datos
records = load_sequences("data/secuencia.fasta")

print("Número de secuencias:", len(records))

# Tomar fragmentos. En este caso, solo los primeros 1000 nucleótidos para análisis rápido
seq1 = records[0].seq[:1000]
seq2 = records[1].seq[:1000]

print("ID 1:", records[0].id)
print("ID 2:", records[1].id)

# Alineamiento
alignment = align_sequences(seq1, seq2)
print(alignment)

# Comparación
differences, similarity = compare_sequences(seq1, seq2)

print("Diferencias:", differences)
print("Similitud (%):", similarity)

# Mutaciones
mutations, silent, missense = analyze_mutations(seq1, seq2)

print("\n--- MUTACIONES ---")
for m in mutations:
    print(m)

print("\nResumen:")
print("Silenciosas:", silent)
print("Missense:", missense)


def count_bases(seq):
    bases = ["A", "T", "G", "C"]
    return {base: seq.count(base) for base in bases}

# Conteo de bases (usa la primera secuencia)
count = count_bases(seq1)

# Generar gráfica
plot_nucleotide_composition(count)

# Guardar reporte
save_report(records, differences, similarity, mutations, silent, missense)