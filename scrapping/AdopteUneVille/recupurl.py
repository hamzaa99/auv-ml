import mysql.connector


def recuplistvilleformat():
    # variables de connections a la bd
    host = "localhost"
    user = "nassim"
    passwd = "pass"
    db = "projetml"

    # Connexion a la bd
    conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=db)
    cursor = conn.cursor()

    cursor.execute('''SELECT slug, insee_code FROM cities''')

    res = cursor.fetchall()

    tabCities = []

    for x in res:
        s = ''
        i = 0
        for item in x:
            if i == 0:
                s = s + item
            if i == 1 and item is not None:
                s = s + '_' + f'{item}'
                s = s.replace(" ", "-")
                tabCities.append(s)
            i = i + 1
    return tabCities

def constructurls():
    tab = recuplistvilleformat()
    tabUrl = []
    for x in tab:
        tabUrl.append('https://www.ville-ideale.fr/'+x)
    return tabUrl


