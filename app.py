from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Serve the HTML donation form
@app.route('/')
def donation_page():
    return render_template('donation.html')  # File should be in the "templates" directory

# Endpoint for handling donation notifications
@app.route('/notify-donation', methods=['POST'])
def notify_donation():
    data = request.json
    if not data:
        return jsonify({"error": "No donation data received"}), 400

    name = data.get("name")
    email = data.get("email")
    amount = data.get("amount")
    payment_method = data.get("paymentMethod")
    phone = data.get("phone")
    admin_email = data.get("adminEmail")

    print(f"Donation Notification: {name} donated ${amount} using {payment_method}. Contact: {email}, {phone}")

    return jsonify({"message": "Donation notification received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

