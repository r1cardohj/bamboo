from apiflask import Schema
from apiflask.fields import String, DateTime, Integer
from apiflask.validators import Length


class PageIn(Schema):
    site_id = Integer(required=True)
    title = String(required=True, validate=Length(0, 255))
    path = String(required=True)
    content = String(required=True)


class PageOut(Schema):
    id = Integer()
    site_id = Integer()
    title = String()
    path = String()
    content = String()
    updated_at = DateTime()
    created_at = DateTime()
