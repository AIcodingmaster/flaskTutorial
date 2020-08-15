from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from .. import db
from ..models import Question
from ..forms import QuestionForm,AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():#list는 예약어라 그냥 _ 붙인 거임.
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_l.html', question_l=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_d.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    # ---------------------------------------- [edit] ---------------------------------------- #
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, conent=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    # ---------------------------------------------------------------------------------------- #        
    return render_template('question/question_f.html', form=form)