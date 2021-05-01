from supports.response_module import *
from django.db import connection as conn


# Query function to delete if specific role comes as 1 or 2 other role discared
def query_delete_specific_role(role_id, sql):
    if role_id == 1 or role_id == 2:
        if conn:
            with conn.cursor() as cursor:
                try:
                    for each_sql in sql:
                        cursor.execute(each_sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err

        else:
            return response_nodbconn()
    else:
        return response_unauthorised()
