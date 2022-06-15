
import csv


file = open('D:\\Programs\\Python Projects\\CVS PDF exercise\\15-PDFs-and-Spreadsheets\\Exercise_Files\\find_the_link.csv', encoding='utf-8')
text = csv.reader(file)
data_lines = list(text)

find = []
location = 0
for x in data_lines:
    find.append(x[location])
    location += 1
link = ''
link = link.join(find)
print(link)


import re
import PyPDF2
pattern = re.compile(r"\d{1}")
phone_no = []
f = open('D:\\Programs\\Python Projects\\CVS PDF exercise\\15-PDFs-and-Spreadsheets\\Exercise_Files\\Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)
for n in range(0, 17):
    page = pdf.getPage(n)
    text = page.extractText()
    phone_no.append(re.findall(pattern, text))
for n in range(len(phone_no)):
    if len(phone_no[n]) == 10:
        final_list ="".join(str(x) for x in phone_no[n])
        print(final_list)
