import psycopg2


def pg_connection(database):
    try:
        connection = psycopg2.connect(dbname=database['default']['NAME'],
                                      user=database['default']['USER'],
                                      password=database['default']['PASSWORD'],
                                      host=database['default']['HOST'],
                                      port=database['default']['PORT'])
        return connection

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
