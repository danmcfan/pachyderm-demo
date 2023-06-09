import os

from PIL import Image


def normalize(filepath: str) -> None:
    image = Image.open(filepath)

    image = image.convert("L")

    output_filepath = os.path.join("/pfs/out", os.path.basename(filepath))
    image.save(output_filepath)


for dirpath, dirs, files in os.walk("/pfs/bbox"):
    for file in files:
        normalize(os.path.join(dirpath, file))
