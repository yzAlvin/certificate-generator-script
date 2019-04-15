from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image
import csv

data = 'data.csv'

def import_data(data):
    student = csv.reader(open(data,"r"))
    for row in student:
        surname = row[0]
        firstname = row[1]
        level = row[2]
        group = row[3]
        date = row[4]
        pdf_filename = level + '_' + surname + firstname + '.pdf'
        generate_certificate(firstname, surname, level, group, date, pdf_filename)

def generate_certificate(firstname, surname, level, group, date, pdf_filename):
    student_name = firstname + ' ' + surname
    c = canvas.Canvas(pdf_filename, pagesize=portrait(A5))

    #template
    template = 'template.png'
    c.drawImage(template, 0,0, width=None, height=None)
    #name
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(215, 310, student_name)
    #level
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(178, 215, level)
    #group
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(155, 190, group)
    #date
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(105, 100, date)

    #save
    c.showPage()
    print('writing')
    c.save()

import_data(data)
