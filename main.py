from sensor.logger import logging
from sensor.exception import SensorException


def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Stopping the test_logger_and_exception")
     
     except Exception as e:
          raise SensorException(error_message, error_details)