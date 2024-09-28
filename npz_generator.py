"""
This file is licensed by the MIT License
Copyright © 2024 RandomKiddo, Nishanth-Kunchala, Jacoube, danield33
"""

import numpy as np
import cv2
import os

encodings = {
    'Mild': 0,
    'Moderate': 1,
    'Non': 2,
    'Very': 3
}

j = 1
for fp in sorted(os.listdir('Data')):
    if fp.startswith('.'):
        continue
    i = 0
    imgs = []
    for f in sorted(os.listdir(os.path.join('Data', fp))):
        if f.startswith('.'):
            continue
        img = np.array(
            cv2.cvtColor(
                cv2.resize(
                    cv2.imread(os.path.join('Data', fp, f)), (124, 62)
                ), cv2.COLOR_RGB2GRAY)/255.
        )
        imgs.append(img)
        i += 1
        if i == 61:
            np.savez_compressed(os.path.join('Stacked', fp, f'{j}.npz'), np.stack(imgs, axis=-1))
            i = 0
            imgs = []
            print(f'Processing Stack j={j}')
            j += 1