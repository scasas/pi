@auth.requires_login()
def categorias():
    titulo = 'Categorias'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Categorias
        , csv=False
        , showbuttontext=False
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
    )
    return dict(form = grid, title=titulo)

@auth.requires_login()
def egresos():
    titulo = 'Entregas'
    response.view = 'load.html'
    # ABM & Consulta 
    grid = SQLFORM.grid(Egresos
        , csv=False
        , showbuttontext=False
    )
    return dict(form = grid, title=titulo)

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
