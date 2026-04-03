from Bio.Align import PairwiseAligner

def align_sequences(seq1, seq2):
    aligner = PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    return alignments[0]