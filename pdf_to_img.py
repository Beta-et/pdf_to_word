from pdf2image import convert_from_path
from pathlib import Path


path_list = Path("pdfs/").glob('**/*.pdf')

for file in path_list:
    filename = str(file)[5:-4]
    print(filename, file, sep=' : ')

    path_to = r"imgs/"
    pages = convert_from_path(file, 350, output_folder='raw')

    for i, page in enumerate(pages):
        image_name = path_to + f"{filename}_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i + 1

