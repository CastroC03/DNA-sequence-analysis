def compare_sequences(seq1, seq2):
    differences = 0

    for a, b in zip(seq1, seq2):
        if a != b:
            differences += 1

    similarity = (1 - differences / min(len(seq1), len(seq2))) * 100

    return differences, similarity