import os

# This script automatically scans your projects folder, 
# replaces spaces with underscores, and fixes asset references.
projects_dir = "projects"

if not os.path.exists(projects_dir):
    print("Error: 'projects' folder not found here. Make sure you put this script in your main portfolio folder.")
    exit()

print("Scanning and fixing file names...")

for root, dirs, files in os.walk(projects_dir):
    for file in files:
        # Check image and document files
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf', '.svg', '.html', '.htm')):
            old_path = os.path.join(root, file)
            
            # Clean up the filename: replace spaces with underscores to prevent web breaking
            new_filename = file.replace(" ", "_")
            new_path = os.path.join(root, new_filename)
            
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Fixed name: {file} -> {new_filename}")

print("All files cleaned and synchronized successfully!")