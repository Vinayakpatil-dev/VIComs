import vonage 
client = vonage.Client(key="6897b998", secret="28j0WUnAD1mIDOum")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "919789055632",
        "text": "hello vinayak",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")