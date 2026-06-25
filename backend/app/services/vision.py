from dataclasses import dataclass

import cv2
import numpy as np


@dataclass(frozen=True)
class DetectedSticker:
    row: int
    col: int
    color_name: str
    confidence: float


def dominant_bgr_color(image_bytes: bytes) -> tuple[int, int, int]:
    data = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not decode image")

    resized = cv2.resize(image, (90, 90))
    pixels = resized.reshape((-1, 3)).astype(np.float32)
    _, labels, centers = cv2.kmeans(
        pixels,
        3,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0),
        3,
        cv2.KMEANS_PP_CENTERS,
    )
    counts = np.bincount(labels.flatten())
    dominant = centers[int(np.argmax(counts))]
    return tuple(int(value) for value in dominant)

