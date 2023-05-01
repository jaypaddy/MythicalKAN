import unittest
from unittest.mock import MagicMock, patch
from app.metrics import CounterMetric, GaugeMetric


class TestMetrics:
    def test_counter(self):
        self.counter = CounterMetric("loopcounter", "Number of Loops", ["plant", "edge", "line", "workload"])   
        self.counter.inc(1, ["FLOWERMOUND", "MYTHICALAKSEE", "FM407", "MYTHICALAPP1"])  
        assert self.counter.counter.labels("FLOWERMOUND", "MYTHICALAKSEE", "FM407", "MYTHICALAPP1")._value.get() == 1   

    def test_gauge(self):
        self.gauge = GaugeMetric("gauge_metric", "gauge metric description", ["plant", "edge", "line", "workload"])
        self.gauge.set(.5, ["FLOWERMOUND", "MYTHICALAKSEE", "FM407", "MYTHICALAPP1"])
        assert self.gauge.gauge.labels("FLOWERMOUND", "MYTHICALAKSEE", "FM407", "MYTHICALAPP1")._value.get() == .5  

       

if __name__ == '__main__':
    unittest.main()