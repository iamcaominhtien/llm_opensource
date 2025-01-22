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
		template = """You are a question-answer assistant.
		Answer the question in concise and clear format.
		If you don't know the answer, you can say "I don't know".
		Don't try to make up an answer.
		Question: {question}
		"""

		prompt = ChatPromptTemplate.from_template(template)
		model = OllamaLLM(model="deepseek-r1:1.5b")
		chain = prompt | model
		response = chain.invoke({"question": question})

		return Response(response, mimetype='text/plain')
