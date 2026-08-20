from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client()

# Using Interactions

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)

# Using generate_content

# chat = client.chats.create(
#     model="gemini-3.7-flash" # Pass your tools configuration here if applicable
# )

# response = chat.send_message("Explain how AI works in a few words")
# print(response.text)


