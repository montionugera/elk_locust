## Run 

docker-compose up --scale locust-worker=2


## App Destination

web : http://localhost:2350/

locust_host : http://localhost:2330/

elastic_host : http://localhost:9200/

kibana_host : http://localhost:5601



## Locust Ref

https://docs.locust.io/en/latest/quickstart.html

### locust image ref
https://github.com/sernst/locusts

## Logstash / GROK

#### Doc
https://www.elastic.co/guide/en/logstash/current/input-plugins.html
https://www.elastic.co/guide/en/logstash/current/filter-plugins.html

tutorial

https://logz.io/blog/logstash-grok/

tester

https://grokdebug.herokuapp.com/