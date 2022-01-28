from pathlib import Path


def fasta_from_string(fasta_string: str):
    # TODO properly filter line.startswith(';'),
    #  current implementation only respects the customary first line ;

    sequences = [seq for seq in fasta_string.split('>') if not (seq == '' or seq.startswith(';'))]
    data = {}
    for seq in sequences:
        split_data = seq.split()
        label = split_data[0]
        sequence = ''.join(split_data[1:])

        data[label] = sequence

    return data


def fasta_from_path(fasta_path: Path):
    with fasta_path.open() as fasta:
        fasta_from_string(fasta.read())


if __name__ == '__main__':
    sample_data = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""
    print(fasta_from_string(sample_data))
