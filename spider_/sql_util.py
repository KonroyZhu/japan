from mysql import connector

def connect():
    config = {
        'host': 'rm-wz90561i7g5g8539c2o.mysql.rds.aliyuncs.com',
        'user': 'root',
        'password': 'NewsSpider2018',
        'port': 3306,
        'database': 'czjtest',
        'charset': 'utf8'
    }

    try:
        cnn=connector.connect(**config)
    except connector.Error as e:
        print('connect fails!{}'.format(e))
    cursor = cnn.cursor()
    cursor


connect()

