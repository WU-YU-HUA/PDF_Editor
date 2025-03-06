import fitz

def split_pdf(input_pdf, output_path, every_page):
    file = fitz.open(input_pdf)
    for page in range(0, len(file), every_page):
        end_page = page + every_page - 1
        new_file = fitz.open()
        new_file.insert_pdf(file, from_page=page, to_page=end_page)
        new_file.save(f"{output_path}_{page+1}_{end_page+1}.pdf")
        new_file.close()
    file.close()

def merge_pdf(input_array, output_path):
    new_file = fitz.open()
    for input in input_array:
        file = fitz.open(input)
        new_file.insert_pdf(file)
        file.close()

    new_file.save(output_path)
    new_file.close()

# split_pdf('abroad_travel.pdf', 'split_test', 4)
merge_pdf(['split_test_1_4.pdf', 'split_test_5_8.pdf', 'split_test_9_12.pdf'], 'merge_pdf.pdf')