from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('fact',__name__, url_prefix='/fact')

@bp.route('/new')
def new():
  return render_template('new.html')