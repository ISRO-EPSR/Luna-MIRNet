import torch
from torchvision import transforms
from PIL import Image

# Example for loading a pre-trained model
def load_mirnet_model():
    # Load your MIRNet model (adjust this based on your actual model loading code)
    model = torch.load("path/to/mirnet_model.pth")
    model.eval()
    return model

def enhance_image_with_mirnet(image_path):
    """Enhance image using MIRNet."""
    # Load MIRNet model
    model = load_mirnet_model()
    
    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    
    # Perform enhancement
    with torch.no_grad():
        output_tensor = model(input_tensor)
    
    # Convert output tensor to PIL image
    output_image = transforms.ToPILImage()(output_tensor.squeeze(0))
    
    # Save enhanced image
    enhanced_path = Path(f"enhanced_{Path(image_path).name}")
    output_image.save(enhanced_path)
    
    return enhanced_path
