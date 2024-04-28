import os
import json
import sys
import boto3

prompt="""

        you are a cricket expert now just tell me when RCB will win the IPL?
"""

bedrock=boto3.client(service_name="bedrock-runtime")

