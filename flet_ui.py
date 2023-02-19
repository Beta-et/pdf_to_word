import pdf_to_img as pti
import img_to_txt as itt
import flet as ft


def main(page: ft.Page):
    page.title = "Beta OCR"
    page.theme = ft.Theme(color_scheme_seed='black', use_material3=True)
    page.window_width = 200
    page.window_height = 200

    def file_pick(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled"
        )
        selected_files_path.value = e.files[0].path

        selected_files.update()

        ocr_status.value = OCR(selected_files.value, selected_files_path.value)
        ocr_status.update()

    def OCR(file, file_w_path):
        img_ext = ['.png', '.jpg', 'jpeg']
        ext = file[-4:]
        if file.endswith('.pdf'):
            pti.main(file_w_path, file)
            print('PDF converted to Image')

            itt.main(file[:-4])
            print('Image converted to Text')
            return "Complete"
        elif file[-4:] in img_ext:
            itt.main(file[:-4])
            print('Image converted to Text')
            return "Complete"
        else:
            return "Failed"

    pick_files_dialog = ft.FilePicker(on_result=file_pick)
    selected_files = ft.Text()
    selected_files_path = ft.Text()
    ocr_status = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Column(
            [
                ft.ElevatedButton(
                    "Pick Files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                        allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']
                    ),
                ),
                selected_files,
                ocr_status,
            ]
        )
    )


ft.app(target=main)