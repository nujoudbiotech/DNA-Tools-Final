# 🧬 DNA-Tools - Tool 3 Final - by Nujoud

CODON_TABLE = {
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'UAU':'Y', 'UAC':'Y', 'UAA':'*', 'UAG':'*',
    'UGU':'C', 'UGC':'C', 'UGA':'*', 'UGG':'W',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

def reverse_complement(dna):
    comp = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join(comp.get(b,b) for b in reversed(dna.upper()))

def transcribe(dna):
    return dna.upper().replace('T','U')

def translate(rna):
    rna = rna.upper()
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3: break
        aa = CODON_TABLE.get(codon,'X')
        if aa == '*':
            protein += '*'
            break
        protein += aa
    return protein

# --- Test ---
if __name__ == "__main__":
    with open("sample.fasta") as f:
        lines = [l.strip() for l in f if not l.startswith(">") and l.strip()]
        dna = "".join(lines)

    rna = transcribe(dna)
    prot = translate(rna)

    print(f"Original: {dna[:30]}...")
    print(f"Rev Comp: {reverse_complement(dna)[:30]}...")
    print(f"RNA: {rna[:30]}...")
    print(f"Protein: {prot[:50]}...")
    print(f"Length: {len(prot)} aa")