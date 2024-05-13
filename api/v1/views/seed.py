from flask import jsonify
from models.seed import Seed

@app.route('/api/v1/seeds', methods=['GET'])
def get_seeds():
    seeds = Seed.query.all()
    seed_list = [{'name': seed.name, 'variety': seed.variety} for seed in seeds]
    return jsonify({'seeds': seed_list})
