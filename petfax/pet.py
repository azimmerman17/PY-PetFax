from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet',__name__, url_prefix='/pets')

@bp.route('/')
def index():
  return render_template('index.html', pets=pets)


@bp.route('/<int:index>')
def show(index):
  pet = pets[index - 1]
  return render_template('show.html', pet=pet)