from mongoengine import BooleanField, Document, ObjectIdField, StringField

class Todo(Document):
    _id = ObjectIdField()
    activity = StringField(required=True)
    completed = BooleanField(required=True, default=False)