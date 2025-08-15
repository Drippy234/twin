# features.py
import torch
from torchvision import models, transforms as T
from PIL import Image
import numpy as np
import os
import requests
from io import BytesIO
from ddgs import DDGS


def build_model():
    """Load pre-trained ResNet50 model."""
    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
    model.eval()
    preprocess = T.Compose([
        T.Resize((224, 224)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225])
    ])
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return model, preprocess, device

def get_features(image, model, preprocess, device):
    """Extract features from an image."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    img_tensor = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model(img_tensor)
    features = features / features.norm()
    return features.squeeze().cpu().numpy()

def download_images(query, max_images=10):
    """Download images from DuckDuckGo Search."""
    results = DDGS().images(query, max_results=max_images)
    paths = []
    for i, res in enumerate(results):
        try:
            img_data = requests.get(res["image"], timeout=5).content
            img = Image.open(BytesIO(img_data))
            if img.mode != "RGB":
                img = img.convert("RGB")
            path = f"downloads/{query.replace(' ', '_')}_{i}.jpg"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            img.save(path)
            paths.append(path)
        except Exception:
            continue
    return paths

def find_top_matches(user_img, query, model, preprocess, device, top_k=3):
    """Find top look-alike matches for a given query."""
    # Download fresh images each time
    paths = download_images(query, max_images=15)

    if not paths:
        return [], []

    user_feat = get_features(user_img, model, preprocess, device)
    scores = []
    for path in paths:
        try:
            img = Image.open(path)
            feat = get_features(img, model, preprocess, device)
            score = np.dot(user_feat, feat) / (np.linalg.norm(user_feat) * np.linalg.norm(feat))
            scores.append((score, path))
        except Exception:
            continue

    scores.sort(reverse=True)
    top = scores[:top_k]
    images = [Image.open(path) for _, path in top]
    return images, [p for _, p in top]
