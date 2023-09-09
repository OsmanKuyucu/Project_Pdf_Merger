from PyPDF2 import PdfMerger
import os


input_files = ['file1.pdf', 'file2.pdf']
output_file = 'merged_output.pdf'
merger = PdfMerger()

for file in input_files:
    merger.append(file)

merger.write(output_file)
merger.close()