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
        , orderby=Marcas.nombre
        , csv=False
        , showbuttontext=False
        )
    return dict(grid=grid, titulo=titulo, button="marcas")

## PC -------------------------------------------------------------------------
@auth.requires_login()
def microprocesadores():
    titulo = 'Microprocesadores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Microprocesadores, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo, button="microprocesadores")

@auth.requires_login()
def placa_madre():
    titulo = 'Placa Madre'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Placa_madre
        , orderby=Placa_madre.marca_id | Placa_madre.modelo
        , csv=False
        , showbuttontext=False
        )
    return dict(grid = grid, titulo = titulo, button="placa_madre")

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


## PORTATILES ------------------------------------------------------------------
@auth.requires_login()
def portatiles():
    grid = SQLFORM.grid(Portatiles, csv=False, showbuttontext=False)
    return dict(grid = grid)

## IMPRESORAS ------------------------------------------------------------------
@auth.requires_login()
def impresoras():
    titulo = 'Impresoras'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Impresoras
        , orderby=Impresoras.marca_id | Impresoras.modelo
        , csv=False
        , showbuttontext=False
        )
    return dict(
        grid = grid
        , titulo = titulo
        , button="impresoras"
        )

@auth.requires_login()
def impresoras_insumos():
    titulo = 'Impresoras | Insumos'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Impresoras_insumos, csv=False, showbuttontext=False)
    return dict(grid = grid, titulo = titulo)

@auth.requires_login()
def stock_impresoras():
    grid = SQLFORM.grid(Stock_impresoras
        , orderby=db.stock_impresoras.impresora_id
        , csv=False
        , showbuttontext=False
        )

    return dict(grid = grid)#, form=form)


## MONITORES -------------------------------------------------------------------
@auth.requires_login()
def monitores():
    titulo = 'Monitores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Monitores
        , orderby=Monitores.marca_id | Monitores.modelo
        , csv=False
        , showbuttontext=False)
    return dict(grid = grid, titulo = titulo, button="monitores")

@auth.requires_login()
def stock_monitores():
    grid = SQLFORM.grid(
        Stock_monitores
        , fields = [
            Stock_monitores.identificador
            , Stock_monitores.monitor_id
            , Stock_monitores.responsable_id
            , Stock_monitores.area_id
            , Stock_monitores.estado
        ]
        # , orderby=Stock_monitores.monitor_id
        , csv=False
        , showbuttontext=False
        , maxtextlength=30
        )
    return dict(grid = grid)

## UPS | ESTABILIZADOR ---------------------------------------------------------
@auth.requires_login()
def ups_estabilizador():
    titulo = 'UPS | Estabilizadores'
    response.view = 'equipos/dispositivos.html'
    grid = SQLFORM.grid(Ups_estabilizador
        , orderby=Ups_estabilizador.marca_id | Ups_estabilizador.modelo
        , csv=False
        , showbuttontext=False
        )
    return dict(grid = grid, titulo = titulo, button="ups_estabilizador")

@auth.requires_login()
def stock_ups_estabilizador():
    grid = SQLFORM.grid(Stock_ups_estabilizador
        , fields = [
            Stock_ups_estabilizador.ups_estabilizador_id
            , Stock_ups_estabilizador.responsable_id
            , Stock_ups_estabilizador.area_id
            , Stock_ups_estabilizador.estado
        ]
        # , orderby=Stock_ups_estabilizador.ups_estabilizador_id.marca_idself.
        , csv=False
        , showbuttontext=False
        )
    return dict(grid = grid)
