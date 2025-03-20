"""
Automated news analysis and sentiment scoring using Bedrock.

@dev Ensure AWS environment variables are set correctly for Bedrock access.
"""

import os
import sys
import json
import re
from typing import List

from langchain_aws import ChatBedrock
from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio
import nest_asyncio  #Se agrego esta libreria con pip install nest_asyncio ya que la de arriba permite que el bucle se cierre forzadamente
from dotenv import load_dotenv

from pydantic import BaseModel
from browser_use import Agent, SystemPrompt
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

load_dotenv()

nest_asyncio.apply()

class Post(BaseModel):
	title: str
	url: str
	likes: str
	subscriptores: str
     

class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)     


def get_llm():
    return ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        temperature=0.0,
        max_tokens=None,
    )




class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        # Get existing rules from parent class
        existing_rules = super().important_rules()

        # Add your custom rules
        new_rules = """
        Respond exclusively in JSON format with the following structure:
        { "title": "...", "url": "...", "likes": "...", "subscribers": "..." }
        Do not include any additional text, explanations, or formatting.
"""

        # Make sure to use this pattern otherwise the exiting rules will be lost
        return f'{existing_rules}\n{new_rules}'



async def mainAws(task):  # Añadimos task como parámetro
    llm = get_llm()
    browser = Browser(config=BrowserConfig())
    agent = Agent(
        task=task,  # Usamos el parámetro task
        llm=llm,
        controller=Controller(output_model=Posts),
        browser=browser,
        validate_output=True,
        system_prompt_class=MySystemPrompt,
    )
    
    history = await agent.run()
    result = history.final_result()
    await browser.close()  # Cerramos el navegador
    return result  # Devolvemos el resultado crudo para procesarlo en Gradio




#CODIGO PARA GPT MAS CORTO Y RAPIDO 


async def mainGPT(task):  # Añadimos task como parámetro
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, controller=controller)  # Usamos el parámetro task
    history = await agent.run()
    result = history.final_result()
    return result  # Devolvemos el resultado crudo para procesarlo en Gradio


