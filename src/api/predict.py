from src.data_processing.preprocess import preprocess_image
from src.models.model import enhance_image
from pathlib import Path

def process_image(file_path):
    """Process the image by applying preprocessing and enhancement."""
    # Convert file_path to a Path object if it is not already one
    file_path = Path(file_path)
    
    # Apply preprocessing
    preprocessed_path = preprocess_image(file_path)
    
    # Apply image enhancement
    enhanced_path = enhance_image(preprocessed_path)
    
    # Return the path of the enhanced image
    return enhanced_path
