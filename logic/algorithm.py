from itertools import combinations
from logic.config import Result
from logic.config import GAP_PENALTY, MISMATCH_PENALTY, MATCH

def brute_force(dna1, dna2):
	len1 = len(dna1)
	len2 = len(dna2)
	best_score = float('inf') # infinity for comparing
	best_a1= dna1
	best_a2 = dna2
	for align_length in range(max(len1, len2), len1 + len2 + 1):
		for pos1 in combinations(range(align_length), len1):
			for pos2 in combinations(range(align_length), len2):
				score = 0
				a1_chars, a2_chars = [], []
				ptr1, ptr2 = 0, 0
				for idx in range(align_length):
					if ptr1 < len1 and pos1[ptr1] == idx:
						char1 = dna1[ptr1]
						ptr1 += 1
					else:
						char1 = '-'
					if ptr2 < len2 and pos2[ptr2] == idx:
						char2 = dna2[ptr2]
						ptr2 += 1
					else:
						char2 = '-'
					if char1 == '-' or char2 == '-':
						score += GAP_PENALTY
					elif char1 != char2:
						score += MISMATCH_PENALTY
					a1_chars.append(char1)
					a2_chars.append(char2)
				if score < best_score:
					best_score = score
					best_a1 = "".join(a1_chars)
					best_a2 = "".join(a2_chars)
	return Result(int(best_score), best_a1, best_a2, None)


def greedy_first(dna1, dna2):
    ptr1, ptr2 = 0, 0
    aligned_dna1, aligned_dna2 = [], []
    score = 0

    while ptr1 < len(dna1) and ptr2 < len(dna2):
        
        # Option 1: align current characters (match or mismatch)
        if dna1[ptr1] == dna2[ptr2]:
            diagonal_cost = MATCH          # cost = 0
        else:
            diagonal_cost = MISMATCH_PENALTY  # cost = 2

        # Option 2: insert gap in dna2 (advance dna1 only)
        gap_in_dna2_cost = GAP_PENALTY     # cost = 1

        # Option 3: insert gap in dna1 (advance dna2 only)
        gap_in_dna1_cost = GAP_PENALTY     # cost = 1

        # Greedy choice: pick the locally optimal (minimum cost) option
        min_cost = min(diagonal_cost, gap_in_dna2_cost, gap_in_dna1_cost)

        if min_cost == diagonal_cost:
            # Irrevocable: commit to aligning both characters
            aligned_dna1.append(dna1[ptr1])
            aligned_dna2.append(dna2[ptr2])
            score += diagonal_cost
            ptr1 += 1
            ptr2 += 1

        elif min_cost == gap_in_dna2_cost:
            # Irrevocable: commit to gap in dna2
            aligned_dna1.append(dna1[ptr1])
            aligned_dna2.append('-')
            score += GAP_PENALTY
            ptr1 += 1

        else:
            # Irrevocable: commit to gap in dna1
            aligned_dna1.append('-')
            aligned_dna2.append(dna2[ptr2])
            score += GAP_PENALTY
            ptr2 += 1

    # Flush remaining characters — only one sequence can have leftovers
    while ptr1 < len(dna1):
        aligned_dna1.append(dna1[ptr1])
        aligned_dna2.append('-')
        score += GAP_PENALTY
        ptr1 += 1

    while ptr2 < len(dna2):
        aligned_dna1.append('-')
        aligned_dna2.append(dna2[ptr2])
        score += GAP_PENALTY
        ptr2 += 1

    return Result(score, "".join(aligned_dna1), "".join(aligned_dna2), None)

def dynamic_programming(dna1, dna2):
	dp = [[0] * (len(dna2) + 1) for _ in range(len(dna1) + 1)] # matrix, size: rows=(len(dna1) + 1) x columns=(len(dna2) + 1)
 
	for i in range(len(dna1) + 1):
		dp[i][0] = i * GAP_PENALTY
  
	for j in range(len(dna2) + 1):
		dp[0][j] = j * GAP_PENALTY
  
	for i in range(1, len(dna1) + 1):	
		for j in range(1, len(dna2) + 1):
			if dna1[i - 1] == dna2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + MATCH
			else:
				dp[i][j] = min(dp[i - 1][j] + GAP_PENALTY, dp[i][j - 1] + GAP_PENALTY, dp[i - 1][j - 1] + MISMATCH_PENALTY)
    
	aligned_dna1, aligned_dna2 = [], []
	i = len(dna1)
	j = len(dna2)

	while i > 0 or j > 0:

    # Diagonal: letter from dna1 and letter from dna2
		if i > 0 and j > 0:
			if dna1[i - 1] == dna2[j - 1]:
				cost = MATCH
			else:
				cost = MISMATCH_PENALTY

			if dp[i][j] == dp[i - 1][j - 1] + cost:
				aligned_dna1.append(dna1[i - 1])
				aligned_dna2.append(dna2[j - 1])
				i -= 1
				j -= 1
				continue

		# Up: letter from dna1 and gap in dna2
		if i > 0 and dp[i][j] == dp[i - 1][j] + GAP_PENALTY:
			aligned_dna1.append(dna1[i - 1])
			aligned_dna2.append("-")
			i -= 1

		# Left: letter from dna2 and gap in dna1
		else:
			aligned_dna1.append("-")
			aligned_dna2.append(dna2[j - 1])
			j -= 1	

	return Result(dp[len(dna1)][len(dna2)], "".join(reversed(aligned_dna1)), "".join(reversed(aligned_dna2)), None)