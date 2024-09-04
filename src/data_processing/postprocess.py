from PIL import Image
from pathlib import Path  # Import Path class from pathlib module

def postprocess_image(file_path):
    # Convert file_path to a Path object if it is not already one
    file_path = Path(file_path)
    
    # Open an image file
    with Image.open(file_path) as img:
        # Convert image back to RGB if necessary (optional step)
        img = img.convert("RGB")
        
        # Save the postprocessed image
        postprocessed_path = file_path.with_name(f"postprocessed_{file_path.name}")
        img.save(postprocessed_path)
        
        return postprocessed_path
