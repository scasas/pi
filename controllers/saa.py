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
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def egresos_new():

    art = int(11)
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
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def stock():
    titulo = 'Stock de Articulos a la fecha'
    # response.view = 'load.html'

    query = 'SELECT articulo_id, nombre, sum(cantidad) FROM pi.stock_articulos group by articulo_id'

    grid = db.executesql(query)

    return dict(grid = grid, titulo=titulo)    