from PIL import Image, ImageEnhance
import numpy as np
import cv2
from pathlib import Path

def denoise_image(image_cv):
    """Apply noise reduction to the image."""
    return cv2.fastNlMeansDenoisingColored(image_cv, None, 10, 10, 7, 21)

def equalize_histogram(image_cv):
    """Apply histogram equalization to the image."""
    if len(image_cv.shape) == 2:  # Grayscale image
        return cv2.equalizeHist(image_cv)
    else:  # Color image
        ycrcb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2YCrCb)
        channels = list(cv2.split(ycrcb))  # Convert tuple to list
        channels[0] = cv2.equalizeHist(channels[0])
        ycrcb = cv2.merge(channels)
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


def resize_image(image, size=(256, 256)):
    """Resize the image to the specified size."""
    return image.resize(size)

def adjust_brightness(image, factor=1.5):
    """Adjust the brightness of the image."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def preprocess_image(image_path, size=(256, 256), brightness_factor=1.5):
    """Preprocess the image by applying various steps."""
    # Load image
    image = Image.open(image_path)
    
    # Convert image to OpenCV format
    image_cv = np.array(image)
    
    # Apply preprocessing steps
    image_cv = denoise_image(image_cv)
    image_cv = equalize_histogram(image_cv)
    
    # Convert back to PIL format for resizing and brightness adjustment
    image = Image.fromarray(image_cv)
    image = resize_image(image, size=size)
    image = adjust_brightness(image, factor=brightness_factor)
    
    # Create directory if it doesn't exist
    output_dir = Path("public/preprocessed")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save preprocessed image
    preprocessed_path = output_dir / f"preprocessed_{Path(image_path).name}"
    image.save(preprocessed_path)
    
    return preprocessed_path
