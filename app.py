from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_request():
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "message": "Invalid request format"}), 400
        
        raw_data = data['data']
        numbers = [x for x in raw_data if x.isdigit()]
        alphabets = [x for x in raw_data if x.isalpha()]
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else None

        response = {
            "is_success": True,
            "user_id": "vicky_kumar_01012000",  
            "college_email": "vicky.kumar@cuchd.in",  
            "college_roll_number": "123456789",  
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": "OPERATION_12345"}), 200

if __name__ == '__main__':
    app.run(debug=True)
