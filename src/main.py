from __future__ import print_function

from flask import Flask, request, jsonify
import ssl
import sys
from container_utils import check_image, get_allowed_list

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    allowed = True
    allowed_list = get_allowed_list()
    print(request.json)
    image = request.json["request"]["object"]["spec"]["containers"]["image"]
    is_allowed = check_image(image, allowed_list)

    if is_allowed == False:
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
                        "status": {"message": "Image repository is allowed "},
                    }
                }
    
    return jsonify(response)
        

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("/etc/certs/cert.pem", "/etc/certs/key.pem")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", ssl_context=context)
