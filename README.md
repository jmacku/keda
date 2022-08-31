# Celery Autoscale POC

1. create k8s cluster  
   for example `minikube start --driver=podman --container-runtime=containerd` can do the job

2. install keda  
   `helm repo add kedacore https://kedacore.github.io/charts`
   `helm install keda kedacore/keda --namespace keda --create-namespace`

3. optional: install postgres  
   `helm repo add bitnami https://charts.bitnami.com/bitnami`
   `helm install postgres --set auth.postgresPassword=postgres bitnami/postgresql`
   > can use redis as backend for sake of demo just adjust in app.py
   ```python
   backend=f'db+postgresql+psycopg2://{db_user}:{db_pass}@{db_server}'
   ```

4. optional: install prometheus, to see utilization  
   `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
   `helm install monprom prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace`