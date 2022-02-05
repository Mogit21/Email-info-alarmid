import sqlite3


def queryidtable(idinput):
    """This function gets input as a string of NEIDs separated by comma, example:
    "10,11,25" ,connect to db,then create and send a query to id table and returns 
    all data for the NEID(s) as a list of tuples, one tuple containing data for each NEID"""
    
    idmultinput = (idinput).split(',')
    idmulti = [int(x) for x in idmultinput] 
    idmultinput=tuple(idmultinput) 
    
    connection = sqlite3.connect("info-alarmid-db.db")
    cursor = connection.cursor()
    
    if len (idmultinput) >1:
        cursor.execute (f"SELECT * FROM id WHERE id IN {idmultinput}")
        result = cursor.fetchall()
    else:
        idmultinput=str(idmultinput[0])
        cursor.execute (f"SELECT * FROM id WHERE id = {idmultinput}")
        result = cursor.fetchall()
        
    connection.commit()
    connection.close()
    return result


result = queryidtable("10,15,16")
def datalisted(result,x):
    """This function create a list of data related to NEID(s) such as 
    names, ipaddresses and offices
    input is result of queryidtable() or queryregiontable()
    output is a list of specific data, ex: names, ipaddresses ..."""
    listnames=[]
    for i, v in enumerate(result):
            listnames.append(v[x])
    return (listnames) 


def datatext(datalist):
    """This function converts the data list to string values
    separated by commas (,)"""

    s = ","
    datatext = s.join(datalist)
    return datatext


def queryregiontable(offices):
    """This function has a tuple of distinct offices as input
    and create and send a query to id table and returns all owners data for the office(s)"""
    
    connection = sqlite3.connect("info-alarmid-db.db")
    cursor = connection.cursor()
    
    if len (offices) > 1:
            cursor.execute (f"SELECT * FROM region WHERE office IN {offices}")
            rgresult = cursor.fetchall()
    else:
        oneoffice=offices[0]
        cursor.execute (f"SELECT * FROM region WHERE office = '{oneoffice}'")
        rgresult = cursor.fetchall()
        
    connection.commit()
    connection.close()
    return rgresult