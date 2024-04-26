from flask import jsonify
from models.producing_company import ProducingCompany

@app.route('/api/v1/producing_companies', methods=['GET'])
def get_producing_companies():
    companies = ProducingCompany.query.all()
    company_list = [{'name': company.name, 'website': company.website, 'phone': company.phone} for company in companies]
    return jsonify({'producing_companies': company_list})
