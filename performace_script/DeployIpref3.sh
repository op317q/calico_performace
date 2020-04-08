#!/bin/bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    role: server
  name: server-service
spec:
  ports:
  - port: 5201
    protocol: TCP
    targetPort: 5201
  selector:
    role: server
  type: NodePort
  externalIPs:
  - controller_ip
  externalTrafficPolicy: Cluster
EOF


cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: server1
  labels:
    role: server
spec:
  nodeName: controller_node
  securityContext:
    runAsUser: 0
  containers:
    - name: server
      image: ubuntu-ipref3:latest
      imagePullPolicy: IfNotPresent
      command: ["iperf3 -s"]
      securityContext:
        privileged: true
        runAsUser: 0
      command: ["sleep", "infinity"]
EOF
