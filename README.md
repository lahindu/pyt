# MonitoringTechnicalAssignment

**Prerequisite:**

* Kubernetes cluster
* Helm, Kubectl, Gocker and Git install server with access to Kubernetes cluster.



In this prometheus monitoring set up contains following commonents
1. prometheus
2. node expoter
3. metrix server
4. alertmanager
5. grafana
6. process counter exporter

## Architecture overview

![](https://monitoringdiagrams.s3.ap-southeast-1.amazonaws.com/PrometheusSetup.png)

## Install

### Create Custom process counter exporter docker image

Goto CustomProcessCounterExporter folder

    $ docker build . -t <docker-repo-url>/process_counter_exporter:v1
    $ docker push <docker-repo-url>/process_counter_exporter:v1


### Setup monitoring 


update process_counter_exporter docker image

    $ vi HelmCharts/process_counter_exporter/values.yaml

change image.repository value

Update alertmanager email and slack config

    $ vi HelmCharts/alertmanager/alertmanager.yaml


3. setup monitoring

Deploy kube-state-metrics

    $ helm template kube-state-metrics HelmCharts/kube-state-metrics/
    $ helm install kube-state-metrics HelmCharts/kube-state-metrics/

Deploy node-exporter 

    $ helm template node-exporter HelmCharts/node-exporter/
    $ helm install node-exporter HelmCharts/node-exporter/


Deploy process-counter-exporter 

    $ helm template process-counter-exporter HelmCharts/process-counter-exporter/
    $ helm install process-counter-exporter HelmCharts/process-counter-exporter/


Deploy alertmanager 

    $ helm template alertmanager HelmCharts/alertmanager/
    $ helm install alertmanager HelmCharts/alertmanager/


Deploy prometheus 

     $ helm template prometheus HelmCharts/prometheus/
     $ helm install prometheus HelmCharts/prometheus/


Deploy grafana 

    $ helm template grafana HelmCharts/grafana/
    $ helm install grafana HelmCharts/grafana/
    


