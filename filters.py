import cv2
import numpy as np

def apply_printer_noise(image, intensity=1.0):

    noise = np.random.randint(0, 2, image.shape[:2], dtype='uint8') * 255  # Random black/white noise
    noise = cv2.merge([noise] * 3)  # Make noise 3-channel
    noisy_image = cv2.addWeighted(image, 1 - intensity, noise, intensity, 0)  # Blend noise with the original
    return noisy_image

def apply_vintone(image, intensity=1.0):
    
    image = image.astype('float32') / 255.0

    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)

    vintone_image = cv2.addWeighted(image, 1 - intensity, sepia_image, intensity, 0)
    return (vintone_image * 255).astype('uint8')

def apply_mob_glow(image, intensity=1.0):

    brighter_image = cv2.convertScaleAbs(image, alpha=1 + intensity * 0.2, beta=50 * intensity)

    blurred_image = cv2.GaussianBlur(brighter_image, (15, 15), 0)

    mob_glow_image = cv2.addWeighted(brighter_image, 1 - intensity * 0.3, blurred_image, intensity * 0.3, 0)
    return mob_glow_image
