from reportlab.lib.pagesizes import landscape, A4, LEGAL, portrait

def pdf2(data, page):
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm, cm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas
    from uuid import uuid4
    from cgi import escape
    import os

    styles = getSampleStyleSheet()
    
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    
    doc = SimpleDocTemplate(
        tmpfilename
        , pagesize=page['orientation'](page['size']) 
        , rightMargin=1*cm, leftMargin=1*cm, topMargin=1.5*cm, bottomMargin=0.5*cm
        )
    
    story = []

    t=Table(data)
    t.setStyle(
            TableStyle(
                [
                    ('ALIGN',(0,0),(0,-1),'RIGHT'),
                    ('ALIGN',(1,0),(1,-1),'LEFT'),
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
    response.headers['Content-Disposition']= 'inline; filename=report.pdf'
    return data

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

@auth.requires_login()
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

@auth.requires_login()
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

@auth.requires_login()
def list_portatiles():

    from applications.pi.modules.tools import *

    pc = db(Portatiles).select()

    page = {}
    page['size'] = A4
    page['orientation'] = landscape

    aux = []
    i=0
    for reg in pc:
        i=i+1

        aux.append([
            i
            , reg.tipo
            , control_microprocesador_id(reg)
            , reg.disco + ' GB'
            , reg.memoria + ' MB'
            , reg.pulgadas
            , reg.so
            , reg.unidad_optica
            , reg.area_id.nombre
            , control_reponsable_id(reg)
            ])

    aux = sorted(aux, key=lambda x:x[1])#, reverse=True)

    data = []
    data = [[
        'Item'
        , 'Tipo'
        , 'Microprocesador'
        , 'Disco'
        , 'Memoria'
        , 'Pulgadas'
        , 'SO'
        , 'Unidad Optica'
        , 'Area'
        , 'Responsable']]
    data = data + aux

    return pdf(data, 'Listado de Portatiles', page)

@auth.requires_login()
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

@auth.requires_login()
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

@auth.requires_login()
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

@auth.requires_login()
def list_pedidos():

    from applications.pi.modules.tools import *

    pedidos = db(Pedidos).select()

    page = {}
    page['size'] = LEGAL
    page['orientation'] = landscape

    aux = []
    i=0
    for reg in pedidos:
        i=i+1

        aux.append([
            i
            , reg.personal_id.apellido + ' ' + reg.personal_id.nombres
            , reg.fecha_solicitud
            , reg.problema_tipo
            , reg.problema_detalle
            , reg.problema_solucion_propuesta
            , reg.problema_estado
            , reg.personal_computos_id.apellido + ' ' + reg.personal_computos_id.nombres
            ])

    aux = sorted(aux, key=lambda x:x[3])#, reverse=True)

    data = []
    data = [['Item'
        , 'Agente'
        , 'Fecha'
        , 'Tipo de Problema'
        , 'Detalle del Problema'
        , 'Solucion Propuesta'
        , 'Estado'
        , 'Personal de Computos']]
    data = data + aux

    return pdf(data, 'Control de Pedidos', page)




@auth.requires_login()
def etiqueta():

    from applications.pi.modules.tools import *

    if request.vars.dispositivo == 'pc':
        grid = db(Pc.id == request.vars.id).select()
        aux = [
            [ 'Identificador: ', 'CPU-' + str(100+grid[0].id) ],
            [ 'Microprocesador: ', control_microprocesador_id(grid[0])],
            [ 'Placa Madre: ', control_placa_madre_id(grid[0])],
            [ 'Disco: ', grid[0].disco + ' GB'],
            [ 'Memoria: ', grid[0].memoria + ' MB'],
            [ 'SO: ', grid[0].so],
            [ 'Area: ', grid[0].area_id.nombre],
            [ 'Responsable: ', control_reponsable_id(grid[0])],
        ]

    elif request.vars.dispositivo == 'impresoras':
        grid = db(Stock_impresoras.id == request.vars.id).select()
        aux = [
            [ 'Identificador: ', 'IMP-' + str(100+grid[0].id) ],
            [ 'Impresora: ', grid[0].impresora_id.marca_id.nombre + ' ' + grid[0].impresora_id.modelo],
            [ 'Area: ', grid[0].area_id.nombre],
            [ 'Responsable: ', control_reponsable_id(grid[0])],
        ]

    elif request.vars.dispositivo == 'monitores':
        grid = db(Stock_monitores.id == request.vars.id).select()
        aux = [
            [ 'Identificador: ', 'MON-' + str(100+grid[0].id) ],
            [ 'Monitor: ', grid[0].monitor_id.marca_id.nombre + ' ' + grid[0].monitor_id.modelo ],
            [ 'Area: ', grid[0].area_id.nombre],
            [ 'Responsable: ', control_reponsable_id(grid[0])],
        ]

    elif request.vars.dispositivo == 'portatiles':
        grid = db(Portatiles.id == request.vars.id).select()
        aux = [
            [ 'Identificador: ', 'POR-' + str(100+grid[0].id) ],
            [ 'Tipo: ', grid[0].tipo],
            [ 'Marca: ', grid[0].marca_id.nombre],
            [ 'Modelo: ', grid[0].modelo],
            [ 'Microprocesador: ', control_microprocesador_id(grid[0])],
            [ 'Memoria RAM: ', grid[0].memoria + ' MB'],
            [ 'Capacidad de Disco: ', grid[0].disco + ' GB'],
            [ 'Pulgadas: ', grid[0].pulgadas + '"'],
            [ 'SO: ', grid[0].so],
            [ 'Area: ', grid[0].area_id.nombre],
            [ 'Responsable: ', control_reponsable_id(grid[0])],
        ]

    elif request.vars.dispositivo == 'ups_estabilizador':
        grid = db(Stock_ups_estabilizador.id == request.vars.id).select()
        aux = [
            [ 'Identificador: ', 'U_E-' + str(100+grid[0].id) ],
            [ 'Dispositivo: ', grid[0].ups_estabilizador_id.marca_id.nombre + ' ' + grid[0].ups_estabilizador_id.modelo ],
            [ 'Estado: ', grid[0].estado],
            [ 'Area: ', grid[0].area_id.nombre],
            [ 'Responsable: ', control_reponsable_id(grid[0])],
        ]

    else:
        redirect(URL(c='default', f='index'))

    # return dict(grid = grid)
    page = {}
    page['size'] = A4
    page['orientation'] = portrait

    

    return pdf2(aux, page)