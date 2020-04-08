# Build ipref3 image 

sudo docker build -t ubuntu-ipref3

and run the deployment script to deploy ipref3 pod

# run wrk script 

copy paths.txt from root directory to this directoy 

and run the below command to get the performance 

here you have 44 thread with 1000 connection for 3 minutes

ubuntu@controller:~/wrkscript/wrk-scripts$ taskset -c 0-21,44-65 wrk -t 44 -c 1000 -d 180s -s multiplepaths.lua http://controller_ip
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
multiplepaths: Found 10 paths
Running 3m test @ http://controller_ip
  44 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   839.37ms  656.67ms   2.00s    51.62%
    Req/Sec    11.62      8.38   151.00     80.69%
  70542 requests in 3.00m, 28.55MB read
  Socket errors: connect 0, read 1, write 0, timeout 33208
  Non-2xx or 3xx responses: 7515
Requests/sec:    391.69
Transfer/sec:    162.32KB


# run ipref3 for bandwidth

you can also run ipref3 to get the bandwidth 

root@controller:~# kubectl exec -it server bash
root@server:/home# iperf3 -s
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------

and then run the client:- 

iperf3 -P 20 -c 10.108.80.3