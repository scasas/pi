from reportlab.lib.pagesizes import landscape, A4, LEGAL, portrait

def pdf2():
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm, cm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    # from reportlab.lib.pagesizes import landscape, A4, LEGAL
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from uuid import uuid4
    from cgi import escape
    import os

    c = canvas.Canvas("canvas_page_num.pdf")

    for i in range(5):
        page_num = c.getPageNumber()
        text = "This is page %s" % page_num
        c.drawString(100, 750, text)
        c.showPage()
        c.save()

def pdf(data, title, page):
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm, cm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    # from reportlab.lib.pagesizes import landscape, A4, LEGAL
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from uuid import uuid4
    from cgi import escape
    import os

    heading = "Areas: "
    # text = 'bla '* 100

    styles = getSampleStyleSheet()
    
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    

    # portrait | landscape
    # A4 | LEGAL
    doc = SimpleDocTemplate(
        tmpfilename
        , pagesize=page['orientation'](page['size']) 
        , rightMargin=1*cm, leftMargin=1*cm, topMargin=1.5*cm, bottomMargin=0.5*cm
        )
    
    story = []
    story.append(Paragraph(escape(title),styles["Title"]))
    story.append(Paragraph(escape(heading),styles["Heading2"]))
    # story.append(Paragraph(escape(text),styles["Normal"]))
    # story.append(Spacer(1,0.5*inch))
    # story.append(PageBreak())

    t=Table(data)
    t.setStyle(
            TableStyle(
                [
                    # ('ALIGN',(1,1),(-2,-2),'RIGHT'),
                    # ('ALIGN',(1,1),(-2,-2),'RIGHT'),
                    # ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                    # ('VALIGN',(0,0),(0,-1),'TOP'),
                    # ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                    # ('ALIGN',(3,1),(3,-1),'RIGHT'), #pc col ram
                    # ('ALIGN',(4,1),(4,-1),'RIGHT'), #pc col disco
                    ('ALIGN',(0,0),(-1,0),'CENTER'),
                    ('ALIGN',(0,1),(0,-1),'CENTER'),
                    # ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    # ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                    ('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                    # ('BACKGROUND',(0,0),(0,-1),colors.white),
                ]
            )
        )
    # tblStyle.add
    # tblStyle.add
 
    story.append(t)
    
    doc.build(story)#, onFirstPage=drawPage, onLaterPages=drawPage)

    # doc.setAuthor("Author")
    # doc.setCreator("Creator")
    # doc.setTitle("Title")
    # doc.setSubject("Subject") # This sets description!
    # doc.setKeywords(["Keyword1", "Keyword2"])

    data = open(tmpfilename,"rb").read()

    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']= 'inline; filename=report.pdf'
    return data

def draw_page(self, page_count):
        self.setFont("Helvetica", 7)
        self.drawRightString(200*mm, 20*mm,
            "Page %d of %d" % (self._pageNumber, page_count))


# LISTADOS ===================================================================================

def list_agentes():

    data = [['Item', 'APELLIDO', 'NOMBRES', 'AREA']]
    agentes = db(Agentes).select(orderby=Agentes.apellido|Agentes.nombres)    

    page = {}
    page['size'] = LEGAL
    page['orientation'] = portrait

    i=0
    for reg in agentes:
        i=i+1
        data.append([
            i
            , reg.apellido.upper()
            , reg.nombres.upper()
            , reg.area_id.nombre
            ])

    return pdf(data, 'Listado de Agentes', page)

def list_pc():

    from applications.pi.modules.tools import *

    pc = db(Pc).select()

    page = {}
    page['size'] = A4
    page['orientation'] = landscape

    aux = []
    i=0
    for reg in pc:
        i=i+1

        aux.append([
            i
            , control_microprocesador_id(reg)
            , control_placa_madre_id(reg)
            , reg.disco + ' GB'
            , reg.memoria + ' MB'
            , reg.so
            , reg.area_id.nombre
            , control_reponsable_id(reg)
            ])

    aux = sorted(aux, key=lambda x:x[6])#, reverse=True)

    data = []
    data = [['Item', 'Microprocesador', 'Placa Madre', 'Ram', 'Disco', 'S.O.', 'Area', 'Responsable']]
    data = data + aux

    return pdf(data, 'Listado de PCs', page)


def list_monitores():

    from applications.pi.modules.tools import *

    data = [['Item', 'MONITOR', 'AREA', 'RESPONSABLE', 'ESTADO']]
    monitores = db(Stock_monitores).select()

    page = {}
    page['size'] = A4
    page['orientation'] = portrait

    i=0
    for reg in monitores:
        i=i+1

        data.append([
            i
            , reg.monitor_id.marca_id.nombre + ' ' + reg.monitor_id.modelo
            , reg.area_id.nombre
            , control_reponsable_id(reg)
            , reg.estado
            ])

    return pdf(data, 'Listado de Monitores', page)

def list_impresoras():

    from applications.pi.modules.tools import *

    pc = db(Stock_impresoras).select()

    page = {}
    page['size'] = A4
    page['orientation'] = portrait

    aux = []
    i=0
    for reg in pc:
        i=i+1

        aux.append([
            i
            , reg.impresora_id.marca_id.nombre + ' ' + reg.impresora_id.modelo
            , reg.area_id.nombre
            , control_reponsable_id(reg)
            , reg.estado
            ])

    
    aux = sorted(aux, key=lambda x:x[1])#, reverse=True)

    data = []
    data = [['Item', 'IMPRESORA', 'AREA', 'RESPONSABLE', 'ESTADO' ]]
    data = data + aux


    return pdf(data, 'Listado de Impresoras', page)

def list_ups_estabilizador():

    from applications.pi.modules.tools import *

    pc = db(Stock_ups_estabilizador).select()

    page = {}
    page['size'] = A4
    page['orientation'] = portrait

    aux = []
    i=0
    for reg in pc:
        i=i+1

        aux.append([
            i
            , reg.ups_estabilizador_id.marca_id.nombre + ' '  + reg.ups_estabilizador_id.modelo
            , reg.estado
            , reg.area_id.nombre
            , control_reponsable_id(reg)
            ])

    aux = sorted(aux, key=lambda x:x[3])#, reverse=True)

    data = []
    data = [['Item', 'Dispositivo', 'Estado', 'Area', 'Responsable']]
    data = data + aux

    return pdf(data, 'Listado de UPS | Estabilizadores', page)