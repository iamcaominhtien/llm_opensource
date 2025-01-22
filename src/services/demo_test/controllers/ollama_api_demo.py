from flask import Response
from flask_apispec import doc, marshal_with, MethodResource, use_kwargs
from flask_restful import Resource
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from src.services.demo_test.models.demo_test_api_schema import OllamaAPIGetSchema


@doc(tags=["Demo Test"])
class OllamaApiDemoAPIController(MethodResource, Resource):
	@use_kwargs(OllamaAPIGetSchema, location="query")
	@marshal_with(OllamaAPIGetSchema, code=200, description="Success")
	def get(self, question):
		template = """Question: {question}

		Answer: Let's think step by step."""

		prompt = ChatPromptTemplate.from_template(template)
		model = OllamaLLM(model="llama3.2")
		chain = prompt | model
		response = chain.invoke({"question": question})

		return Response(response, mimetype='text/plain')
