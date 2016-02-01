@auth.requires_login()
def dashboard():
    return dict()

@auth.requires_membership('admin')
def panel_user():
    response.view = 'admin/panel_control.html'
    grid = SQLFORM.grid(db.auth_user, csv=False, showbuttontext=False)
    return dict(grid = grid)

@auth.requires_membership('admin')
def panel_group():
    response.view = 'admin/panel_control.html'
    grid = SQLFORM.grid(db.auth_group, csv=False, showbuttontext=False)
    return dict(grid = grid)

@auth.requires_membership('admin')
def panel_membership():
    response.view = 'admin/panel_control.html'
    grid = SQLFORM.grid(db.auth_membership, csv=False, showbuttontext=False)
    return dict(grid = grid)

@auth.requires_membership('admin')
def panel_permission():
    response.view = 'admin/panel_control.html'
    grid = SQLFORM.grid(db.auth_permission, csv=False, showbuttontext=False)
    return dict(grid = grid)

@auth.requires_membership('admin')
def panel_sessiones():
    response.view = 'admin/panel_control.html'
    grid = SQLFORM.grid(db.web2py_session_secviv_equipos
        , fields=[
            db.web2py_session_secviv_equipos.client_ip
            , db.web2py_session_secviv_equipos.created_datetime
        ]
        , create=False
        , deletable=False
        , editable=False
        , details=False
        , csv=False)
    return dict(grid=grid)

@auth.requires_membership('admin')
def panel_control():
    grid = False
    value = request.args(0)

    if request.args(0):

        if request.args(0) == 'user':
            grid = SQLFORM.grid(db.auth_user, csv=False)
        elif request.args(0) == 'group':
            grid = SQLFORM.grid(db.auth_group, csv=False)
        elif request.args(0) == 'membership':
            grid = SQLFORM.grid(db.auth_membership, csv=False)
        elif request.args(0) == 'permission':
            grid = SQLFORM.grid(db.auth_permission, csv=False)
        elif request.args(0) == 'marcas':
            grid = SQLFORM.grid(db.auth_permission, csv=False)

    return dict(grid = grid, value = value)