import time
from collections.abc import Callable

import streamlit as st

import data.dna_str as dna
import logic.algorithm as algorithm
import logic.config as conf

VALID_DNA_CHARS = {"A", "C", "G", "T"}

TEST_CASES: list[tuple[str, Callable[[], str]]] = [
    ("Shortest Random DNAs", dna.shortestDna),
    ("Short Random DNAs", dna.shortDna),
    ("Long Random DNAs", dna.longDna),
    ("Longer Random DNAs", dna.longerDna),
    ("Longest Random DNAs", dna.longestDna),
]

SOLUTION_METHODS: list[tuple[str, Callable[[str, str], conf.Result]]] = [
    ("Brute force", algorithm.brute_force),
    ("Greedy first", algorithm.greedy_first),
    ("Dynamic programming", algorithm.dynamic_programming),
]


def is_valid_dna_string(value: str) -> bool:
    return bool(value) and all(char in VALID_DNA_CHARS for char in value)


def analyze(method: Callable[[str, str], conf.Result], dna_pair: tuple[str, str]) -> conf.Result:
    dna1, dna2 = dna_pair
    start_time = time.perf_counter()
    result = method(dna1, dna2)
    end_time = time.perf_counter()
    result.time_taken = (end_time - start_time) * 1000
    return result


def build_random_pair(case_name: str) -> tuple[str, str]:
    for label, generator in TEST_CASES:
        if label == case_name:
            return generator(), generator()
    return dna.shortDna(), dna.shortDna()


def render_result(method_name: str, result: conf.Result) -> None:
    st.subheader(method_name)
    cols = st.columns(3)
    cols[0].metric("Best score", f"{result.best_score}")
    cols[1].metric("Time (ms)", f"{result.time_taken:.3f}")
    cols[2].metric("Alignment length", f"{len(result.aligned_dna1)}")

    st.code(f"{result.aligned_dna1}\n{result.aligned_dna2}", language="text")


def main() -> None:
    st.set_page_config(page_title="DNAlignUI", layout="wide")
    st.title("DNA Alignment")

    with st.sidebar:
        st.header("Input Settings")
        input_mode = st.radio("DNA Source", ["Random test cases", "Custom DNA strings"])
        dna_pair: tuple[str, str] = ("", "")
        match input_mode:
            case "Random test cases":
                selected_case = st.selectbox("Random case", [label for label, _ in TEST_CASES])
                dna_pair = build_random_pair(selected_case)

            case "Custom DNA strings":
                with st.sidebar:
                    st.subheader("Custom DNA Strings")
                    custom_dna1 = st.text_input("First DNA string (A/C/G/T only)", placeholder="A/C/G/T only")
                    custom_dna2 = st.text_input("Second DNA string (A/C/G/T only)", placeholder="A/C/G/T only")

                dna_pair = (custom_dna1.strip().upper(), custom_dna2.strip().upper())
                if not is_valid_dna_string(dna_pair[0]) or not is_valid_dna_string(dna_pair[1]):
                    st.error("Enter valid DNA strings")
                    return

        st.header("Algorithms")
        selected_methods = st.multiselect(
            "Run", [label for label, _ in SOLUTION_METHODS], default=[label for label, _ in SOLUTION_METHODS]
        )

        run = st.button("Run comparison", type="primary")

    if not run:
        st.info("Choose inputs")
        return

    if not selected_methods:
        st.warning("Pick at least one algorithm to run.")
        return

    st.divider()
    st.subheader("Inputs")
    st.code(f"{dna_pair[0]}\n{dna_pair[1]}", language="text")

    results: list[tuple[str, conf.Result]] = []
    for method_name, method in SOLUTION_METHODS:
        if method_name not in selected_methods:
            continue
        result = analyze(method, dna_pair)
        results.append((method_name, result))
        render_result(method_name, result)

    if len(results) > 1:
        st.divider()
        st.subheader("Comparison")

        score_data = []
        time_data = []
        for name, r in results:
            score_data.append({"Metric": "Best Score", "Algorithm": name, "Value": r.best_score})
            time_data.append({"Algorithm": name, "Time (ms)": round(r.time_taken or 0, 3)})

        col1, col2 = st.columns([2, 1])
        with col1:
            st.caption("Alignment Score")
            st.bar_chart(score_data, x="Metric", y="Value", color="Algorithm", stack=False)
        with col2:
            st.caption("Execution Time")
            st.bar_chart(time_data, x="Algorithm", y="Time (ms)")

        
if __name__ == "__main__":    
    main()