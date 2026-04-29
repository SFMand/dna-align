import time
from typing import LiteralString
import data.dna_str as dna
import logic.algorithm as algorithm
import logic.config as conf
from collections.abc import Callable
test_cases = [
        ("Shortest Random DNAs", dna.shortestDna),
        ("Short Random DNAs", dna.shortDna),
        ("Long Random DNAs", dna.longDna),
        ("Longer Random DNAs", dna.longerDna),
        ("Longest Random DNAs", dna.longestDna)
    ]

solution_methods = [
    # ("Brute force", algorithm.brute_force),
    ("Greedy first", algorithm.greedy_first),
    ("Dynamic programming", algorithm.dynamic_programming),
]

def analysis(method: Callable[[LiteralString, LiteralString], conf.Result], test_case: Callable[[], LiteralString]):
    dna1 = test_case()
    dna2 = test_case() 
    start_time = time.perf_counter()
    print(f"Analysis start time: {start_time}\nDNA1: {dna1}\nDNA2: {dna2}")
    analysis_result = method(dna1, dna2)
    end_time = time.perf_counter()
    print(f"Analysis end time: {end_time}")
    analysis_result.time_taken = (end_time - start_time) * 1000
    return analysis_result



for case_name, dna_rand in test_cases:
    print(f"\n--- {case_name} ---")
    for method_name, method in solution_methods:
        print(f"\n{method_name}:")
        try:
            solution = analysis(method, dna_rand)
        except NotImplementedError:
            print("Not implemented yet")
            continue

        print(f"""
              ================================
              Best alignment score: {solution.best_score}
              Aligned DNA strings:
              {solution.aligned_dna1}
              {solution.aligned_dna2}
              Time taken: {solution.time_taken: 3f} milliseconds
              ================================
              """)