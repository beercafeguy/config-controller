from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.String(50), unique=True, nullable=False)
    model_id = db.Column(db.String(50), nullable=False)

    def __init__(self, candidate_id, model_id):
        self.candidate_id = candidate_id
        self.model_id = model_id