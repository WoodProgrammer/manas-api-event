# manas-api-event
Event triggered policy handler for Kubernetes Clusters.Currently this policy handler check the allowed repo list and interrupt the Kubernetes requests so let's have look at flow.

## POLICY Options

    * Image repo check (0.0.1)
    * Cert Mutator (TO-DO)

### Image repo check
You can specify your allowed repo list and add them via configmap, manas app fetch the allowed repo list and compare your request.

Let's have a look at this example output : 
```
kubectl run app-new --generator=run-pod/v1 --image my-repo/re1dis
Error from server: admission webhook "manas.manas.svc" denied the request: Image repository is not allowed
```

Example repo.list: 
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: manas-allowed-repo-list
  namespace: manas
data:
  allowed.repo_list: |
    quay.io
    myown_repo.com
```

Let's run create pod command with allowed repos in the list, and manas app does not interrupt your request.
```
kubectl run app-new --generator=run-pod/v1 --image quay.io/redis
pod/app-new created
```

## How to deploy manas-api-event ?

Manas Controller deploy this stack into your Kubernetes, there is 2 mandatory things for AdmissionValidationWebhook development one of is CA certificate the other one is a controller to execute your logic.

### * Run Manas-Controller

Controller needs to some of ClusterRole,SA like RBAC objects to create, patch, delete your dependencies (deployment, webhook definition).

```
kubectl apply -f k8s/jobs.yaml
```
This deploys a Job to deploy manas admission webhook.
