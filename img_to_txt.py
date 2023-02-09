import subprocess
import sys
import docx


def imgs():
    images = 'imgs/161118 Letter_0.jpg'
    return images


def extract_text_from_image(image_file):
    text = subprocess.run(["tesseract", image_file, "stdout", "-l", "eng"], capture_output=True, text=True).stdout
    return text


def extract_text_from_pdf(pdf_file):
    images = imgs()
    text = ""
    for i, image in enumerate(images):
        image_file = f"image_{i}.png"
        image.save(image_file)
        text += extract_text_from_image(image_file) + "\n"
    return text


def write_text_to_word(text):
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save("output.docx")
    print('saved')


def main():
    if len(sys.argv) != 2:
        print("Please provide a file name as an argument.")
        sys.exit(1)

    file_name = sys.argv[1]
    if file_name.endswith(".pdf"):
        text = extract_text_from_pdf(file_name)
    elif file_name.endswith(".jpg") or file_name.endswith(".png"):
        text = extract_text_from_image(file_name)
    else:
        print("Unsupported file format. Please provide a PDF or image file.")
        sys.exit(1)

    write_text_to_word(text)
    print(text)


if __name__ == "__main__":
    main()
