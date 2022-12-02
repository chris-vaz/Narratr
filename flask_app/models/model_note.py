from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Note:
    db_name = 'narratr_db'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.note = data['note']
        self.date_of_note = data['date_of_note']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO notes (title,note,date_of_note, users_id) VALUES (%(title)s,%(note)s,%(date_of_note)s,%(users_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM sightings;"
    #     results =  connectToMySQL(cls.db_name).query_db(query)
    #     all_sightings = []
    #     for row in results:
    #         print(row['date_of_siting'])
    #         all_sightings.append( cls(row) )
    #     return all_sightings
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM notes join users on notes.users_id=users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_notes = []
        for row in results:
            note=cls(row)
            user={
                **row,
                'first_name':row['first_name'],
                'last_name':row['last_name'],
            }
            note.user=user
            all_notes.append(note)
            # print(row['date_of_siting'])
            # all_sightings.append( cls(row) )
        return all_notes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM notes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE notes SET title=%(title)s,note=%(note)s,date_of_note=%(date_of_note)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM notes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    # @classmethod
    # def get_user(cls):
    #     query = "SELECT * FROM sightings LEFT JOIN users ON sightings.users_id = users.id;"
    #     getusers =  connectToMySQL(cls.db_name).query_db(query)
    #     get_user = []
    #     for row in getusers:
    #         print(row['first_name'])
    #         c=row['first_name']
    #         get_user.append( cls(row) )
    #     return c

    @staticmethod
    def validate_note(note):
        is_valid = True
        if len(note['title']) <= 0:
            is_valid = False
            flash("Enter a great title for your story!","note")
        if note['date_of_note'] == "":
            is_valid = False
            flash("Oops! You forgot the date ","note")
        if len(note['note']) <= 0:
            is_valid = False
            flash("Narrate to us. What's up?","note")    
        return is_valid