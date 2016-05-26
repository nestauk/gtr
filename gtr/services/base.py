import requests

from .. import __version__


class _Service(object):

    def __init__(self):
        self._BASE_URI = "http://gtr.rcuk.ac.uk/gtr/api/"

    def get_session(self, token=None, env=None):
        session = requests.Session()

        session.headers.update(
            {'User-Agent': ' '.join(
                [self.product_token, requests.utils.default_user_agent()]),
             'Accept': 'application/vnd.rcuk.gtr.json-v3'})     # Returns json only
        return session

    @property
    def product_token(self):
        """A product token for use in User-Agent headers."""
        return 'gtr/{0}'.format(__version__)

    def handle_http_error(self, response, custom_messages=None,
                          raise_for_status=False):
        if not custom_messages:
            custom_messages = {}
        if response.status_code in custom_messages.keys():
            raise requests.exceptions.HTTPError(
                custom_messages[response.status_code])
        if raise_for_status:
            response.raise_for_status()
