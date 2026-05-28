import os
import random

print("==================================================")
print("STAGE 1: RAW FASTQ SEQUENCE GENERATION")
print("==================================================")

output_dir = "../simulated_reads"
os.makedirs(output_dir, exist_ok=True)

# Define a segment of the E. coli genome we want to simulate
target_gene_sequence = "ATGTTTCGTTTAAACCAACTAATTGCAACCAAAGCCAAACGCACCGCACG"
# Low-quality sequencing adapter we want our QC step to catch and trim
illumina_adapter = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"

# Phred scores: 'I' represents high quality (Q40), '!' represents lowest quality (Q0)
high_quality_string = "I" * len(target_gene_sequence)
low_quality_string = "!" * len(illumina_adapter)

r1_path = f"{output_dir}/Ecoli_clinical_R1.fastq"
r2_path = f"{output_dir}/Ecoli_clinical_R2.fastq"

print("Simulating high-throughput paired-end reads...")

# Write forward and reverse mock sequencing outputs
with open(r1_path, "w") as r1, open(r2_path, "w") as r2:
    for i in range(100):  # Generating 100 high-depth reads
        # Forward Read (R1)
        r1.write(f"@ERR1234567.{i+1} HWI-ST123:1:1101:1234:5678 length=84\n")
        r1.write(f"{target_gene_sequence}{illumina_adapter}\n")
        r1.write("+\n")
        r1.write(f"{high_quality_string}{low_quality_string}\n")
        
        # Reverse Read (R2) - Complementary strand simulation
        r2.write(f"@ERR1234567.{i+1} HWI-ST123:1:1101:1234:5678 length=84\n")
        r2.write(f"{target_gene_sequence[::-1]}{illumina_adapter}\n")
        r2.write("+\n")
        r2.write(f"{high_quality_string}{low_quality_string}\n")

print(f"Success! Raw sequencing data generated locally.")
print(f"  * Forward Reads: {r1_path}")
print(f"  * Reverse Reads: {r2_path}")