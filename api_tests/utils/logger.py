import json
from utils.logging_config import setup_logger

logger = setup_logger("api_tests")

def log_request(method, url, payload=None, params=None):
    logger.info("REQUEST %s %s", method, url)

    if params is not None:
        logger.info("PARAMS: %s", json.dumps(params, ensure_ascii=False))

    if payload is not None:
        logger.info("PAYLOAD: %s", json.dumps(payload, ensure_ascii=False))


def log_response(response):
    logger.info("RESPONSE %s", response.status_code)

    try:
        logger.info("BODY: %s", json.dumps(response.json(), ensure_ascii=False))
    except Exception:
        logger.info("BODY: %s", response.text)