from __future__ import print_function

from flask import Flask, request, jsonify
import ssl
import sys
from container_utils import check_image

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    allowed = True
    image = request.json["request"]["object"]["spec"]["containers"]["image"]
    is_allow = check_image(image)

    if is_allow == False
        allowed = False
        response = {
                    "response": {
                        "allowed": allowed,
                        "uid": request.json["request"]["uid"],
                        "status": {"message": "Image repository is not allowed "},
                    }
                }
    else:
        response = {
                    "response": {
                        "allowed": allowed,
                        "uid": request.json["request"]["uid"],
                        "status": {"message": "Image repository is not allowed "},
                    }
                }
    
    return jsonify(response)
        

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("/etc/certs/cert.pem", "/etc/certs/key.pem")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", ssl_context=context)
