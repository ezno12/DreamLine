from app.app import db


class Dreams(db.Model):
    __tablename__ = "dreams"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    dream = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),autoincrement=True, nullable=False)