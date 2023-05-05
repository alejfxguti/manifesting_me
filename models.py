from app import db

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    completed = db.Column(db.Boolean, default=False)
    daily = db.Column(db.Boolean, default=False)
    weekly = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Goal {self.name}>'
