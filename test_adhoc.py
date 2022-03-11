import argparse
from datetime import datetime
import json
import os
import logging
from timenlp.timenlp import logger
from datetime import datetime

logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

from timenlp import timenlp

def test():
  ref = datetime(2022, 3, 7, 12, 34)
  phrase = "3 and 1/4 of an hour"
  parsed = timenlp(phrase, ts=ref, latent_time=True)
  print("ref:", ref, "phrase:", phrase)
  print(parsed)
  print(parsed.resolution)
  
  assert True


test()