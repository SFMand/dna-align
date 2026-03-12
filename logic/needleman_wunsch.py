# scoring parameters (cost) — same as brute_force.py
alpha = 1  # gap `-`
beta = 2   # mismatch

def needleman_wunsch(dna1, dna2):
	len1 = len(dna1)
	len2 = len(dna2)

	# Build scoring matrix
	dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
	for i in range(len1 + 1):
		dp[i][0] = i * alpha
	for j in range(len2 + 1):
		dp[0][j] = j * alpha

	for i in range(1, len1 + 1):
		for j in range(1, len2 + 1):
			if dna1[i - 1] == dna2[j - 1]:
				match_cost = 0
			else:
				match_cost = beta
			dp[i][j] = min(
				dp[i - 1][j - 1] + match_cost,  # match or mismatch
				dp[i - 1][j] + alpha,            # gap in dna2
				dp[i][j - 1] + alpha             # gap in dna1
			)

	# Traceback
	a1_chars, a2_chars = [], []
	i, j = len1, len2
	while i > 0 or j > 0:
		if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (0 if dna1[i - 1] == dna2[j - 1] else beta):
			a1_chars.append(dna1[i - 1])
			a2_chars.append(dna2[j - 1])
			i -= 1
			j -= 1
		elif i > 0 and dp[i][j] == dp[i - 1][j] + alpha:
			a1_chars.append(dna1[i - 1])
			a2_chars.append('-')
			i -= 1
		else:
			a1_chars.append('-')
			a2_chars.append(dna2[j - 1])
			j -= 1

	aligned1 = "".join(reversed(a1_chars))
	aligned2 = "".join(reversed(a2_chars))
	best_score = dp[len1][len2]
	return best_score, aligned1, aligned2
