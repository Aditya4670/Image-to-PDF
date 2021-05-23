import img2pdf

with open("test.pdf", 'wb') as f:
    f.write(img2pdf.convert(images))
    f.close()
