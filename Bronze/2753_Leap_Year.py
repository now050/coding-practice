# BOJ 2753 - Leap Year
# URL     : https://www.acmicpc.net/problem/2753
# Tier    : Bronze V
# Category: Implementation
# Date    : 2026-03-25
# ───────────────────────────────
# <Approach>
# - Using nested if statements can cause multiple outputs for the same case.
# - To avoid this, the false condition is handled with an else statement instead of a separate if statement.
# ───────────────────────────────

year = int(input())

if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("1")
    else:
      print("0")
  else:
    print("1")
else:
  print("0")

# ───────────────────────────────
# <Notes>
# - When using nested if statements, be careful not to print multiple times for the same case
# ───────────────────────────────
