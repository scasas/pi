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