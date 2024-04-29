from PyPDF2 import PdfFileMerger

pdfs = ['./examples/example-1.pdf', './examples/example-2.pdf', './examples/example-3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

name = input("📝 What do you want for the PDF file name ? (without '.pdf'): ")
pdf_filename = name + ".pdf"

print("📋 Currently generating " + pdf_filename + " for you ...")
merger.write(pdf_filename)
merger.close()

print("🎉 Congrats! You have successfully merged your PDF files!")
