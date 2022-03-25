import openai

 # INTRODUCIR API KEY DE OPENAI PARA QUE PUEDA FUNCIONAR EL CHATBOT
openai.api_key=""

conversation = ""

exe= True

while(exe):
    question = input("Humano: ")
    conversation += "\nHumano: " + question + "\nAI"
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", "Humano:", "AI"]
    )
    answer=response.choices[0].text.strip()
    conversation += answer
    print("AI" + answer + "\n")
