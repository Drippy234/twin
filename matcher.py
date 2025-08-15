# matcher.py
import numpy as np
from PIL import Image

def find_top_matches(user_img, cartoon_features, cartoon_paths, celeb_features, celeb_paths, model, preprocess, get_features):
    if user_img is None:
        return [], []

    user_feat = get_features(user_img, model, preprocess)

    def get_top3(features, paths):
        sims = np.dot(features, user_feat) / (
            np.linalg.norm(features, axis=1) * np.linalg.norm(user_feat)
        )
        idx = np.argsort(sims)[::-1][:3]
        return [Image.open(paths[i]) for i in idx]

    cartoons = get_top3(cartoon_features, cartoon_paths)
    celebs = get_top3(celeb_features, celeb_paths)

    return cartoons, celebs
