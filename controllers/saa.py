@auth.requires_login()
def categorias():
    titulo = 'Categorias'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Categorias
        , csv=False
        , showbuttontext=False
        , maxtextlength=30
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def articulos():
    titulo = 'Articulos'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Articulos
        , csv=False
        , showbuttontext=False
        , maxtextlength=30
        , paginate=200
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def egresos():
    titulo = 'Egresos'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Egresos
        , create=False
        , deletable=False
        , editable=False
        , csv=False
        , showbuttontext=False
        , maxtextlength=30
        , paginate=200
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def egresos_new():

    # art = int(11)
    art = int(request.vars.articulo_id)
    articulo = Articulos(art)

    query = 'SELECT articulo_id, nombre, sum(cantidad) FROM pi.stock_articulos where articulo_id=%s group by articulo_id' %art

    grid = db.executesql(query)

    # response.view = 'biblioteca/libros_prestar.html'

    form = ''

    cantidad = grid[0][2]
    if (cantidad>0):

        request.vars = ''

        form = SQLFORM.factory(
                Field('agente_id'
                      , Agentes
                      , requires=IS_IN_DB(
                        db
                        , Agentes.id
                        ,  lambda r: r.apellido.upper() + ' ' + r.nombres.upper()
                        , orderby = Agentes.apellido | Agentes.nombres
                        )
                      )
                , Field('area_id'
                    , Areas
                    , requires=IS_IN_DB(
                            db
                            , Areas.id
                            ,  lambda r: r.nombre.upper()
                            , orderby = Areas.nombre
                        )
                    )
                , Field('cantidad'
                    , 'list:string'
                    , requires=IS_IN_SET(range(1, cantidad + 1)))
                    , notnull=True
                )

        if form.accepts(request.vars, session):
            
            Egresos.insert(
                    fecha_entrega=request.now,
                    agente_id=form.vars.agente_id,
                    area_id=form.vars.area_id,
                    articulo_id=art,
                    cantidad_entregada=int(form.vars.cantidad)
                )
            db.commit()
            session.flash = 'Se entregaro %s insumos' % (form.vars.cantidad)
            redirect(URL('saa', 'stock'))

        elif form.errors:
            response.flash = 'Controle el formulario'
    else:
        session.flash = 'No hay stock disponible del articulo seleccionado' 
        redirect(URL('saa', 'stock'))

    return dict(form=form, articulo=articulo, grid=grid)

@auth.requires_login()
def ingresos():
    titulo = 'Ingresos'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Ingresos
        , csv=False
        , showbuttontext=False
        , maxtextlength=30
        , paginate=200
        , orderby = Ingresos.articulo_id
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def stock():
    from reportlab.lib.pagesizes import landscape, A4, LEGAL, portrait
    
    fecha = str(request.now.day) + '/' + str(request.now.month) + '/' + str(request.now.year)

    titulo = 'Stock de Articulos a la fecha: ' + fecha
    # response.view = 'load.html'

    query = 'SELECT articulo_id, nombre, sum(cantidad) FROM pi.stock_articulos group by articulo_id'

    grid = db.executesql(query)

    # if 'pdf' in request :
    if 'pdf' in request.args:
        # response.view = 'report/stock.html'

        data = [['Item', 'ARTICULO', 'CANTIDAD']]

        page = {}
        page['size'] = A4
        page['orientation'] = portrait

        i=0
        for reg in grid:
            i=i+1
            data.append([
                i
                , reg[1].upper()
                , reg[2]
                ])

        return pdf(data, titulo, page)
        # return dict(data=data)
    else:
        return dict(grid = grid, titulo=titulo)


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


def test():
    # columns = ['member.firstName', 'member.lastName', 'member.city',
    #            'member.state', 'member.phone', 'member.joinedOn',
    #            'member.deceased']
    # orderBy = ['member.lastName']
    grid = SQLFORM.smartgrid(Agentes

        )
    return dict(grid=grid)