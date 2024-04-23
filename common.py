# -*- coding: utf-8 -*-
from openai import OpenAI

API_KEY = "你的apikey"

def get_openai_client():
    return OpenAI(api_key=API_KEY)