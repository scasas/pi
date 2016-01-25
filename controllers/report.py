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
