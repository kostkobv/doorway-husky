from linkedin import linkedin
from wsgiref.simple_server import make_server
from urlparse import parse_qs

import webbrowser


class LinkedinMan(object):
    """
    Class for communication with linkedin. Just simplifying the interface to make it simpler to use
        inside off app
    """

    SERVER_PORT = 4567
    SERVER_HOST = 'localhost'
    RETURN_URL = "http://%s:%s/" % (SERVER_HOST, SERVER_PORT)

    def __init__(self, api_key, api_secret):
        """
        Inits the linkedin instance object. Raises error if API key or secret aren't provided

        :param api_key:
        :param api_secret:
        :return: new Linkedin object
        """

        if not (api_key or api_secret):
            raise NameError('No API key or secret provided')

        self.server = make_server(self.SERVER_HOST, self.SERVER_PORT, self.catch_answer)
        self.token = None
        self.auth = None
        self.app = None

        self.auth = linkedin.LinkedInAuthentication(api_key, api_secret, self.RETURN_URL)

    def set_app_from_auth_code(self, code):
        """
        Creating app to make requests to linkedin API

        :param code: string with code after linkedin auth
        :return: app
        """

        token = self.set_token_from_code(code)
        self.app = linkedin.LinkedInApplication(token)

        print 'Got app. Ready to make requests to API.\n'

    def catch_answer(self, environ, start_response):
        """
        Function that handles the requests from linkedin after authentication

        :param environ: wsgi env params
        :param start_response:
        :return: string response to browser
        """

        params = parse_qs(environ.get('QUERY_STRING', ''))
        code = self.parse_code(params)

        self.set_app_from_auth_code(code)

        start_response('200 OK', [('Content-type', 'text/plain')])

        return 'Such WOW\nNow proceeding. You can close me!'

    def set_token_from_code(self, code):
        """
        Sets token based on auth code returned by linkedin

        :param code:
        :return:
        """
        print 'Got code. Code is %s\n' % code

        self.auth.authorization_code = code
        token = self.auth.get_access_token().access_token

        print 'Got token. Token is %s\n' % token

        return token

    @staticmethod
    def parse_code(params):
        """
        Gets auth code from linkedin response. Raises error if there is no code in response.

        :param params: request params
        :return: code
        """
        if 'code' in params:
            return params['code'][0]

        raise NameError('Ooops... No code. Something go wrong. Try again or contact the developer.')

    def authentication(self):
        """
        Authenticates user. Opens the browser for user to authenticate in linkedin.
        Then sets up simple server to catch response from linkedin.
        """

        webbrowser.open(self.auth.authorization_url)

        self.server.handle_request()

    def get_app(self):
        """
        Returns linkedin app which gives the ability to make requests

        :return: linkedin app to make requests
        """
        return self.app
