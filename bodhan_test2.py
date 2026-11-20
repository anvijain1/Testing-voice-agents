
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

# Input dictionary
text = {
    # HINDI
    "H-N01": "इसमें 250 मिलीलीटर दूध और 100 मिलीलीटर पानी डालें।",
    "H-N02": "500 ग्राम आटे में आधा चम्मच नमक मिलाएँ।",
    "H-N03": "इस मिश्रण को 180 डिग्री पर 20 मिनट तक बेक करें।",

    # MARATHI
    "MR-N01": "यामध्ये 240 मिलीलीटर दूध आणि १०० मिलीलीटर पाणी घाला.",
    "MR-N02": "५०० ग्रॅम पिठात अर्धा चमचा मीठ मिसळा.",
    "MR-N03": "हे मिश्रण १८० अंश तापमानावर २० मिनिटे बेक करा.",

    # TAMIL
    "TA-N01": "இதில் 250 மில்லிலிட்டர் பால் மற்றும் 100 மில்லிலிட்டர் தண்ணீர் சேர்க்கவும்.",
    "TA-N02": "500 கிராம் மாவில் அரை தேக்கரண்டி உப்பு சேர்க்கவும்.",
    "TA-N03": "இந்த கலவையை 180 டிகிரியில் 20 நிமிடங்கள் பேக் செய்யவும்.",

    # MALAYALAM
    "ML-N01": "ഇതിൽ 250 മില്ലിലിറ്റർ പാലും 100 മില്ലിലിറ്റർ വെള്ളവും ചേർക്കുക.",
    "ML-N02": "500 ഗ്രാം മാവിൽ അര ടീസ്പൂൺ ഉപ്പ് ചേർക്കുക.",
    "ML-N03": "ഈ മിശ്രിതം 180 ഡിഗ്രിയിൽ 20 മിനിറ്റ് ബേക്ക് ചെയ്യുക.",

    # KANNADA
    "KN-N01": "ಇದಕ್ಕೆ 250 ಮಿಲಿಲೀಟರ್ ಹಾಲು ಮತ್ತು 100 ಮಿಲಿಲೀಟರ್ ನೀರು ಸೇರಿಸಿ.",
    "KN-N02": "500 ಗ್ರಾಂ ಹಿಟ್ಟಿಗೆ ಅರ್ಧ ಚಮಚ ಉಪ್ಪು ಸೇರಿಸಿ.",
    "KN-N03": "ಈ ಮಿಶ್ರಣವನ್ನು 180 ಡಿಗ್ರಿಯಲ್ಲಿ 20 ನಿಮಿಷ ಬೇಯಿಸಿ."
}

# Language mapping
languages = {
    "H": "hi",
    "MR": "mr",
    "TA": "ta",
    "ML": "ml",
    "KN": "kn"
}

# Folder mapping
language_folders = {
    "H": "hindi",
    "MR": "marathi",
    "TA": "tamil",
    "ML": "malayalam",
    "KN": "kannada"
}

# Base output directory
base_path = "audio_test2/bodhan"

# Generate audio for each category
for category, sentence in text.items():

    # Identify language
    language_group = category.split("-")[0]

    language_code = languages[language_group]
    folder_name = language_folders[language_group]

    # Create language-specific folder
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    print(f"\nGenerating Bodhan audio: {category}")
    print(f"Language: {folder_name}")

    start = time.perf_counter()

    try:
        # Generate speech
        speech = client.audio.speech.create(
            model="indic-speak",
            input=sentence,
            voice="Kavya",
            instructions=f'{{"lang": "{language_code}"}}'
        )

        # Save audio
        file_path = os.path.join(folder_path, f"{category}.wav")
        speech.write_to_file(file_path)

        elapsed = time.perf_counter() - start

        print(f"Successfully generated: {file_path}")
        print(f"Time taken: {elapsed:.2f} seconds")

    except Exception as e:
        print(f"Failed for category {category}: {e}")

print("\nBodhan testing completed!")
