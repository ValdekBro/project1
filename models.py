from UsersDB import sqldb, nosqldb

# class user
class User(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    name = sqldb.Column(sqldb.String(50))
    password = sqldb.Column(sqldb.String(50))

class Note(nosqldb.Document):
    date = nosqldb.DateTimeField()
    comment = nosqldb.StringField()

class Counter(nosqldb.Document):
    added = nosqldb.IntField()
    deleted = nosqldb.IntField()
    edited = nosqldb.IntField()

LogCount = Counter.query.first()
