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

You can launch a Prometheus container for trying it out with

    $ docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus

Prometheus will now be reachable at http://localhost:9090/.

    $ docker build . -t <docker-repo-url>/process_counter_exporter:v1
    $ docker push <docker-repo-url>/process_counter_exporter:v1


Setup monitoring 


update process_counter_exporter docker image

    $ vi HelmCharts/process_counter_exporter/values.yaml

change image.repository value

update alertmanager email and slack config

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
