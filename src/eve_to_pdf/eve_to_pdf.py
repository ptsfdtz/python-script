import os
from docx2pdf import convert
import openpyxl

def convert_docx_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        if file.endswith('.docx'):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + '.pdf')
            convert(input_file, output_file)

def convert_excel_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        if file.endswith('.xlsx'):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + '.pdf')

            workbook = openpyxl.load_workbook(input_file)
            sheets = workbook.sheetnames

            # Create a PDF file for each sheet in the workbook
            for sheet_name in sheets:
                ws = workbook[sheet_name]
                ws.title = sheet_name
                pdf_file = output_file[:-4] + "_" + sheet_name + ".pdf"
                ws.sheet_view.showGridLines = False  # Hide gridlines in the PDF
                ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE  # Landscape orientation
                ws.page_setup.fitToHeight = False
                ws.page_setup.fitToWidth = True
                ws.page_margins.left = 0.2
                ws.page_margins.right = 0.2
                ws.page_margins.top = 0.2
                ws.page_margins.bottom = 0.2
                ws.page_margins.header = 0
                ws.page_margins.footer = 0
                ws.page_setup.paperSize = ws.PAPERSIZE_A4

                ws.print_options.horizontalCentered = True
                ws.print_options.verticalCentered = True

                workbook.save(output_file)
                os.remove(output_file)

if __name__ == "__main__":
    input_folder = "src\eve_to_pdf\input"
    output_folder = "src\eve_to_pdf\output"

    convert_docx_to_pdf(input_folder, output_folder)
    convert_excel_to_pdf(input_folder, output_folder)
