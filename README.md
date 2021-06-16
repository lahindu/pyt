# MonitoringTechnicalAssignment

**Prerequisite:**

* Kubernetes cluster
* Helm, Kubectl, Gocker and Git install server with access to Kubernetes cluster.



In this prometheus monitoring set up contains following commonents, 
1. prometheus
2. node expoter
3. metrix server
4. alertmanager
5. grafana
6. process counter exporter


## Install

Create Custom process counter exporter docker image

goto CustomProcessCounterExporter folder

  $ docker build . -t <docker-repo-url>/process_counter_exporter:v1
  $ docker push <docker-repo-url>/process_counter_exporter:v1


Setup monitoring 

1. update process_counter_exporter docker image

  $ vi HelmCharts/process_counter_exporter/values.yaml

change image.repository value

2. update alertmanager email and slack config

  $ vi HelmCharts/alertmanager/alertmanager.yaml


3. setup monitoring

deploy kube-state-metrics 
  $ helm template kube-state-metrics HelmCharts/kube-state-metrics/
  $ helm install kube-state-metrics HelmCharts/kube-state-metrics/

deploy node-exporter 
  $ helm template node-exporter HelmCharts/node-exporter/
  $ helm install node-exporter HelmCharts/node-exporter/


deploy process-counter-exporter 
  $ helm template process-counter-exporter HelmCharts/process-counter-exporter/
  $ helm install process-counter-exporter HelmCharts/process-counter-exporter/


deploy alertmanager 
  $ helm template alertmanager HelmCharts/alertmanager/
  $ helm install alertmanager HelmCharts/alertmanager/


deploy prometheus 
  $ helm template prometheus HelmCharts/prometheus/
  $ helm install prometheus HelmCharts/prometheus/


deploy grafana 
  $ helm template grafana HelmCharts/grafana/
  $ helm install grafana HelmCharts/grafana/
