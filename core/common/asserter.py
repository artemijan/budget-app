import assertpy
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status as http_status

from core.common.utils import PathExtractor


class GenericAssertionBuilder(assertpy.assertpy.AssertionBuilder):

    def extracting_path(self, path=''):
        path_resolver = PathExtractor(self.val)
        extracted = path_resolver.resolve(path)
        return self.__class__(extracted, description=path)

    def _fmt_items(self, i):
        if len(i) == 0:
            return '<>'
        elif len(i) == 1:
            return '<{}>'.format(i[0])
        else:
            return '<{}>'.format(str(i).lstrip('([').rstrip(',])'))

    def extracting(self, *names, **kwargs):
        result = super().extracting(*names, **kwargs)
        return self.__class__(result.val, result.description, result.kind)

    def raises(self, ex):
        res = super().raises(ex)
        return self.__class__(res.val, res.description, res.kind, ex)

    def when_called_with(self, *some_args, **some_kwargs):
        res = super().when_called_with(*some_args, **some_kwargs)
        if isinstance(res, assertpy.assertpy.AssertionBuilder):
            return self.__class__(res.val, res.description, res.val)
        return res


class GenericResponseAssertionBuilder(GenericAssertionBuilder):

    def is_successful(self):
        if not isinstance(self.val, HttpResponse):
            raise TypeError('val is not HttpResponse')

        if not http_status.is_success(self.val.status_code):
            self._err('Expected %s to respond with successful status (2xx), but was not. Got <%s %s>.' % (
                self._fmt_response(self.val),
                self.val.status_code,
                # TODO: status_text seems to be specific to rest framework's response and dooes not exist on generic
                #       django's HttpResponse. Figure out another way to get status message
                getattr(self.val, 'status_text', ''),
            ))

        return self

    def is_ok(self):
        return self._assert_specific_response_status_code(200, 'OK')

    def is_bad_request(self):
        return self._assert_specific_response_status_code(400, 'Bad Request')

    def is_unauthorized(self):
        return self._assert_specific_response_status_code(401, 'Unauthorized')

    def is_forbidden(self):
        return self._assert_specific_response_status_code(403, 'Forbidden')

    def is_not_found(self):
        return self._assert_specific_response_status_code(404, 'Not Found')

    def is_redirect(self):
        return self._assert_specific_response_status_code(302, 'Http Redirect')

    def is_unavailable(self):
        return self._assert_specific_response_status_code(503, 'Service Unavailable')

    def has_no_cookie(self, cookie_key):
        return self._assert_specific_cookie_value(cookie_key, None)

    def _assert_specific_cookie_value(self, cookie_key, value):
        if not isinstance(self.val, HttpResponse):
            raise TypeError('val is not HttpResponse')
        if self.val.cookies.get(cookie_key) != value:
            if value is None:
                msg = f"Response object should not have cookie {cookie_key}. But it has."
            else:
                msg = f"Response object should have " \
                      f"cookie {cookie_key} set to {value}. But got {self.val.cookies.get(cookie_key)}"
            self._err(msg)
        return self

    def _assert_specific_response_status_code(self, status_code, status_message):
        if not isinstance(self.val, HttpResponse):
            raise TypeError('val is not HttpResponse')

        if self.val.status_code != status_code:
            msg = 'Expected %s to respond <%s %s>, but was not. Got <%s %s>.' % (
                self._fmt_response(self.val),
                status_code,
                status_message,
                self.val.status_code,
                # TODO: status_text seems to be specific to rest framework's response and dooes not exist on generic
                #       django's HttpResponse. Figure out another way to get status message
                getattr(self.val, 'status_text', '')
            )
            self._err(msg)

        return self

    def _fmt_response(self, response: HttpResponse) -> str:
        method = response.request.get('REQUEST_METHOD')
        path = response.request.get('PATH_INFO')
        query_string = response.request.get('QUERY_STRING')

        return '<{method} {path}{query_string}>'.format(
            method=method,
            path=path,
            query_string=f'?{query_string}' if query_string else ''
        )


class ApiResponseAssertionBuilder(GenericResponseAssertionBuilder):
    val: Response

    def api_error_code_is(self, error_code):
        # todo implement error codes for the API
        return self

    def extracting_body(self, path=''):
        if not isinstance(self.val, Response):
            raise TypeError('val is not HsApiResponse')

        # todo: check that has content type of Json
        payload = self.val.json()
        path_resolver = PathExtractor(payload)
        extracted = path_resolver.resolve(path)
        return self.__class__(extracted)
