@auth.requires_login()
def pedidos():
    titulo = 'Control de Pedidos'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Pedidos
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
    return dict(form = grid, title=titulo)

@auth.requires_login()
def consulta():

    if request.vars.dispositivo == 'pedidos':
        grid = db(Pedidos).select()
        titulo = 'Control de Pedidos'
        response.title = 'Control de Pedidos'
        response.view = 'pedidos/consulta_pedidos.html'

    else:
        redirect(URL(c='default', f='index'))

    return dict(grid = grid, titulo=titulo)