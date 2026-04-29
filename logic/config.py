from dataclasses import dataclass
from typing import LiteralString

GAP_PENALTY = 1
MISMATCH_PENALTY = 2

@dataclass
class Result:
    best_score: int
    aligned_dna1: LiteralString
    aligned_dna2: LiteralString
    time_taken: float | None