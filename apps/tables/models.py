from apps import db 

class PageItems(db.Model):
    __tablename__ = 'page_items'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    items_per_page = db.Column(db.Integer, default=25)


class HideShowFilter(db.Model):
    __tablename__ = 'hide_show_filter'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Boolean, default=False)

class ModelFilter(db.Model):
    __tablename__ = 'model_filter'
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(255), nullable=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)