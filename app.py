def handler(event, context):
    """
    Lambda function handler.

    Args:
    - event: AWS event data (API Gateway request).
    - context: Lambda execution context.

    Returns:
    - Dictionary with HTTP status code and response body.
    """
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }

