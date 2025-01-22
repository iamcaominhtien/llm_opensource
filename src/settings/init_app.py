import logging
import sys

from flask import Flask

from src.settings.configs import BaseConfig
from src.settings.extensions import api, docs
from src.settings.urls import api_list


def init_routes(app):
	for url in api_list:
		api.add_resource(url.resource, url.url, endpoint=url.url)
		app.add_url_rule(
			url.url,
			endpoint=url.url,
			view_func=url.resource.as_view(url.url[1:]),
		)
		docs.register(url.resource, endpoint=url.url)


def create_app(config_class=BaseConfig):
	app = Flask(__name__)

	app.config.from_object(config_class)
	api.init_app(app)
	init_routes(app)
	docs.init_app(app)

	return app


def setup_logging(logger=logging.getLogger(), level=logging.INFO):
	formatter = logging.Formatter(
		"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	)
	handler = logging.StreamHandler(sys.stdout)
	handler.setFormatter(formatter)
	file_handler = logging.FileHandler('log.log', encoding="utf-8")
	logger.addHandler(file_handler)
	logger.addHandler(handler)
	logger.setLevel(level)

	# disable logging httpx
	logging.getLogger('httpx').setLevel(logging.WARNING)
