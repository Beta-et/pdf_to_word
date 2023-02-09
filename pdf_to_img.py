import sys
from pdf2image import convert_from_path


def img_extractor(file):
    path_to = r"imgs/"
    pages = convert_from_path('pdfs/' + file, 350, output_folder='raw', fmt='jpg')

    for i, page in enumerate(pages):
        image_name = path_to + f"{file[:-4]}_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i + 1


def main():
    if len(sys.argv) != 2:
        print("Please provide a file name as an argument.")
        sys.exit(1)

    file_name = sys.argv[1]
    if file_name.endswith(".pdf"):
        img_extractor(file_name)
    else:
        print("Unsupported file format. Please provide a PDF file.")


if __name__ == '__main__':
    main()
