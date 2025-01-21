import os
import cv2
import argparse
from filters import apply_printer_noise, apply_vintone, apply_mob_glow

INPUT_DIR = './input'
OUTPUT_DIR = './output'

FILTERS = {
    'printer_noise': apply_printer_noise,
    'vintone': apply_vintone,
    'mob_glow': apply_mob_glow
}

def process_images(selected_filter="mob_glow", intensity=1.0):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{selected_filter}_{filename}")

            image = cv2.imread(input_path)
            if image is None:
                print(f"Error: Could not read image {input_path}")
                continue

            filtered_image = FILTERS[selected_filter](image, intensity)
            cv2.imwrite(output_path, filtered_image)
            print(f"Saved image {filename} to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply filters to images.")
    parser.add_argument("filter", choices=FILTERS.keys(), help="Select a filter to apply.")
    parser.add_argument("--intensity", type=float, default=1.0, help="Intensity of the filter (0.0 to 1.0).")
    args = parser.parse_args()

    process_images(selected_filter=args.filter, intensity=args.intensity)
