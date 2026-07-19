# Project 3: The Books Don't Match

## The Problem
When organizing group funds for a tour, the expected hand-counted total rarely matches the digital transfer history because people send money using different banking apps, partial amounts, and unclear memo descriptions. I needed a script that could apply my own personal "translation rules" to ambiguous digital memos, match them to the correct individuals, and instantly calculate the missing financial gap so I know exactly who to follow up with.

## The AI Tool Used
Gemini

## How I Verified the Result
Before running the script, I established the ground truth by manually calculating the books:
1. Four people owing 15,000 means the total expected baseline is 60,000.
2. I manually translated the messy records ("Anas Transfer" [15,000], "Basit Trip" [15,000], "Abu H. partial" [10,000]) which equals 40,000 received.
3. This creates a hand-calculated gap of 20,000.
4. Manually checking the names reveals Noman Habib paid nothing (owes 15,000) and Abu Huraira shorted the payment (owes 5,000).

When I ran the AI script, it correctly identified the total gap as 20,000 and explicitly flagged Abu Huraira for 5,000 and Noman Habib for 15,000. Because the script's output matched my manual audit perfectly, the code was verified as successful.
