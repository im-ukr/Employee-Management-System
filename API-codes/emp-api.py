from flask_cors import CORS
from flask import Flask, jsonify, request
app = Flask(__name__)
CORS(app)
data = [
    {"id": 7369, "emp_name": "Smith", "age": 34, "gender": "M", "email_id":"smith2@abc.in"},
    {"id": 7370, "emp_name": "Allen", "age": 23, "gender": "M", "email_id":"allen6@comp.in"},
    {"id": 7371, "emp_name": "Jones", "age": 27, "gender": "M", "email_id":"jones77@csi.in"},
]

# Define a route to get all the data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Define a route to get data by ID
@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    for item in data:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({'error': 'Data not found'})

# Define a route to add new data
@app.route('/data', methods=['POST'])
def add_data():
    new_item = {
        'id': request.json['id'],
        'emp_name': request.json['emp_name'],
        'age': request.json['age'],
        'gender': request.json['gender'],
        'email_id': request.json['email_id']
    }
    data.append(new_item)
    return jsonify(new_item)

# Define a route to update data by ID
@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    for item in data:
        if item['id'] == id:
            item['emp_name'] = request.json['emp_name']
            item['age'] = request.json['age']
            item['gender'] = request.json['gender']
            item['email_id'] = request.json['email_id']
            return jsonify(item)
    return jsonify({'error': 'Data not found'})

# Define a route to delete data by ID
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    for i, item in enumerate(data):
        if item['id'] == id:
            data.pop(i)
            return jsonify({'message': 'Data with employee id '+ str(id) +' deleted successfully'})
    return jsonify({'error': 'Data not found'})

if __name__ == '__main__':
    app.run(debug=True)
