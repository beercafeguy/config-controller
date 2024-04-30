from flask import render_template, request, redirect, url_for
from .models import db, Candidate
from . import app

@app.route('/')
def index():
    candidates = Candidate.query.all()
    return render_template('index.html', candidates=candidates)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    candidate_id = request.form['candidate_id']
    model_id = request.form['model_id']
    candidate = Candidate(candidate_id=candidate_id, model_id=model_id)
    db.session.add(candidate)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_candidate/<int:id>', methods=['GET', 'POST'])
def edit_candidate(id):
    candidate = Candidate.query.get_or_404(id)
    if request.method == 'POST':
        candidate.candidate_id = request.form['candidate_id']
        candidate.model_id = request.form['model_id']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_candidate.html', candidate=candidate)

if __name__ == '__main__':
    app.run(debug=True)