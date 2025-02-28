# webhook-store
Just a simple python app for storing incoming webhook as JSON file.

This project could be useful for self-testing the webhooks in a local OpenShift installation cluster.


## Installation
Let's first create an OpenShift project for this application
```
$ oc new-project webhook-store
```
Then we can launch the application build and the Kubernetes resources' configuration by creating an OpenShift Application:
```
oc new-app --name=webhook-store --labels="application=webhook-store-app"  python:3.9-ubi9~https://github.com/alezzandro/webhook-store 
```
You can monitor the application deployment process by looking at the BuildConfig / Builds elements and at the Pods running in the Project.

Finally let's expose the Service through the OpenShift's Ingress Controller (we are creating a Route object);
```
oc expose service webhook-store -l application=webhook-store-app --name=webhook-store
```
That's all, you can test if the service is working properly by contacting the Route URL we just created also with a simple ```curl``` command.

<b>Please note: this steps don't require administrative privilegies.</b>

## OpenShift's AlertManager configuration
Once deployed the containerized webhook receiver, we can navigate in our OpenShift Web Console to configure the webhook receivers in the respective section. You can follow the OpenShift Documentation at this url: https://docs.openshift.com/container-platform/4.18/observability/monitoring/configuring-core-platform-monitoring/configuring-alerts-and-notifications.html#configuring-alert-routing-console_configuring-alerts-and-notifications


## Testing
Finally you can test any alert you want, for getting some data you could try to shutdown one of the master and one of the worker nodes (in case you have enough machines to let the cluster survive the fault!).