from itertools import combinations
# scoring parameters (cost)
gamma = 0 # match
alpha = 1 # gap `-`
beta = 2	# mismatch

def brute_force(dna1, dna2):
	len1 = len(dna1)
	len2 = len(dna2)
	best_score = float('inf') # infinity for comparing
	best_a1 = None
	best_a2 = None
	for align_length in range(max(len1, len2), len1 + len2 + 1):
		for pos1 in combinations(range(align_length), len1):
			for pos2 in combinations(range(align_length), len2):
				print(f"Position 1: {pos1}\tPosition 2: {pos2}")
	return best_score, best_a1, best_a2