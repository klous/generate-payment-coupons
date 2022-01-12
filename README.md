# Python AWS Lambda compatible serverless function for loan payment coupons

This AWS Lambda ready function can take input the start date of loan payments, number of payments, payment amount, lender name, late charge, and property address and then return a set of data that contains all the neccessary data in a format to be used in a template loop to produce the payment coupons


Originally created on Python 3.7 locally and on AWS Python 3.7 runtime.


## Usage
To run the function locally using the local_test.py file:

$	python local_test.py test_data.json

If properly configured and set up, you can also use [AWS SAM command line tools](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html)

$	sam local invoke [OPTIONS]