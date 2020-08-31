# Watermark add to pdf(1 ~ 1000) as the requirements

import PyPDF2

# open sample pdf and reading
template = PyPDF2.PdfFileReader(open('sample.pdf','rb'))

# open sample watermark pdf and reading
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))

# write file as output
output = PyPDF2.PdfFileWriter()

# getting page count and adding watermark
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    # save watermarked file and give new name
    with open('watermarked.pdf','wb') as file:
        output.write(file)