# BOJ 9498 - Exam Scores
# URL     : https://www.acmicpc.net/problem/9498
# Tier    : Bronze V
# Category: Implementation
# Date    : 2026-03-24

# ───────────────────────────────
# <Approach>
# Read an integer and categorize it using chained conditional statements.
# ───────────────────────────────

score = int(input())

if 90 <= score <= 100:
	print("A")
elif 80 <= score <= 89:
	print("B")
elif 70 <= score <= 79:
	print("C")
elif 60 <= score <= 69:
	print("D")
else:
	print("F")

# ───────────────────────────────
# <Notes>
# - Each condition is mutually exclusive, so 'elif' is used instead of 'if'
# ───────────────────────────────
