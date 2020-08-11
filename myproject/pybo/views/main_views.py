from flask import Blueprint,render_template
from pybo.models import Question
bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_l.html', question_l=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    q=Question.query.get_or_404(question_id)
    return render_template('question/question_d.html',question=q)
