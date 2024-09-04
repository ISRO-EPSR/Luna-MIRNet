from PIL import Image
from pathlib import Path

def enhance_image(image_path: Path) -> Path:
    # Load the image
    image = Image.open(image_path)
    
    # Simulate enhancement (e.g., save it with a new name)
    enhanced_image_path = image_path.with_name(f"enhanced_{image_path.name}")
    
    # Save the "enhanced" image
    image.save(enhanced_image_path)
    
    return enhanced_image_path
