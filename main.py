import time
import data.dna_str as dna
import logic.brute_force as bf

test_cases = [
        ("Shortest Random DNAs", dna.shortestDna),
        ("Short Random DNAs", dna.shortDna),
        # ("Long Random DNAs", dna.longDna),
        # ("Longer Random DNAs", dna.longerDna),
        # ("Longest Random DNAs", dna.longestDna)
    ]

for case_name, dna_rand in test_cases:
        print(f"\n--- {case_name} ---")
        dna1 = dna_rand()
        dna2 = dna_rand() 
        start_time = time.perf_counter()
        print(f"Analysis start time: {start_time}\nDNA1: {dna1}\nDNA2: {dna2}")
        best_score, aligned1, aligned2 = bf.brute_force(dna1, dna2)
        end_time = time.perf_counter()
        print(f"Analysis end time: {end_time}")
        
        print(f"""
              Best alignment score: {best_score}
              Aligned DNA strings:
              {aligned1}
              {aligned2}
              Time taken: {(end_time - start_time) * 1000: .3f} milliseconds
              """)