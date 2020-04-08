# Design

```text
Here I am trying to Design below flow . Here we are trying to test North South traffic and at the same time East West traffic.

For North South , the request will come from ingress controller pod.

for East west traffic , the request will then go to flask app and then flask app to postgress db

```

![Screenshot](Design_flow.tiff)

# deployment script does following thing :-

```text

1) It deploys flask and postgress on different node.
2) you can set the parameter how many pods you want to deploy
3) it creates  ingress policy to access through ingress controller pod
4) it creates network policy where postgress is accessed by flask and flask is accessed by outside

```

# Run deploymnet script 

./deployment.sh

```text
root@controller:~# kubectl get all -n flask-1
NAME                              READY   STATUS    RESTARTS   AGE
pod/flask-1-7855d9d857-kw6jj      1/1     Running   0          7h46m
pod/postgres-1-6f6c979ff8-nx52t   1/1     Running   0          7h46m

NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/svc-flask-1      ClusterIP   10.109.227.80   <none>        80/TCP     7h46m
service/svc-postgres-1   ClusterIP   10.99.200.69    <none>        5432/TCP   7h46m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask-1      1/1     1            1           7h46m
deployment.apps/postgres-1   1/1     1            1           7h46m

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/flask-1-7855d9d857      1         1         1       7h46m
replicaset.apps/postgres-1-6f6c979ff8   1         1         1       7h46m

root@controller:~/script# kubectl get ingress -n flask-1
NAME                    CLASS    HOSTS   ADDRESS         PORTS   AGE
nginx-ingress-flask-1   <none>   *       controller_IP    80      9h


root@controller:~/script# kubectl get networkpolicy -n flask-1
NAME                             POD-SELECTOR     AGE
api-allow-flask-1                app=flask-1      9h
ingress-network-policy-flask-1   app=postgres-1   9h

```
# run curl command or run the URL in the browser 

```text
run the curl command 
 curl http://controller-ip/nginx-ingress-flask-1
 
 and you can see below 
 
User 'Jerry Moore MD has address 460 Erin View Jillland, MO 80008 and user got text :-Difficult source board these nature half idea. Write another building enjoy anyone behind. Born close check six good doctor. I writer military option task rich respond public.' is from database

```
# you can verify in the db 

```text
kubectl exec -it -n flask-1 postgres-1-6f6c979ff8-dtkn8 /bin/sh

# psql -U postgres


psql (9.6.2)
Type "help" for help.

postgres=# \c
You are now connected to database "postgres" as user "postgres".
postgres=# \q



# psql -U postgres
psql (9.6.2)
Type "help" for help.

postgres=# \c demo_db
You are now connected to database "demo_db" as user "postgres".
demo_db=# \d
             List of relations
 Schema |     Name     |   Type   |  Owner
--------+--------------+----------+---------
 public | users        | table    | mudasir
 public | users_id_seq | sequence | mudasir
(2 rows)

demo_db=# \d+ users
                                                   Table "public.users"
 Column  |       Type        |                     Modifiers                      | Storage  | Stats target | Description
---------+-------------------+----------------------------------------------------+----------+--------------+-------------
 id      | integer           | not null default nextval('users_id_seq'::regclass) | plain    |              |
 name    | character varying |                                                    | extended |              |
 address | character varying |                                                    | extended |              |
 text    | character varying |                                                    | extended |              |
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)

demo_db=# select * from users;
 id |        name        |          address           |                                                          text

----+--------------------+----------------------------+-------------------------------------------------------------------------------------------------------
------------------
  1 | Kimberly Harris    | 772 Campos Mount Suite 054+| Drug century fire rate. Investment truth protect staff much common.
                 +
    |                    | Heatherside, SD 17818      | Pretty stand lawyer throw affect together. Recently small yet major hold.
                 +
    |                    |                            | Store car doctor who image. Third tend support public.
  2 | Cynthia Jackson MD | 3986 Brittany Parkway     +| Degree site detail cost. Interesting onto base move. Bill hotel truth each.
                 +
    |                    | Lake Natalieland, PA 41009 | Perform stand data never. Water approach big decide reality. Town condition inside official.
  3 | Alyssa Lee         | 0146 Brown Garden Apt. 172+| Drop expert model list generation wonder. Determine room her director. Audience degree outside either
support behavior.+
    |                    | East Marcus, DE 11515      | Six hot little develop. Bar level suffer example attack.
  4 | Hayley Kaiser      | 591 Brandon Run           +| Drop remain include place imagine hear. Their story call with. Yeah head daughter ahead amount firm.
                 +
    |                    | Garciaton, MI 07253        | Concern allow bill natural animal kid garden. However laugh since risk exactly PM.
  5 | Jeffrey Vasquez    | 0834 Kelli Branch Apt. 616+| Dark very realize network. Military model reality glass. Some statement account.
    |                    | East Nicolehaven, ME 81435 |
  6 | Robert Carson      | 75553 Grant Highway       +| List similar if bed international follow open. Traditional total sister firm inside show leg happy.
                 +
    |                    | Lake Frankstad, VT 44866   | Tax oil media walk give a develop.
                 +
    |                    |                            | Ahead make modern few.
(6 rows)

demo_db=#
```

