import os
import sys
from PIL import Image
from loguru import logger

class ImageConverter:
    def __init__(self, input_path, output_path, output_format):
        self.input_path = input_path
        self.output_path = output_path
        self.output_format = output_format.upper()
        self.validate_paths()

    def validate_paths(self):
        if not os.path.isfile(self.input_path):
            logger.error(f"The input file {self.input_path} does not exist.")
            sys.exit(1)
        if not os.path.isdir(os.path.dirname(self.output_path)):
            logger.error(f"The output directory {os.path.dirname(self.output_path)} does not exist.")
            sys.exit(1)

    def convert_image(self):
        try:
            with Image.open(self.input_path) as img:
                img = img.convert("RGB")
                img.save(self.output_path, self.output_format)
                logger.info(f"Converted {self.input_path} to {self.output_path} in {self.output_format} format.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 4:
        logger.error("Usage: python image_converter.py <input_image_path> <output_image_path> <output_format>")
        sys.exit(1)
    
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    output_format = sys.argv[3]

    converter = ImageConverter(input_image_path, output_image_path, output_format)
    converter.convert_image()

if __name__ == "__main__":
    logger.add("image_converter.log", rotation="1 MB")
    main()
