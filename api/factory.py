"""Factory for creating the flask app."""
import logging

from flask import Blueprint, Flask, current_app, g, jsonify, request
from flask.logging import default_handler
from pythonjsonlogger.jsonlogger import JsonFormatter

LOG_EXTRA_FIELDS = {
    "user_agent",
    "referrer",
    "endpoint",
    "args",
    "base_url",
    "host",
    "host_url",
    "path",
    "remote_addr",
    "remote_user",
}


class CustomJSONFormatter(JsonFormatter):
    """Custom json formatter based on JsonFormatter."""

    def add_fields(self, log_record, record, message_dict):
        """Set additional fields in the log record."""
        super(CustomJSONFormatter, self).add_fields(log_record, record, message_dict)
        if request:
            for f in LOG_EXTRA_FIELDS:
                log_record[f] = getattr(request, f, "")


def setup_app():
    """Set up the app."""
    app = Flask("app")
    setup_logging(app)
    register_endpoints(app)
    return app


def setup_logging(app):
    """Set up the logging."""
    handler = logging.StreamHandler()
    formatter = JsonFormatter("(asctime) (name) (levelname) (message)")
    handler.setFormatter(formatter)
    default_handler.setFormatter(formatter)
    loggers = ["root", "app", "werkzeug", "gunicorn.access", "gunicorn.error"]
    for each in loggers:
        log = logging.getLogger(each)
        log.addHandler(handler)


basic_mod = Blueprint("basic", __name__)


@basic_mod.route("/ping")
def ping():
    """Ping pong endpoint."""
    return jsonify(ping="pong"), 200


def register_endpoints(app):
    """Register endpoints."""
    app.register_blueprint(basic_mod, url_prefix="/api/v1/basic")
