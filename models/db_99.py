# LABELS    -------------------------------------------------------------------- 

# # Agentes
Agentes.area_id.label = 'Area'

# PC
Pc.responsable_id.label = 'Responsable'
Pc.area_id.label = 'Area'
Pc.microprocesador_id.label = 'Microprocesador'
Pc.placa_madre_id.label = 'Placa Madre'
Pc.disco.label = 'Capacidad de Disco (GB)'
Pc.memoria.label = 'Capacidad de Memoria (Mb)'
Pc.so.label = 'Sistema Operativo'

# Portatiles
Portatiles.responsable_id.label = 'Responsable'
Portatiles.area_id.label = 'Area'
Portatiles.marca_id.label = 'Marca'
Portatiles.microprocesador_id.label = 'Microprocesador'
Portatiles.disco.label = 'Capacidad de Disco (GB)'
Portatiles.memoria.label = 'Capacidad de Memoria (Mb)'
Portatiles.tipo.label = 'Tipo de Portatil'
Portatiles.so.label = 'Sistema Operativo'

# Monitores
Stock_monitores.monitor_id.label = 'Monitor'
Stock_monitores.responsable_id.label = 'Responsable'
Stock_monitores.area_id.label = 'Area'

# Impresoras
Stock_impresoras.impresora_id.label = 'Impresora'
Stock_impresoras.responsable_id.label = 'Responsable'
Stock_impresoras.area_id.label = 'Area'

# # UPS | Estabilizador
# Stock_ups_estabilizador.ups_estabilizador_id.label = 'Dispositivo'
# Stock_ups_estabilizador.responsable_id.label = 'Responsable'
# Stock_ups_estabilizador.area_id.label = 'Area'


# # Pedidos
# Pedidos.problema_tipo.label = 'Tipo de Problema'
# Pedidos.problema_detalle.label = 'Detalle del Problema'
# Pedidos.problema_solucion_propuesta.label = 'Solucion Propuesta'
# Pedidos.problema_estado.label = 'Estado'
# Pedidos.fecha_solicitud.label = 'Fecha'
# Pedidos.personal_id.label = 'Personal'


# REQUIRES ---------------------------------------------------------------------

# # PC
Pc.microprocesador_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Microprocesadores.id, lambda r: r.marca_id.nombre + ' ' + r.modelo + ' ' + r.frecuencia_trabajo + ' Ghz', orderby = Microprocesadores.marca_id | Microprocesadores.modelo ))
Pc.placa_madre_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Placa_madre.id,  lambda r: r.marca_id.nombre + ' ' + r.modelo, orderby = Placa_madre.marca_id | Placa_madre.modelo))
Pc.responsable_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Agentes.id,  lambda r: r.apellido.upper() + ' ' + r.nombres.upper(), orderby = Agentes.apellido | Agentes.nombres))

# Portatiles
Portatiles.responsable_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Agentes.id,  lambda r: r.apellido.upper() + ' ' + r.nombres.upper(), orderby = Agentes.apellido | Agentes.nombres))
Portatiles.microprocesador_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Microprocesadores.id, lambda r: r.marca_id.nombre + ' ' + r.modelo + ' ' + r.frecuencia_trabajo + ' Ghz', orderby = Microprocesadores.marca_id | Microprocesadores.modelo ))


# Placa Madre ------------------------------------------------------------------
Placa_madre.marca_id.requires = IS_IN_DB(db(db.tab_marcas.placa_madre == True), Marcas.id, '%(nombre)s')

# Microprocesadores
Microprocesadores.marca_id.requires = IS_IN_DB(db(db.tab_marcas.microprocesador == True), Marcas.id, '%(nombre)s')

# Monitores
Monitores.marca_id.requires = IS_IN_DB(db(db.tab_marcas.monitor == True), Marcas.id, '%(nombre)s')
Stock_monitores.responsable_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Agentes.id,  lambda r: r.apellido.upper() + ' ' + r.nombres.upper(), orderby = Agentes.apellido | Agentes.nombres))
Stock_monitores.monitor_id.requires = IS_IN_DB(db, Monitores.id,  lambda r: r.marca_id.nombre.upper() + ' ' + r.modelo.upper(), orderby = Monitores.marca_id | Monitores.modelo)

# Impresoras
Impresoras.marca_id.requires = IS_IN_DB(db(db.tab_marcas.impresora == True), Marcas.id, '%(nombre)s')
Stock_impresoras.responsable_id.requires = IS_EMPTY_OR(IS_IN_DB(db, Agentes.id,  lambda r: r.apellido.upper() + ' ' + r.nombres.upper(), orderby = Agentes.apellido | Agentes.nombres))
Stock_impresoras.impresora_id.requires = IS_IN_DB(db, Impresoras.id,  lambda r: r.marca_id.nombre.upper() + ' ' + r.modelo.upper(), orderby =~ Impresoras.marca_id | Impresoras.modelo, error_message='Debes seleccionar una impresora')

# UPS | Estabilizadore
Ups_estabilizador.marca_id.requires = IS_IN_DB(db(db.tab_marcas.ups_estabilizador == True), Marcas.id, '%(nombre)s')



# WRITABLE ---------------------------------------------------------------------
Stock_impresoras.identificador.writable = False

# Readable ---------------------------------------------------------------------
Stock_impresoras.id.readable = True