import os

import pytest

# from cdk.service.constants import (
#     CONFIGURATION_NAME,
#     ENVIRONMENT,
#     IDEMPOTENCY_TABLE_NAME_OUTPUT,
#     POWER_TOOLS_LOG_LEVEL,
#     POWERTOOLS_SERVICE_NAME,
#     SERVICE_NAME,
#     TABLE_NAME_OUTPUT,
# )
ERVICE_ROLE_ARN = 'ServiceRoleArn'
LAMBDA_BASIC_EXECUTION_ROLE = 'AWSLambdaBasicExecutionRole'
SERVICE_ROLE = 'ServiceRole'
CREATE_LAMBDA = 'CreateOrder'
TABLE_NAME = 'orders'
IDEMPOTENCY_TABLE_NAME = 'IdempotencyTable'
TABLE_NAME_OUTPUT = 'DbOutput'
IDEMPOTENCY_TABLE_NAME_OUTPUT = 'IdempotencyDbOutput'
APIGATEWAY = 'Apigateway'
GW_RESOURCE = 'orders'
LAMBDA_LAYER_NAME = 'common'
API_HANDLER_LAMBDA_MEMORY_SIZE = 128  # MB
API_HANDLER_LAMBDA_TIMEOUT = 10  # seconds
POWERTOOLS_SERVICE_NAME = 'POWERTOOLS_SERVICE_NAME'
SERVICE_NAME = 'Orders'
METRICS_NAMESPACE = 'my_product_kpi'
POWERTOOLS_TRACE_DISABLED = 'POWERTOOLS_TRACE_DISABLED'
POWER_TOOLS_LOG_LEVEL = 'LOG_LEVEL'
BUILD_FOLDER = '.build/lambdas/'
COMMON_LAYER_BUILD_FOLDER = '.build/common_layer'
ENVIRONMENT = 'dev'
CONFIGURATION_NAME = 'my_conf'
CONFIGURATION_MAX_AGE_MINUTES = '5'  # time to store app config conf in the cache before refetching it
from test.utils import get_stack_output


@pytest.fixture(scope='module', autouse=True)
def init():
    os.environ[POWERTOOLS_SERVICE_NAME] = SERVICE_NAME
    os.environ[POWER_TOOLS_LOG_LEVEL] = 'DEBUG'
    os.environ['REST_API'] = 'https://www.ranthebuilder.cloud/api'
    os.environ['ROLE_ARN'] = 'arn:partition:service:region:account-id:resource-type:resource-id'
    os.environ['CONFIGURATION_APP'] = SERVICE_NAME
    os.environ['CONFIGURATION_ENV'] = ENVIRONMENT
    os.environ['CONFIGURATION_NAME'] = CONFIGURATION_NAME
    os.environ['CONFIGURATION_MAX_AGE_MINUTES'] = '5'
    os.environ['AWS_DEFAULT_REGION'] = 'ap-southeast-1'  # used for appconfig mocked boto calls
    # os.environ['TABLE_NAME'] = get_stack_output(TABLE_NAME_OUTPUT)
    # os.environ['IDEMPOTENCY_TABLE_NAME'] = get_stack_output(IDEMPOTENCY_TABLE_NAME_OUTPUT)


# @pytest.fixture(scope='module', autouse=True)
# def table_name():
#     return os.environ['TABLE_NAME']