from pathlib import Path
import shutil

def get_target_category(filepath: Path) -> str:
    """Returns the folder name based on file extension"""
    ext = filepath.suffix.lower()
    
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']:
        return "Images"
    elif ext in ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv']:
        return "Documents"
    elif ext in ['.mp4', '.mov', '.avi', '.mkv', '.wmv']:
        return "Videos"
    elif ext in ['.mp3', '.wav', '.flac', '.aac', '.m4a']:
        return "Audio"
    elif ext in ['.zip', '.rar', '.7z', '.tar', '.gz']:
        return "Archives"
    elif ext in ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']:
        return "Code"
    else:
        return "Others"


def organize_downloads():
   
    downloads_path = Path.home() / "Downloads"
    
    if not downloads_path.exists():
        print("Downloads folder not found!")
        return
    
    
    categories = ["Images", "Documents", "Videos", "Audio", "Archives", "Code", "Others"]
    for category in categories:
        (downloads_path / category).mkdir(exist_ok=True)
    
    
    for file in downloads_path.iterdir():
        if file.is_file(): 
            category = get_target_category(file)
            target_folder = downloads_path / category
            
            try:
                shutil.move(str(file), str(target_folder / file.name))
                print(f"Moved: {file.name} → {category}/")
            except Exception as e:
                print(f"Error moving {file.name}: {e}")


if __name__ == "__main__":
    print("Starting Downloads folder organization...")
    organize_downloads()
    print("Organization completed!")