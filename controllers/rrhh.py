@auth.requires_login()
def agentes():
    # ABM & Consulta de los Agentes
    grid = SQLFORM.grid(Agentes
    	, fields=[
            db.agentes.apellido
            , db.agentes.nombres
            , db.agentes.area_id
        ]
        # , create=False
        # , deletable=False
        # , editable=False
        # , details=False
        , links=[lambda r: agente_equipos(r)]
        , csv=False
        , showbuttontext=False
        )

    return dict(grid = grid)

@auth.requires_login()
def agente():
    # ABM & Consulta del equipamiento de un determinado agente
    # response.view = 'test.html'

    agente = {}

    agente['datos'] = Agentes(request.vars.id) or redirect(URL(c='rrhh', f='agentes'))

    # r = request.vars

    agente['pc'] = db(db.pc.responsable_id == request.vars.id ).select()
    agente['monitores'] = db(db.stock_monitores.responsable_id == request.vars.id ).select()
    agente['impresoras'] = db(db.stock_impresoras.responsable_id == request.vars.id ).select()
    agente['ups_estabilizador'] = db(db.stock_ups_estabilizador.responsable_id == request.vars.id ).select()
    agente['portatiles'] = {}

    # grid = SQLFORM.grid(Agentes, csv=False, showbuttontext=False)

    return dict(agente = agente)


@auth.requires_login()
def areas():
    # ABM & consulta de las areas
    grid = SQLFORM.grid(Areas
        , links=[lambda r: area_equipos(r)]
        , csv=False
        , showbuttontext=False
        )

    return dict(grid = grid)

@auth.requires_login()
def area():
    # ABM & Consulta del equipamiento de un determinado agente
    area = {}

    auxiliar = Areas(request.vars.id) or redirect(URL(c='rrhh', f='area'))
    area['nombre'] = auxiliar['nombre']

    # libro = Libro(movimiento.libro_id)
    area['pc'] = db(db.pc.area_id == request.vars.id ).select()
    area['monitores'] = db(db.stock_monitores.area_id == request.vars.id ).select()
    area['impresoras'] = db(db.stock_impresoras.area_id == request.vars.id ).select()
    area['ups_estabilizador'] = {} #db(db.stock_ups_estabilizador.area_id == request.vars.id ).select()
    area['portatiles'] = {}

    return locals()