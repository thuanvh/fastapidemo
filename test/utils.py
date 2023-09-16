import json
import random
import string
from typing import Any, Dict, Optional

import boto3
from aws_lambda_powertools.utilities.typing import LambdaContext
import yaml

def generate_random_string(length: int = 3):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_context() -> LambdaContext:
    context = LambdaContext()
    context._aws_request_id = '888888'
    return context


def get_stack_name()->str:
    with open('serverless.yml', 'r') as file:
        yamlfile = yaml.safe_load(file)
        return yamlfile['service']+'-'+yamlfile['provider']['stage']
def get_region()->str:
    with open('serverless.yml', 'r') as file:
        yamlfile = yaml.safe_load(file)
        return yamlfile['provider']['region']
def get_table_name()->str:
    with open('.serverless/serverless-state.json', 'r') as file:
        a = json.load(file)
        return a['service']['custom']['tableName']
def get_stack_output(output_key: str) -> str:
    client = boto3.client('cloudformation')
    response = client.describe_stacks(StackName=get_stack_name())
    stack_outputs = response['Stacks'][0]['Outputs']
    for value in stack_outputs:
        if str(value['OutputKey']) == output_key:
            return value['OutputValue']
    raise Exception(f'stack output {output_key} was not found')