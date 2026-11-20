
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.bodhan.ai/v1",
    api_key=os.getenv("BODHAN_API_KEY")
)

# Input dictionary
text = {
    "A": "सबसे पहले प्याज़ और टमाटर को बारीक काट लें।",
    "B": "अब इसमें कसूरी मेथी और गरम मसाला मिलाएँ।",
    "C": "लगभग 180 डिग्री तापमान पर 20 मिनट तक बेक करें।",
    "D": "सर्वप्रथम कांदा आणि टोमॅटो बारीक चिरून घ्या.",
    "E": "क्या मैं इसमें थोड़ा और पानी डाल सकती हूँ?"
}

# Language mapping
languages = {
    "A": "hi",
    "B": "hi",
    "C": "hi",
    "D": "mr",
    "E": "hi"
}

os.makedirs("audio/bodhan", exist_ok=True)

# Generate audio for each category
for category, sentence in text.items():

    print(f"\nGenerating Bodhan audio: {category}")

    start = time.perf_counter()

    try:
        speech = client.audio.speech.create(
            model="indic-speak",
            input=sentence,
            voice="Kavya",
            instructions=f'{{"lang": "{languages[category]}"}}'
        )

        file_path = f"audio/bodhan/{category}.wav"

        speech.write_to_file(file_path)

        elapsed = time.perf_counter() - start

        print(f"Successfully generated: {file_path}")
        print(f"Time taken: {elapsed:.2f} seconds")

    except Exception as e:
        print(f"Failed for category {category}: {e}")

print("\nBodhan testing completed!")
