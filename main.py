import time
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
    ("Brute force", algorithm.brute_force),
    ("Greedy first", algorithm.greedy_first),
    ("Dynamic programming", algorithm.dynamic_programming),
]

VALID_DNA_CHARS = {"A", "C", "G", "T"}

def analysis(method: Callable[[str, str], conf.Result], test_cases: tuple[str, str]):
    dna1 = test_cases[0]
    dna2 = test_cases[1]
    start_time = time.perf_counter()
    print(f"Analysis start time: {start_time}\nDNA1: {dna1}\nDNA2: {dna2}")
    analysis_result = method(dna1, dna2)
    end_time = time.perf_counter()
    print(f"Analysis end time: {end_time}")
    analysis_result.time_taken = (end_time - start_time) * 1000
    return analysis_result


def is_valid_dna_string(value: str) -> bool:
    return all(char in VALID_DNA_CHARS for char in value)


def get_custom_dna_pair() -> tuple[str, str]:
    while True:
        dna1 = input("Enter first DNA string (A/C/G/T only): ").strip().upper()
        dna2 = input("Enter second DNA string (A/C/G/T only): ").strip().upper()
        if is_valid_dna_string(dna1) and is_valid_dna_string(dna2):
            return dna1, dna2
        print("Invalid input. Use only A, C, G, T and make sure both strings are non-empty.\n")


def run_once() -> None:
    for case_name, dna_rand in test_cases:
        print(f"\n--- {case_name} ---")
        dna_rand_result = (dna_rand(), dna_rand())
        solve(dna_rand_result)

def run_custom_once() -> None:
    dna_pair = get_custom_dna_pair()
    print("\n--- Custom DNA Strings ---")
    solve(dna_pair)

def solve(dna_pair):
    for method_name, method in solution_methods:
        print(f"\n{method_name}:")
        solution = analysis(method, dna_pair)
        print(f"""
              ================================
              Best alignment score: {solution.best_score}
              Aligned DNA strings:
              {solution.aligned_dna1}
              {solution.aligned_dna2}
              Time taken: {solution.time_taken: 3f} milliseconds
              ================================
              """)

def main():
    while True:
        print("\nChoose input mode:")
        print("1. Random test cases")
        print("2. Custom DNA strings")
        mode = input("Select option (1/2): ").strip()

        if mode == "1":
            run_once()
        elif mode == "2":
            run_custom_once()
        else:
            print("Invalid option. Please select 1 or 2.")
            continue

        should_continue = input("Run again? (y/n): ").strip().lower()
        if should_continue not in {"y", "yes"}:
            print("Exiting app.")
            break


if __name__ == "__main__":
    main()