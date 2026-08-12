import os

projects_dir = "projects"

if not os.path.exists(projects_dir):
    print("Error: 'projects' folder not found in the current directory.")
else:
    for item in os.listdir(projects_dir):
        item_path = os.path.join(projects_dir, item)
        
        # Check if it's a directory (e.g., "Medes Club", "Aibolot")
        if os.path.isdir(item_path):
            print(f"Scanning project folder: {item}")
            for file in os.listdir(item_path):
                # Look for HTML files that aren't already named index.html
                if file.endswith(".html") and file.lower() != "index.html":
                    old_file_path = os.path.join(item_path, file)
                    new_file_path = os.path.join(item_path, "index.html")
                    
                    # If an index.html doesn't exist yet, rename the long file to index.html
                    if not os.path.exists(new_file_path):
                        os.rename(old_file_path, new_file_path)
                        print(f"  -> Renamed '{file}' to 'index.html'")
                    else:
                        print(f"  -> 'index.html' already exists in {item}, skipping rename for '{file}'.")

print("Organization complete! Run your git commands to push.")