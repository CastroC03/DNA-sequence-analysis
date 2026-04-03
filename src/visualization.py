import matplotlib.pyplot as plt
import os

def plot_nucleotide_composition(count, output_path="results/grafica_composicion.png"):
    os.makedirs("results", exist_ok=True)

    plt.style.use('ggplot')

    labels = list(count.keys())
    values = list(count.values())
    colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']

    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color=colors)

    plt.title("Nucleotide Composition", fontsize=14, fontweight='bold')
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()