from Bio import SeqIO

def load_sequences(file_path):
    records = list(SeqIO.parse(file_path, "fasta"))
    return records