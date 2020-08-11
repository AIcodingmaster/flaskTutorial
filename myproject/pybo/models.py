from pybo import db#__init__.py를 의미

class Question(db.Model):
    id=db.Column(db.Integer, primary_key=True)#주된 키
    subject=db.Column(db.String(200),nullable=False)
    conent=db.Column(db.Text(),nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

