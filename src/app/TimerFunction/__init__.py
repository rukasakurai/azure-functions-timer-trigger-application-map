import datetime
import logging
import os
import requests
import uuid

import azure.functions as func

# Set up logging
logger = logging.getLogger('TimerFunction')

def main(mytimer: func.TimerRequest) -> None:
    """Timer trigger function that runs on a schedule and makes an HTTP call to the HttpFunction.
    
    Args:
        mytimer: The timer request object that triggered this function
    """
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    if mytimer.past_due:
        logger.warning('The timer is past due!')
    
    # Generate a unique request ID for tracing
    request_id = str(uuid.uuid4())
    logger.info(f'TimerFunction execution started at {utc_timestamp} with request_id: {request_id}')
    
    try:
        # Get the function app URL from environment or use localhost for local development
        function_app_url = os.environ.get('FUNCTION_APP_URL', 'http://localhost:7071')
        http_function_url = f"{function_app_url}/api/HttpFunction"
        
        # Add custom headers for distributed tracing
        headers = {
            'Request-Id': request_id,
            'X-Correlation-ID': request_id,
            'Content-Type': 'application/json'
        }
        
        # Make HTTP request to the HttpFunction
        logger.info(f"Making request to HttpFunction with request_id: {request_id}")
        response = requests.get(
            http_function_url,
            headers=headers,
            timeout=30
        )
        
        # Log the response
        logger.info(f"HttpFunction response status: {response.status_code}")
        if response.status_code == 200:
            logger.info(f"HttpFunction response: {response.text}")
        else:
            logger.error(f"HttpFunction error response: {response.text}")
    
    except Exception as e:
        logger.error(f"Error in TimerFunction: {str(e)}", exc_info=True)
    
    finally:
        logger.info(f'TimerFunction execution completed with request_id: {request_id}')
