# local_test.py
# This is a simple python module to test the lambda function. Local AWS Lambda testing can also be done with the AWS cli function: $	sam local invoke
# it takes a single argument when running the python file, the json file with the test data, like so: python local_test.py test_data.json

from sys import argv
import json
from lambda_function import lambda_handler

script, testfile = argv


with open(testfile) as f:
  event_test_data = json.load(f)

# AWS passes in other data via context, for our local, basic testing purposes it is not needed
context = ""

print(lambda_handler(event_test_data, context))