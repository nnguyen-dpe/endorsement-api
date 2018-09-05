from database import db
from sqlalchemy import desc

class Endorsement(db.Model):
    """Relational model for Endorsement"""
    __tablename__ = 'endorsement'
    developer = db.Column(db.String, primary_key=True)
    skill = db.Column(db.String, primary_key=True)
    count = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, developer, skill):
        self.developer = developer
        self.skill = skill
        self.count = 0

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def up_vote(self):
        self.count += 1
    
    def down_vote(self):
        self.count -= 1
        if self.count < 0:
            self.count = 0

    @staticmethod
    def get_all(developerId=None, skill=None):
        query = None
        if developerId:
            query = Endorsement.query.filter(Endorsement.developer==developerId)
        if skill:
            query = Endorsement.query.filter(Endorsement.skill == skill)

        if query == None:
            return Endorsement.query.order_by(desc(Endorsement.date_modified)).all()
        else:
            return query.order_by(desc(Endorsement.date_modified)).all()
    
    @staticmethod
    def get_one(developerId, skill):
        return Endorsement.query.filter(
            Endorsement.developer==developerId, 
            Endorsement.skill==skill
        ).first()

    def __repr__(self):
        return "<Endorsement: {}>".format(self.developer)



