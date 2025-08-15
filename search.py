# search.py
import os
from ddgs import DDGS
import requests
from PIL import Image
from io import BytesIO
import random

def download_images(query, max_images, out_dir, force=False):
    """
    Downloads images from DuckDuckGo image search.
    Args:
        query (str): Search keywords
        max_images (int): Number of images to download
        out_dir (str): Directory to save images
        force (bool): If True, always re-download
    Returns:
        List of file paths to downloaded images
    """
    os.makedirs(out_dir, exist_ok=True)

    if not force and len(os.listdir(out_dir)) >= max_images:
        return [os.path.join(out_dir, f) for f in os.listdir(out_dir)]

    # Clear old files if force is True
    if force:
        for f in os.listdir(out_dir):
            os.remove(os.path.join(out_dir, f))

    print(f"[INFO] Searching for: {query}")
    results = DDGS().images(query, max_results=max_images * 3)

    paths = []
    for idx, r in enumerate(results):
        if len(paths) >= max_images:
            break
        try:
            url = r["image"]
            resp = requests.get(url, timeout=5)
            img = Image.open(BytesIO(resp.content)).convert("RGB")
            save_path = os.path.join(out_dir, f"{query.replace(' ', '_')}_{idx}.jpg")
            img.save(save_path)
            paths.append(save_path)
        except Exception as e:
            print(f"[WARN] Skipping an image due to error: {e}")
            continue

    random.shuffle(paths)
    return paths
