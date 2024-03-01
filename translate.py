from deep_translator import GoogleTranslator
while True:
    user_input=input("Please enter your preferred language: ")
    text=GoogleTranslator(
        source="auto",
        target=user_input[:2]
    )
    output=text.translate(input("Enter the text to translate here: "))
    print(output)