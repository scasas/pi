@auth.requires_login()
def pedidos():
    # ABM & Consulta 
    grid = SQLFORM.grid(Pedidos, csv=False)
        

    return dict(
        grid = grid
        )