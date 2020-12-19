#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

mkdir -p certs

generate_certificate(){
    openssl genrsa -out certs/ca.key 2048
    openssl req -new -x509 -key certs/ca.key -out certs/ca.crt -config ca_config.txt
    openssl genrsa -out certs/manas-key.pem 2048
    openssl req -new -key certs/manas-key.pem -subj "/CN=manas.manas.svc" -out manas.csr
    openssl x509 -req -in manas.csr -CA certs/ca.crt -CAkey certs/ca.key -CAcreateserial -out certs/manas-crt.pem
}
apply_certificates(){
    kubectl create secret generic manas -n manas \
        --from-file=key.pem=certs/manas-key.pem \
        --from-file=cert.pem=certs/manas-crt.pem
}

IS_EXIST=true
kubectl get secret -n manas |grep manas |grep Opaque || IS_EXIST=false

if [ "${IS_EXIST}" = true ];then
    echo "Manas Cert is already exist"
else
    echo "Certs are generating"
    generate_certificate
    apply_certificates    
fi
