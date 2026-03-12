import time
import data.dna_str as dna
import logic.brute_force as bf
import logic.needleman_wunsch as nw

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

# Bug found: brute_force is computationally infeasible for longer strings due to
# exponential growth in the number of position combinations. For S1 (19 chars)
# and S2 (15 chars) below, the Needleman-Wunsch dynamic programming algorithm
# is used instead, which runs in O(n*m) time and memory.
specific_cases = [
    ("Specific Strings: S1=ACGTACGTACGTACGTTTT, S2=ACGTACGTACGTACG",
     "ACGTACGTACGTACGTTTT", "ACGTACGTACGTACG"),
]

for case_name, dna1, dna2 in specific_cases:
        print(f"\n--- {case_name} ---")
        start_time = time.perf_counter()
        print(f"Analysis start time: {start_time}\nDNA1: {dna1}\nDNA2: {dna2}")
        best_score, aligned1, aligned2 = nw.needleman_wunsch(dna1, dna2)
        end_time = time.perf_counter()
        print(f"Analysis end time: {end_time}")

        print(f"""
              Best alignment score: {best_score}
              Aligned DNA strings:
              {aligned1}
              {aligned2}
              Time taken: {(end_time - start_time) * 1000: .3f} milliseconds
              """)