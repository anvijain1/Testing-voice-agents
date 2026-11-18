
import os
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import save

# Load environment variables
load_dotenv()

# Initialize Sarvam client
client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

# Hindi test sentence
text = "सबसे पहले प्याज़ और टमाटर को बारीक काट लें।"

# Generate speech
audio = client.text_to_speech.convert(
    model="bulbul:v4-flash",
    text=text,
    language_code="hi-IN",
    speaker="aparna_hi_customer"
)

# Create output directory
os.makedirs("audio/sarvam", exist_ok=True)

# Save generated audio
save(audio, "audio/sarvam/test1.wav")

print("Audio generated successfully!")

