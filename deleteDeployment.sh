#!/bin/bash

for i in {1..1}
do
   frontend=flask-$i
   echo $frontend
   kubectl delete ns $frontend
done