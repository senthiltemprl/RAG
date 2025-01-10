from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
)

# def token(messages,model):  
#     for token in client.chat.completions.create(
#      model=model,
#         messages=[
#         {
#         "role": "user",
#         "content": [
#             {
#             "type": "text",
#             "text": messages
            
#             } 
            
#         ]
#         }
#     ],
#     stream=True
    

#     ):
#          print(token.choices[0].delta.content,end='')


#chat completion
def chat_completion(question, model):
    try:
        response_text = ""
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        }
                    ]
                }
            ],
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                response_text += chunk.choices[0].delta.content
        return response_text
    except Exception as e:
        return f"Error occurred: {str(e)}"