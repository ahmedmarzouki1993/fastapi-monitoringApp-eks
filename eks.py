


from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-fastapi-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-fastapi-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-fastapi-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-fastapi-container",
                        image="267043491037.dkr.ecr.eu-west-3.amazonaws.com/fastapi-monitoring-repo:latest",
                        ports=[client.V1ContainerPort(container_port=8000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service with LoadBalancer type
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-fastapi-service"),
    spec=client.V1ServiceSpec(
        type="LoadBalancer",  # Change from default 'ClusterIP' to 'LoadBalancer'
        selector={"app": "my-fastapi-app"},
        ports=[client.V1ServicePort(port=80, target_port=8000)]  # Expose port 80 externally, map to 8000 in the container
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)

print("Deployment and LoadBalancer Service created successfully.")








"""from kubernetes import client,config
#load kubernetes configuration
config.load_kube_config()
#create  a kubernetes Api Client
api_client =client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-fastapi-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-fastapi-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-fastapi-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-fastapi-container",
                        image="267043491037.dkr.ecr.eu-west-3.amazonaws.com/fastapi-monitoring-repo:latest",
                        ports=[client.V1ContainerPort(container_port=8000)]
                    )
                ]
            )
        )
    )
)
# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)


# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-fastapi-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-fastapi-app"},
        ports=[client.V1ServicePort(port=8000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)"""