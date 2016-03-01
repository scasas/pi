@auth.requires(auth.has_membership('admin') or \
               auth.has_membership('computos'))
def equipos():
    # response.view='generadores/listado.html'
    response.title = ' Listado Completo '
    response.subtitle = ' - app PI'
    return dict(tipo='listado')

@auth.requires(auth.has_membership('admin') or \
               auth.has_membership('computos'))
def get_data():

    query="""
        select * from pc
        """ 

    # if (request.vars['tipo'] == 'patogenicos'):
    #     query += " WHERE generadores.tipo_generador<>1 "

    # if (request.vars['tipo'] == 'peligrosos'):
    #     query += " WHERE generadores.tipo_generador=1 "

    query += """

                """ 


    iTotalRecords='select count(id) from pc;'
    iTotalDisplayRecords = iTotalRecords
    custdata = {}
    custdata['aaData'] = db.executesql(query)
    custdata['iTotalRecords']=db.executesql(iTotalRecords)[0][0]
    custdata['iTotalDisplayRecords']=db.executesql(iTotalDisplayRecords)[0][0]
    custdata['sEcho']=1

    return response.json(custdata)