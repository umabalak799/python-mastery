import os
from PyPDF2 import PdfMerger                  #imports PdfMerger class from PyPDF2 library this is used to combine multiple pdf files into one 

merger = PdfMerger()                                       #creates Pdfmerger object, think of this as an empty container

pdf_folder = r"C:\Users\ubkk\OneDrive\Documents\python-mastery\beginner\Exercise 8\pdfs"       #stores the path 
pdf_files = os.listdir(pdf_folder)                                                             #get all file names from the pdfs folder stores them as a list

# print(pdf_files)
for pdf in pdf_files:                               #starts a loop goes throug the each file name in the folder one by one
    if pdf.endswith(".pdf"):                                          #checks whther the file is a pdf
        merger.append(os.path.join(pdf_folder, pdf))      #combines folder path and careates a full file path adds that pdf to the merger container

merger.write("merged.pdf")            #combines all added PDFs and saves them into new file called merged.pdf
merger.close()                        #closes the merger and frees memory and completes file writing properly     

print("PDFS merged sucessfully into merged.pdf")
print ("Saved at:", os.getcwd())

# print("PDF merger ready hogaya bhai")
