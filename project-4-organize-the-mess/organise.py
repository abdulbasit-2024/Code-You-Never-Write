import os
import shutil

# 1. Setup the Folders
# WARNING: Always use a copy of your folder for safety!
source_folder = "./Downloads_Copy"

# 2. Safety First: The Dry Run Switch
# Set this to False ONLY after you review the printed plan
is_dry_run = True 

# 3. Define File Categories
extensions = {
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"]
}

print("--- FILE ORGANIZATION PLAN ---")
if is_dry_run:
    print("STATUS: DRY RUN MODE. No files will actually be moved.\n")
else:
    print("STATUS: LIVE MODE. Files are being moved right now.\n")

# 4. Scan and Plan
# Check every file in the messy folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    # Skip if it's a folder, we only want to move files
    if os.path.isdir(file_path):
        continue

    # Find out what type of file it is
    file_ext = os.path.splitext(filename)[1].lower()
    
    # Figure out which category folder it belongs to
    target_category = "Others" 
    for category, exts in extensions.items():
        if file_ext in exts:
            target_category = category
            break

    target_folder = os.path.join(source_folder, target_category)
    
    # 5. Execute or just Print the Plan
    if is_dry_run:
        # Just show the user what WOULD happen
        print(f"PLAN: Move '{filename}' ---> '{target_category}/' folder")
    else:
        # Actually do the work
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)
        print(f"SUCCESS: Moved '{filename}' to '{target_category}/'")

if is_dry_run:
    print("\nVERIFICATION COMPLETE: If this plan looks correct, change 'is_dry_run = False' in the code and run it again.")
