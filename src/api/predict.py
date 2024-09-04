from src.data_processing.preprocess import preprocess_image
from src.models.mirnet import enhance_image_with_mirnet
from src.data_processing.postprocess import postprocess_image
from pathlib import Path

def process_image(file_path):
    """Process the image by applying preprocessing, enhancement, and postprocessing."""
    # Apply preprocessing
    preprocessed_path = preprocess_image(file_path)
    
    # Apply MIRNet enhancement
    enhanced_path = enhance_image_with_mirnet(preprocessed_path)
    
    # Apply postprocessing
    postprocessed_path = postprocess_image(enhanced_path)
    
    # Return the path of the postprocessed image
    return postprocessed_path
