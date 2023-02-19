import sys
from pdf2image import convert_from_path
from img_to_txt import extract_text_from_image, write_text_to_word


def img_extractor(file_w_path, file):
    path_to = r"img/"
    pages = convert_from_path(file_w_path, 350, output_folder='raw', fmt='jpg')

    for i, page in enumerate(pages):
        image_name = path_to + f"{file[:-4]}_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i + 1


def main(file_w_path, file_name):
    if file_name.endswith(".pdf"):
        img_extractor(file_w_path, file_name)
    elif file_name.endswith(".jpg") or file_name.endswith(".png"):
        print("File is image, continuing to text processing....")
    else:
        print("Unsupported file format. Please provide a PDF file.")
