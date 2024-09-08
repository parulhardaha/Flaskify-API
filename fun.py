from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/is_palindrome/<string:n>')
def is_palindrome(n):
    # Check if the string is a palindrome
    result = n == n[::-1]
    
    # Get server IP address
    server_ip = request.remote_addr
    
    # Return a JSON response
    return jsonify({
        "Numbers": n,
        "is_palindrome": result,
        "server_ip": server_ip
    })

if __name__ == "__main__":
    app.run(debug=True)
