import datetime
import logging
import json

import azure.functions as func

# Set up logging
logger = logging.getLogger('HttpFunction')

def main(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger function that returns a message with the current time.
    
    Args:
        req: The HTTP request object
        
    Returns:
        An HTTP response containing JSON with a status message and timestamp
    """
    logger.info('HttpFunction processed a request.')
    
    # Extract request ID for distributed tracing from headers if present
    request_id = req.headers.get('Request-Id', 'no-request-id')
    correlation_id = req.headers.get('X-Correlation-ID', request_id)
    
    logger.info(f"Processing request with request_id: {request_id}, correlation_id: {correlation_id}")
    
    # Get current timestamp
    current_time = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    # Create response payload
    response_payload = {
        "message": "This is the HTTP Function response",
        "timestamp": current_time,
        "request_id": request_id,
        "correlation_id": correlation_id
    }
    
    # Log the response
    logger.info(f"Returning response for request_id: {request_id}")
    
    # Return HTTP response with JSON payload
    return func.HttpResponse(
        body=json.dumps(response_payload),
        status_code=200,
        mimetype="application/json"
    )
