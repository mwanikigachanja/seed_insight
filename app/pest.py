from flask import Blueprint, render_template, request, redirect, url_for
from .models import Pest, Disease
from . import db

bp = Blueprint('pest_and_disease', __name__, url_prefix='/pest_and_disease')

@bp.route('/')
def index():
    pests = Pest.query.all()
    diseases = Disease.query.all()
    return render_template('pest_and_disease.html', pests=pests, diseases=diseases)

@bp.route('/pest/<int:id>')
def pest_details(id):
    pest = Pest.query.get_or_404(id)
    return render_template('pest_details.html', pest=pest)

@bp.route('/disease/<int:id>')
def disease_details(id):
    disease = Disease.query.get_or_404(id)
    return render_template('disease_details.html', disease=disease)
