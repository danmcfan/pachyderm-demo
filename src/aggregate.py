import json
import os

from PIL import Image


def aggregate(filepaths: list[str]) -> None:
    values = []

    images = [Image.open(filepath) for filepath in filepaths]
    for image in images:
        values.extend(image.getdata())

    min_value = min(values)
    mean_value = sum(values) / len(values)
    max_value = max(values)

    with open("/pfs/out/aggregate.json", "w") as f:
        json.dump(
            {
                "minimum": min_value,
                "mean": mean_value,
                "maximum": max_value,
            },
            f,
            indent=4,
        )


filepaths = []
for dirpath, dirs, files in os.walk("/pfs/normalize"):
    for file in files:
        filepaths.append(os.path.join(dirpath, file))

aggregate(filepaths)
