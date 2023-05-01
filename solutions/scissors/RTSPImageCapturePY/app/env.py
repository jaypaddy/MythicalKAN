import os
from metrics import GaugeMetric, CounterMetric
import dotenv
dotenv.load_dotenv()

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO").upper()
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALAPP1").split(",")   
prometheus_port = int(os.getenv("PROMETHEUS_PORT", "8081"))
sleep_time = int(os.getenv("SLEEP_TIME", "1"))
file_prefix = os.environ.get("FILE_PREFIX","mythicalscissors")
blob_connstring = os.environ.get("EDGE_BLOB_CONN_STRING")
blobcontainername = os.environ.get("EDGE_BLOB_CONTAINER_NAME")
camera_url = os.environ.get("EDGE_CAMERA_URL")
inference_url = os.environ.get("EDGE_INFERENCE_URL")

#read an environment variable for app name
app_name = os.getenv('APP_NAME', "mythicalapp")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALAKSEE,FM407,MYTHICALSCISSORSOBJDET").split(",")   

gmetric = GaugeMetric("gauge_metric", "gauge metric description", scope_keys)
cmetric = CounterMetric("imgcounter", "Number of Images captured", scope_keys)





