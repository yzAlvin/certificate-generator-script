from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
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
        pdf_filename = level + '_' + surname + firstname + '.pdf'
        generate_certificate(firstname, surname, level, group, pdf_filename)

def generate_certificate(firstname, surname, level, group, pdf_filename):
    student_name = firstname + ' ' + surname
    c = canvas.Canvas(pdf_filename, pagesize=landscape(letter))

    #header
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, "Certificate of Completion")
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 450, "This certificate is presented to:")
    #student
    c.setFont('Helvetica-Bold', 34, leading=None)
    c.drawCentredString(415,395, student_name)
    #for achieving
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 350, "for achieving group:")
    #group
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415,310, group)
    #in level..
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415,270, "in level:")
    #level
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 230, level)

    #image
    seal = 'seal.png'
    c.drawImage(seal, 40,50, width=None, height=None)

    c.showPage()
    print('writing')
    c.save()

import_data(data)
