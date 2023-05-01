import os
from metrics import GaugeMetric, CounterMetric

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO").upper()
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALAPP1").split(",")   
prometheus_port = int(os.getenv("PROMETHEUS_PORT", "8081"))
sleep_time = int(os.getenv("SLEEP_TIME", "1"))


#read an environment variable for app name
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALSCISSORSOBJDET").split(",")   

gmetric = GaugeMetric("gauge_metric", "gauge metric description", scope_keys)
cmetric = CounterMetric("loopcounter", "Number of Loops", scope_keys)





