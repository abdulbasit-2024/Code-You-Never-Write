# Project 1: Money Detective

## The Problem
I needed a way to find hidden financial leaks in my recent expense history without manually checking every single line. Standard budgeting apps miss personal context, so I wanted a custom script to analyze my recent spending (including advertising budgets, tour deposits, and software subscriptions) to spot any accidental duplicate charges.

## The AI Tool Used
Gemini

## How I Verified the Result
To ensure the AI's code was completely accurate, I used the "Code You Never Write" verification method. Before trusting the script, I manually calculated the known baseline figures:

1. I hand-calculated that my total spend for this statement was exactly 82,300.
2. I knew my Meta Ads campaigns were billed on different days (July 1st and July 12th) and should not be counted as duplicates.

The script correctly calculated the exact total as 82,300. It also successfully ignored the ad campaigns and caught the true duplicate charge (a double billing for a Phone VPN Subscription on July 8th). Because the script's output perfectly matched the facts I already knew to be true, I verified the code is safe to trust.
