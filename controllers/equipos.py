## MARCAS ---------------------------------------------------------------------
@auth.requires_membership('admin')
def marcas():
    titulo = 'Marcas'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Marcas
        # , fields=[
        #     db.web2py_session_secviv_equipos.client_ip
        #     , db.web2py_session_secviv_equipos.created_datetime
        # ]
        # , create=False
        # , deletable=False
        # , editable=False
        # , details=False
        , csv=False
        , showbuttontext=False
        )
    return dict(grid=grid, titulo=titulo)

## PC -------------------------------------------------------------------------
@auth.requires_login()
def microprocesadores():
    titulo = 'Microprocesadores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Microprocesadores, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

# @auth.requires_login()
# def load():
    # form = SQLFORM(Microprocesadores)
    # if form.process().accepted:
    #     title = 'form accepted'
    # elif form.errors:
    #     title = 'form has errors'
    # else:
    #     title = 'please fill out the form'
    # return dict(form=form, title=title)
    # #return dict(grid = grid)

@auth.requires_login()
def placa_madre():
    titulo = 'Placa Madre'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Placa_madre, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)


@auth.requires_login()
def pc():
    from applications.pi.modules.modal import Modal

    field1 = db.pc.microprocesador_id
    field2 = db.pc.placa_madre_id
    
    modal1 = Modal(field1, 'Agregar', 'Haciendo clic, podes agregar un micro', 'MICRO')
    modal2 = Modal(field2, 'Agregar', 'Haciendo clic, podes agregar una motherboard', 'MADRE')

    db.pc.microprocesador_id.comment = modal1.create()
    db.pc.placa_madre_id.comment = modal2.create()    
    
    grid = SQLFORM.grid(Pc, csv=False, showbuttontext=False)

    return dict(
        grid = grid
        , micro_modal=modal1.formModal()
        , madre_modal=modal2.formModal()
        )

@auth.requires_login()
def portatiles():
    # titulo = 'Portatiles'
    # response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Portatiles, csv=False, showbuttontext=False)
    return dict(grid = grid)#, titulo = titulo)

## IMPRESORAS ------------------------------------------------------------------
@auth.requires_login()
def impresoras():
    titulo = 'Impresoras'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Impresoras, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

@auth.requires_login()
def impresoras_insumos():
    titulo = 'Impresoras | Insumos'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Impresoras_insumos, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

@auth.requires_login()
def stock_impresoras():
    grid = SQLFORM.grid(Stock_impresoras, csv=False, showbuttontext=False)
    # form = SQLFORM(Stock_impresoras)


    # if form.accepts(request.vars, session):
    #     response.flash = 'Guardado Correctamente'
    # elif form.errors:
    #     response.flash = 'No se pudo Guardar'

    return dict(grid = grid)#, form=form)


## MONITORES -------------------------------------------------------------------
@auth.requires_login()
def monitores():
    titulo = 'Monitores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Monitores, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

@auth.requires_login()
def stock_monitores():
    grid = SQLFORM.grid(
        Stock_monitores
        , fields = [
            Stock_monitores.monitor_id
            , Stock_monitores.responsable_id
            , Stock_monitores.area_id
            , Stock_monitores.estado
        ]
        , csv=False
        , showbuttontext=False
        )
    return dict(grid = grid)

## UPS | ESTABILIZADOR ---------------------------------------------------------
@auth.requires_login()
def ups_estabilizador():
    titulo = 'UPS | Estabilizadores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Ups_estabilizador, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

@auth.requires_login()
def stock_ups_estabilizador():
    grid = SQLFORM.grid(Stock_ups_estabilizador, csv=False)
    return dict(grid = grid)
