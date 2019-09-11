import logging

logger = logging.getLogger(__name__)

class Base(object):
    """
        The Base class for Endpoint Client, which contains 2 wrapper class for
        handling endpoint response.
    """

    def _response_handler(self, cls, response):
        """ _response_handler function

            Convert response json to a Veem Object
        """
        if response and isinstance(response, dict):
            return cls(**response).convert
        logger.error(response)

    def _list_response_handler(self, cls, content_cls, response):
        """ _list_response_handler function

            Convert pagination list to a list of Veem Objects
        """
        if response:
            if isinstance(response, dict):
                return cls(**response).convertContent(content_cls)
            if isinstance(response, list):
                return cls(content=response).convertContent(content_cls)
        logger.error(response)
