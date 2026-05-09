from dataclasses import dataclass
from typing import LiteralString


MISMATCH_PENALTY = 2  # alpha
GAP_PENALTY = 1 # beta
MATCH = 0 # gamma

@dataclass
class Result:
    best_score: int | float
    aligned_dna1: LiteralString
    aligned_dna2: LiteralString
    time_taken: float | None