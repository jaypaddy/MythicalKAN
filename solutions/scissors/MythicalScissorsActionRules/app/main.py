import logging
import logging.config
import os
from JSONFormatter import JSONFormatter
import threading
import time
from metrics import GaugeMetric, CounterMetric, start_metrics_server
from env import scope_keys, scope_values, app_name, sleep_time, prometheus_port
from env import cmetric, gmetric



def main():
    try:

        logger.info("{} started...the loop sleeps every {} secs".format(app_name,sleep_time))
        start_metrics_server(prometheus_port)
        #hmetric = HistogramMetric("histogram_metric", "Static Values", scope_values, [
        #    0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0
        #])
        #run a forever loop that can be exited by a keyboard interrupt or signal
        sleep_time_float = int(sleep_time) * 1.0
        while True:
            logger.info("{} loop {} secs".format(app_name,sleep_time))
            # stop on keyboard interrupt
            try:
                pass
            except KeyboardInterrupt:
                logger.info("Keyboard interrupt received. Exiting...")
                break
            cmetric.inc(1, scope_values)
            gmetric.set(.5, scope_values)
            time.sleep(sleep_time_float)
    except Exception:
        logger.exception("Exception occurred")



if __name__ == "__main__":
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO").upper()
    logging.config.fileConfig('./logging.conf')
    logger = logging.getLogger()
    print(f"Setting Logging level to {LOGGING_LEVEL} for all loggers")

    for handler in logger.handlers:
        handler.setLevel(LOGGING_LEVEL)
        handler.setFormatter(JSONFormatter())
    main()