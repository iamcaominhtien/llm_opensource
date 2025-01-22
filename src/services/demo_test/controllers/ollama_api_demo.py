from flask_apispec import doc, marshal_with, MethodResource, use_kwargs
from flask_restful import Resource

from src.services.demo_test.models.demo_test_api_schema import OllamaAPIGetSchema


@doc(tags=["Demo Test"])
class OllamaApiDemoAPIController(MethodResource, Resource):
	@use_kwargs(OllamaAPIGetSchema, location="query")
	@marshal_with(OllamaAPIGetSchema, code=200, description="Success")
	def get(self, question):
		return {"question": question}
