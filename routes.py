from app import app, db
from app.models import Goal
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET'])
def index():
    daily_goals = Goal.query.filter_by(daily=True, completed=False).all()
    weekly_goals = Goal.query.filter_by(weekly=True, completed=False).all()
    return render_template('index.html', daily_goals=daily_goals, weekly_goals=weekly_goals)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    description = request.form['description']
    is_daily = True if request.form.get('daily') else False
    is_weekly = True if request.form.get('weekly') else False
    goal = Goal(name=name, description=description, daily=is_daily, weekly=is_weekly)
    db.session.add(goal)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    goal = Goal.query.get(id)
    db.session.delete(goal)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    goal = Goal.query.get(id)
    if request.method == 'POST':
        goal.name = request.form['name']
        goal.description = request.form['description']
        goal.daily = True if request.form.get('daily') else False
        goal.weekly = True if request.form.get('weekly') else False
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', goal=goal)
