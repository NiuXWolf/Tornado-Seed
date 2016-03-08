import traceback
import logging

from tornado import escape
from tornado.options import options
from tornado.web import RequestHandler as BaseRequestHandler, HTTPError
#from tasks import email_tasks

class APIHandler(BaseRequestHandler):
    def get_current_user(self):
        pass

    def finish(self, chunk=None, notification=None):
        if chunk is None:
            chunk = {}

        if isinstance(chunk, dict):
            chunk = {"meta": {"code": 200}, "response": chunk}

            if notification:
                chunk["notification"] = {"message": notification}

        callback = escape.utf8(self.get_argument("callback", None))
        if callback:
            self.set_header("Content-Type", "application/x-javascript")

            if isinstance(chunk, dict):
                chunk = escape.json_encode(chunk)

            self._write_buffer = [callback, "(", chunk, ")"] if chunk else []
            super(APIHandler, self).finish()
        else:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            super(APIHandler, self).finish(chunk)

    def write_error(self, status_code, **kwargs):
        """Override to implement custom error pages."""
        debug = self.settings.get("debug", False)
        try:
            exc_info = kwargs.pop('exc_info')
            e = exc_info[1]

            if isinstance(e, APIError):
                pass
            elif isinstance(e, HTTPError):
                e = APIError(e.status_code)
            else:
                e = APIError(500)

            exception = "".join([ln for ln in traceback.format_exception(*exc_info)])

            if status_code == 500 and not debug:
                self._send_error_email(exception)

            if debug:
                e.response["exception"] = exception

            self.clear()
            self.set_status(200)  # always return 200 OK for API errors
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.finish(str(e))
        except Exception:
            logging.error(traceback.format_exc())
            return super(APIHandler, self).write_error(status_code, **kwargs)

    def _send_error_email(self, exception):
        pass
        # try:
        #     # send email
        #     subject = "[%s]Internal Server Error" % options.sitename
        #     body = self.render_string("errors/500_email.html",
        #                               exception=exception)
        #     if options.send_error_email:
        #         email_tasks.send_email_task.delay(options.email_from,
        #                                           options.admins, subject, body)
        # except Exception:
        #     logging.error(traceback.format_exc())

class APIError(HTTPError):
    """API error handling exception

    API server always returns formatted JSON to client even there is
    an internal server error.
    """
    def __init__(self, status_code=400, error_detail="", error_type="",
                 notification="", response="", log_message=None, *args):

        super(APIError, self).__init__(int(status_code), log_message, *args)

        self.error_type = error_type if error_type else \
            _error_types.get(self.status_code, "unknow_error")
        self.error_detail = error_detail
        self.notification = {"message": notification} if notification else {}
        self.response = response if response else {}

    def __str__(self):
        err = {"meta": {"code": self.status_code, "errorType": self.error_type}}
        self._set_err(err, ["notification", "response"])

        if self.error_detail:
            err["meta"]["errorDetail"] = self.error_detail

        return escape.json_encode(err)

    def _set_err(self, err, names):
        for name in names:
            v = getattr(self, name)
            if v:
                err[name] = v

_error_types = {400: "param_error",
                401: "invalid_auth",
                403: "not_authorized",
                404: "endpoint_error",
                405: "method_not_allowed",
                500: "server_error"}
