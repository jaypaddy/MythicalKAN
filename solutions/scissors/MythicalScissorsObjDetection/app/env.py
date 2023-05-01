import os
from metrics import GaugeMetric, CounterMetric

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO").upper()
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALAPP1").split(",")   
prometheus_port = int(os.getenv("PROMETHEUS_PORT", "8081"))


#read an environment variable for app name
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALSCISSORSOBJDET").split(",")   

request_count_metric = CounterMetric("requests", "Number of Requests", scope_keys)





