import os

from xml.etree import ElementTree

from PIL import Image


def bbox(image_id: str) -> None:
    image = Image.open(os.path.join("/pfs/images", image_id + ".jpg"))
    label = ElementTree.parse(os.path.join("/pfs/labels", image_id)).getroot()

    min_x = int(label.find("object/bndbox/xmin").text)
    max_x = int(label.find("object/bndbox/xmax").text)
    min_y = int(label.find("object/bndbox/ymin").text)
    max_y = int(label.find("object/bndbox/ymax").text)

    # draw a box around the object
    image = image.crop((min_x, min_y, max_x, max_y))
    image.save(os.path.join("/pfs/out", image_id + ".jpg"))


image_id = str(os.environ.get("PACH_DATUM_images_JOIN_ON"))

bbox(image_id)
