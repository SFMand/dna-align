from dataclasses import dataclass
from typing import LiteralString

MATCH = 0 # gamma
GAP_PENALTY = 1 # alpha
MISMATCH_PENALTY = 2 # beta

@dataclass
class Result:
    best_score: int
    aligned_dna1: LiteralString
    aligned_dna2: LiteralString
    time_taken: float | None