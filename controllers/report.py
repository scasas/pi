# """

#  Simple web2py controller to generate PDF documents with ReportLab.
 
#  Author: H.C. v. Stockhausen <hc at vst.io>
#  Date:   2012-10-14
 
#  Also see http://www.reportlab.com
 
# """
 
# import cStringIO
 
# from reportlab.platypus.doctemplate import SimpleDocTemplate
# from reportlab.platypus import Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
 
 
# def index():
#     """
#     To display the generated PDF in your browser go to:
#      http://.../<app>/<controller>/generate
     
#     To download it as hello.pdf, for example, instead, use:
#      http://.../<app>/<controller>/generate/hello.pdf
#     """
    
#     styles = getSampleStyleSheet()

#     story = [
#         Paragraph("Título", styles['Heading1']),
#         Paragraph("The quick brown fox", styles['Normal']),
#         Spacer(1, 0.25*inch),
#         Paragraph("jumps over the lazy dog.", styles['Normal'])
#     ]

#     buffer = cStringIO.StringIO()

#     doc = SimpleDocTemplate(buffer)
    
#     doc.build(story)

#     pdf = buffer.getvalue()
    
#     buffer.close()

#     filename = request.args(0)

#     if filename:
#         header = {'Content-Disposition': 'attachment; filename=' + filename}
#     else:
#         header = {'Content-Type': 'application/pdf'}
    
#     response.headers.update(header)
    
#     return pdf

# parque funcione en el servidor debe estar instalado el paquete xhtml2pdf
# se lo instala con:
# pip install xhtml2pdf

import StringIO
from os import path
from xhtml2pdf.pisa import CreatePDF

def index():

    response.view = 'report/index.html'

    agentes = db(Agentes).select()

    context = dict(agentes=agentes)

    if request.extension == 'pdf':
        path_css = path.join(request.env.web2py_path,'applications/pi/static/css/reporte_cert.css')
        
        with open(path_css, 'r') as rcss:
            css = rcss.read()

        html = response.render(response.view, context)
        doc = StringIO.StringIO()
        pdf = CreatePDF(html,
                        dest=doc,
                        default_css=css,
                        encoding='utf-8')
        return doc.getvalue()

def test():
    response.view = 'test.html'
    data = []
    agentes = db(Agentes).select()
    
    for reg in agentes:
        data.append(
                [
                    reg.id, reg.apellido, reg.nombres
                ]
            )
    data= [['00', '01', '02', '03', '04'],
       ['10', '11', '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]

    return dict(agentes=data)

def pdf():
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib import colors
    from uuid import uuid4
    from cgi import escape
    import os

    title = "Listado de Agentes"
    heading = "First Paragraph"
    text = 'bla '* 100

    styles = getSampleStyleSheet()
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    doc = SimpleDocTemplate(tmpfilename)
    story = []
    story.append(Paragraph(escape(title),styles["Title"]))
    story.append(Paragraph(escape(heading),styles["Heading2"]))
    story.append(Paragraph(escape(text),styles["Normal"]))
    story.append(Spacer(1,0.5*inch))
    
    # data= [['00', '01', '02', '03', '04'],
    #    ['10', '11', '12', '13', '14'],
    #    ['20', '21', '22', '23', '24'],
    #    ['30', '31', '32', '33', '34']]
    # t=Table(data)
    # t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
    #                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
    # story.append(t)

    # story.append(Spacer(1,0.5*inch))
    
    data= [['00', '01', '02', '03', '04'],
       ['10', '11', '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]

    data = []
    agentes = db(Agentes).select(orderby=Agentes.apellido|Agentes.nombres)
    size = db(Agentes).count()

    i=0
    for reg in agentes:
        i=i+1
        data.append(
                [
                    i, reg.apellido, reg.nombres
                ]
            )

    t=Table(data,3*[2*inch], size*[0.25*inch])
    t.setStyle(
            TableStyle(
                [
                    # ('ALIGN',(1,1),(-2,-2),'RIGHT'),
                    # ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                    # ('VALIGN',(0,0),(0,-1),'TOP'),
                    # ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                    # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                    # ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    # ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                ]
            )
        )
 
    story.append(t)
    
    doc.build(story)
    data = open(tmpfilename,"rb").read()

    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    return data