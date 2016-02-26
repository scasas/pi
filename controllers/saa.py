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

@auth.requires_login()
def stock():
    titulo = 'Stock de Articulos a la fecha'
    # response.view = 'load.html'

    query = 'SELECT articulo_id, nombre, sum(cantidad) FROM pi.stock_articulos group by articulo_id'

    grid = db.executesql(query)

    return dict(grid = grid, titulo=titulo)    