import os

from PIL import Image


def montage(image_id: str) -> None:
    bbox_image = Image.open(os.path.join("/pfs/bbox", image_id))
    normalized_image = Image.open(os.path.join("/pfs/normalize", image_id))

    total_width = bbox_image.width + normalized_image.width
    height = bbox_image.height

    new_image = Image.new("RGB", (total_width, height))
    new_image.paste(bbox_image, (0, 0))
    new_image.paste(normalized_image, (bbox_image.width, 0))

    output_filepath = os.path.join("/pfs/out", image_id)
    new_image.save(output_filepath)


image_id = str(os.environ.get("PACH_DATUM_bbox_JOIN_ON"))

montage(image_id)
