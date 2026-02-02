from aiogram import Router, F
from aiogram.types import Message
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

router = Router()

last_question = None
last_response_content = None
last_response_reasoning_details = None

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("AI_KEY"),
)

@router.message(F.text.lower().split()[0] == '@')
async def message_hundler(message: Message):
    global last_question, last_response_content, last_response_reasoning_details
    if last_question == None and last_response_content == None and last_response_reasoning_details == None:
        question = message.text.replace("@", "")

        response = client.chat.completions.create(
        model="stepfun/step-3.5-flash:free",
        messages=[
        {
            "role":"user",
            "content":question
        }
            ],

        extra_body={"reasoning": {"enabled": True}}
        )

        response = response.choices[0].message

        await message.answer(response.content)

        last_question = question
        last_response_content = response.content
        last_response_reasoning_details = response.reasoning_details

    else:
        question = message.text.replace("@", "")
        messages = [
            {"role": "user",
            "content" :last_question},
            {
                "role":"assistant", 
                "content": last_response_content,
                "reasoning_details": last_response_reasoning_details 
            },
            {"role":"user","content":question}
        ]


        response = client.chat.completions.create(
        model="stepfun/step-3.5-flash:free",
        messages=messages, 
        extra_body={"reasoning": {"enabled": True}}
        )

        response = response.choices[0].message

        await message.answer(response.content)

        last_question = question
        last_response_content = response.content
        last_response_reasoning_details = response.reasoning_details
