
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Bodhan client
client = OpenAI(
    base_url="https://api.bodhan.ai/v1",
    api_key=os.getenv("BODHAN_API_KEY")
)

# Hindi test sentence
text = "सबसे पहले प्याज़ और टमाटर को बारीक काट लें।"

# Generate speech
start_time = time.perf_counter()

speech = client.audio.speech.create(
    model="indic-speak",
    input=text,
    voice="Kavya",
    instructions='{"lang": "hi"}'
)

end_time = time.perf_counter()

# Create output directory
os.makedirs("audio/bodhan", exist_ok=True)

# Save audio
speech.write_to_file("audio/bodhan/test1.wav")

print("Audio generated successfully!")
print(f"Generation time: {end_time - start_time:.2f} seconds")
