from itertools import combinations
# scoring parameters (cost)
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
						score += alpha
					elif char1 != char2:
						score += beta
					a1_chars.append(char1)
					a2_chars.append(char2)
				if score < best_score:
					best_score = score
					best_a1 = "".join(a1_chars)
					best_a2 = "".join(a2_chars)
					print(f"new best: a1 -> {best_a1}\ta2 -> {best_a2} score {best_score}")
	return best_score, best_a1, best_a2