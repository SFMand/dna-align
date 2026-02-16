import time
import data.dna_str as dna
import logic.brute_force as bf

test_cases = [
        ("Shortest Random DNAs", dna.shortestDna),
        ("Short Random DNAs", dna.shortDna),
        ("Long Random DNAs", dna.longDna),
        ("Longer Random DNAs", dna.longerDna),
        ("Longest Random DNAs", dna.longestDna)
    ]

for case_name, dna_rand in test_cases:
        print(f"\n--- {case_name} ---")
        dna1 = dna_rand()
        dna2 = dna_rand() 
        start_time = time.time()
        print(f"Analysis start time: {start_time}\nDNA1: {dna1[:400]}\nDNA2: {dna2[:400]}")
        bf.brute_force(dna1, dna2)
        end_time = time.time()
        print(f"Analysis end time: {end_time}")
        print(f"Time taken: {end_time - start_time} seconds")
