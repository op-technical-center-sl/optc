# -*- coding: utf-8 -*-

import psycopg2, logging

_logger = logging.getLogger(__name__)



def consultaPostgreSQL(query=''): # Codificacion probada --> OK
    servidor = '192.168.1.221'
    usuario = 'odoo'
    password = 'Fern2963'
    bd = 'optc_sh'
    cadConexion = "dbname='%s' user='%s' host='%s' password='%s'" % (bd, usuario, servidor, password)
    #print cadConexion
    conn =''
    try:
        conn = psycopg2.connect(cadConexion)
        conn.set_client_encoding('UTF8')
    except:
        print("Error al conectar con la BD.")
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None
    cursor.close()
    conn.close()
    return(data)


sqlGetAccountMove = """select id, name
from account_move am 
where ref is not null"""

sqlInsertChatter = """INSERT INTO public.mail_message
(subject, "date", body, parent_id, model, res_id, record_name, message_type, subtype_id, mail_activity_type_id, email_from, author_id, no_auto_thread, message_id, reply_to, mail_server_id, moderation_status, moderator_id, email_layout_xmlid, add_sign, create_uid, create_date, write_uid, write_date)
select 
null subject, now() "date", CONCAT('<P> Reference: ', am.ref, '</p>') body, 
(select id from mail_message where res_id in ({ID}) order by id limit 1) parent_id,
'account.move' model, {ID} res_id, CONCAT(am.name, ' (', am.ref, ')') record_name,
'comment' message_type, 2 subtype_id, null mail_activity_type_id, '"Joaquim Antao" <joaquimantao@teamoptc.com>' email_from,
3 author_id, null no_auto_thread, '<234370989324169.1625646338.592332124710083-openerp-11757-account.move@odoo13-enterprise>' message_id,
'"OP Technical Center SL {NAME} ()" <catchall@optc.odoo.com>' reply_to, null mail_server_id, null moderation_status, 
null moderator_id, null email_layout_xmlid, true add_sign, 2 create_uid, now() create_date, 2 write_uid, now() write_date
from mail_message mm  inner join account_move am on mm.res_id = am.id
where res_id in ({ID})
limit 1"""

accountMove = consultaPostgreSQL(sqlGetAccountMove)

for l in accountMove:
    salida = []
    # _logger.info("Linea: " + str(l.encode('utf-8')))
    # print("Tipo: " + str(type(l)) + "\n")
    # print("Tipo 2: " + str(type(l[0])) + "\n")
    cadena = u' '.join([str(item) for item in l]).encode('utf-8')
    # print("Linea: " + str(cadena ) + "\n")
    s = cadena.decode()
    salida = s.split()
    id = salida[0]
    name = salida[1]
    # print("Tipo 3: " + str(type(s)) + "\n")
    # print("Linea Ok: " + str(s) + "\n")
    #_logger.info("Linea: " + str(cadena))
    sqlIns = sqlInsertChatter.replace("{ID}", id)
    sqlIns = sqlIns.replace("{NAME}", name)
    # sqlIns = sqlIns.replace("{REF}", l[2])
    outSql = consultaPostgreSQL(sqlIns)
    # _logger.info("SQL: " + sqlIns)
    print("SQL: " + sqlIns + "\n")