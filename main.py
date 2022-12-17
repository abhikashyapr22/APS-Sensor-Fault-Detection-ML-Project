from sensor.logger import logging
from sensor.exception import SensorException
import os, sys


def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Stopping the test_logger_and_exception")
     
     except Exception as e:
          raise SensorException(e, sys)

     print("Done")

if __name__=="__main__":
     test_logger_and_exception()