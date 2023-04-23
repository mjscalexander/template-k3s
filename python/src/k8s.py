from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print(f'{i.status.pod_ip}, {i.metadata.namespace}, {i.metadata.name}')