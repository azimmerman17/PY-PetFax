from flask import ( Blueprint, render_template, request, redirect )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('fact',__name__, url_prefix='/fact')

@bp.route('/new')
def new():
  return render_template('fact/new.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    print(request.form)
    return redirect('/fact')

  return 'Thanks for submiting a facts index'