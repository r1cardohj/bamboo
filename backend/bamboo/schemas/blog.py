from apiflask import Schema
from apiflask.fields import String, Integer, List, DateTime
from apiflask.validators import Length


class BlogIn(Schema):
    site_id = Integer(required=True)
    authors = List(Integer())
    title = String(required=True, validate=Length(0, 255))
    path = String(required=True)
    content = String(required=True)


class BlogOut(Schema):
    id = String()
    site_id = Integer()
    authors = List(Integer())
    path = String()
    content = String()
    update_at = DateTime()
    create_at = DateTime()
