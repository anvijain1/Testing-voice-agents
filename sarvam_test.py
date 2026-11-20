
import os
import time
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import save

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
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
    "A": "hi-IN",
    "B": "hi-IN",
    "C": "hi-IN",
    "D": "mr-IN",
    "E": "hi-IN"
}

os.makedirs("audio/sarvam", exist_ok=True)

# Generate audio for each category
for category, sentence in text.items():

    print(f"\nGenerating Sarvam audio: {category}")

    start = time.perf_counter()

    try:
        audio = client.text_to_speech.convert(
            model="bulbul:v4-flash",
            text=sentence,
            language_code=languages[category],
            speaker="aparna_hi_customer"
        )

        file_path = f"audio/sarvam/{category}.wav"

        save(audio, file_path)

        elapsed = time.perf_counter() - start

        print(f"Successfully generated: {file_path}")
        print(f"Time taken: {elapsed:.2f} seconds")

    except Exception as e:
        print(f"Failed for category {category}: {e}")

print("\nSarvam testing completed!")


