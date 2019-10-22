from builtins import classmethod

import pymysql


class User():
    TABLE_NAME = 'users'

    def __init__(self, user_id, username, password, cpf, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.cpf = cpf
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        # Open database connection
        db = pymysql.connect("47.74.246.126", "API", "477075", "calc_ir")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        query = 'SELECT * FROM {table} WHERE username="{username}"'.format(table=cls.TABLE_NAME, username=username)
        cursor.execute(query)
        # Fetch a single row using fetchone() method.
        row = cursor.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        # disconnect from server
        db.close()
        return user

 #   @classmethod
  #  def find_by_id(cls, _id):
   #     return cls.query.filter_by(user_id=_id).first()
