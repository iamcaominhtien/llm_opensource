from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class BaseConfig:
	DEBUG = False
	TESTING = False

	# Swagger stuff
	APISPEC_SWAGGER_URL = "/api/"
	APISPEC_SWAGGER_UI_URL = "/"
	APISPEC_SPEC = APISpec(
		title="LLM Opensource",
		version="v1",
		openapi_version="2.0.0",
		plugins=[MarshmallowPlugin()]
	)
