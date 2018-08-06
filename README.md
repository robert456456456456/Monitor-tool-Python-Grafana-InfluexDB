# Monitor-tool-Python-Grafana-InfluexDB
Simple python agent for Linux  
### Prerequisite
pip install
###### sudo apt-get install python-pip
Linux metric lib
###### sudo pip install linux-metrics
Git for we can clone this
###### sudo apt-get install git-all
##### Install Grafana&InfluxDB
http://docs.grafana.org/installation/debian/
http://www.andremiller.net/content/grafana-and-influxdb-quickstart-on-ubuntu
##### git clone
###### git clone  https://github.com/robert456456456456/Monitor-tool-Python-Grafana-InfluexDB.git
#### Run in cron
###### sudo crontab -e
###### */5 * * * * cd  PATH/Monitor-tool-Python-Grafana-InfluexDB && /usr/bin/python PATH/Monitor-tool-Python-Grafana-InfluexDB/metrick.py >> log.txt
