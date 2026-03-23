# BOJ 1330 - Compare Two Numbers
# URL     : https://www.acmicpc.net/problem/1330
# Tier    : Bronze V
# Category: Implementation
# Date    : 2026-03-23

# ───────────────────────────────
# 📌 Approach
# Read two integers and compare them using conditional operators.
# ───────────────────────────────

a, b = map(int, input().split())

if a < b:
    print("<")
elif a == b:
    print("==")
elif a > b:
    print(">")

# ───────────────────────────────
# 📝 Notes
# - Used map(int, input().split()) to parse two integers at once
# - Used explicit elif instead of else for clarity
# ───────────────────────────────
