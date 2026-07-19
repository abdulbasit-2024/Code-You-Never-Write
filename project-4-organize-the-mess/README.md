# Project 4: Organize the Mess

## The Problem
My digital workspace accumulates clutter rapidly—spreadsheets, PDFs, and video files all get dumped into the same location. I needed a way to automatically group these files by type (e.g., Documents, Videos, Spreadsheets) to clean up the mess. However, using automated scripts to manipulate real files is dangerous, as a bad script can permanently delete or overwrite important data.

## The AI Tool Used
Gemini

## How I Verified the Result
This task required strict safety discipline to verify the code without risking my data. 
1. I created a complete duplicate of my messy folder to act as a sandbox.
2. I demanded the AI write a "Dry Run" mode into the script. 
3. I ran the script with `is_dry_run = True`. The script outputted a printed plan detailing exactly what it intended to do (e.g., "PLAN: Move 'Meta_Ad_Creative.mp4' ---> 'Videos/' folder"). 
4. I manually reviewed this printed plan. Because the AI correctly categorized my PDFs as Documents and my MP4s as Videos without suggesting any deletions, the logic was verified.
5. Only after passing this manual verification did I change the script to live mode and execute the safe organization of the files.
