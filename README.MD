# Voice AI Model Comparison: Sarvam AI vs Bodhan AI

## 1. Project Overview

This project evaluates and compares the Text-to-Speech (TTS) capabilities of **Sarvam AI** and **Bodhan AI (India Speak)** for a multilingual AI-powered cooking assistant.

The objective is to identify which model delivers better pronunciation, fluency, language accuracy, and numerical interpretation when generating cooking instructions.

The evaluation was divided into two tests, with both models receiving identical inputs to ensure a fair comparison.

## 2. Evaluation Parameters

Both models were evaluated using the following parameters:

| Parameter | Evaluation Criteria |
|---|---|
| Pronunciation | Correct pronunciation of words |
| Clarity | Ease of understanding speech |
| Naturalness | Human-like voice delivery |
| Language Accuracy | Naturalness in the target language |
| Numerical Accuracy | Correct pronunciation of quantities and units |
| Consistency | Stability of speech quality across sentences |

## 3. Testing Methodology

### Test 1: Basic Voice Quality Evaluation

**Objective:** To compare the baseline speech quality of both models using five simple inputs covering Hindi, Marathi, cooking terminology, measurements, and conversational questions.

**Test Categories:**

| Test ID | Category |
|---|---|
| A | Basic Hindi Cooking Instruction |
| B | Indian Cooking Terminology |
| C | Numbers & Measurements |
| D | Marathi Cooking Instruction |
| E | Conversational Questions |

**Input Dataset:**

```python
text = {
    "A": "सबसे पहले प्याज़ और टमाटर को बारीक काट लें।",
    "B": "अब इसमें कसूरी मेथी और गरम मसाला मिलाएँ।",
    "C": "लगभग 180 डिग्री तापमान पर 20 मिनट तक बेक करें।",
    "D": "सर्वप्रथम कांदा आणि टोमॅटो बारीक चिरून घ्या.",
    "E": "क्या मैं इसमें थोड़ा और पानी डाल सकती हूँ?"
}
```

This test evaluated pronunciation, fluency, cooking vocabulary, numerical speech, and conversational delivery.

### Test 2: Numerical Accuracy and Multilingual Evaluation

**Objective:** To examine how accurately both models interpret and pronounce numerical values across different Indian languages.

This test focused on measurements, fractions, temperatures, and cooking quantities. It also included Arabic numerals (250, 500, 180) and native-script numerals (१००, ५००, १८०).

**Test Categories:**

| Category | Test IDs |
|---|---|
| Hindi Quantities | H-N01–H-N03 |
| Marathi Quantities | MR-N01–MR-N03 |
| Tamil Quantities | TA-N01–TA-N03 |
| Malayalam Quantities | ML-N01–ML-N03 |
| Kannada Quantities | KN-N01–KN-N03 |

**Input Dataset:**

```python
text = {
    "H-N01": "इसमें 250 मिलीलीटर दूध और 100 मिलीलीटर पानी डालें।",
    "H-N02": "500 ग्राम आटे में आधा चम्मच नमक मिलाएँ।",
    "H-N03": "इस मिश्रण को 180 डिग्री पर 20 मिनट तक बेक करें।",

    "MR-N01": "यामध्ये 240 मिलीलीटर दूध आणि १०० मिलीलीटर पाणी घाला.",
    "MR-N02": "५०० ग्रॅम पिठात अर्धा चमचा मीठ मिसळा.",
    "MR-N03": "हे मिश्रण १८० अंश तापमानावर २० मिनिटे बेक करा.",

    "TA-N01": "இதில் 250 மில்லிலிட்டர் பால் மற்றும் 100 மில்லிலிட்டர் தண்ணீர் சேர்க்கவும்.",
    "TA-N02": "500 கிராம் மாவில் அரை தேக்கரண்டி உப்பு சேர்க்கவும்.",
    "TA-N03": "இந்த கலவையை 180 டிகிரியில் 20 நிமிடங்கள் பேக் செய்யவும்.",

    "ML-N01": "ഇതിൽ 250 മില്ലിലിറ്റർ പാലും 100 മില്ലിലിറ്റർ വെള്ളവും ചേർക്കുക.",
    "ML-N02": "500 ഗ്രാം മാവിൽ അര ടീസ്പൂൺ ഉപ്പ് ചേർക്കുക.",
    "ML-N03": "ഈ മിശ്രിതത്തെ 180 ഡിഗ്രിയിൽ 20 മിനിറ്റ് ബേക്ക് ചെയ്യുക.",

    "KN-N01": "ಇದಕ್ಕೆ 250 ಮಿಲಿಲೀಟರ್ ಹಾಲು ಮತ್ತು 100 ಮಿಲಿಲೀಟರ್ ನೀರು ಸೇರಿಸಿ.",
    "KN-N02": "500 ಗ್ರಾಂ ಹಿಟ್ಟಿಗೆ ಅರ್ಧ ಚಮಚ ಉಪ್ಪು ಸೇರಿಸಿ.",
    "KN-N03": "ಈ ಮಿಶ್ರಣವನ್ನು 180 ಡಿಗ್ರಿಯಲ್ಲಿ 20 ನಿಮಿಷ ಬೇಯಿಸಿ."
}
```

## 4. Key Observations

### Sarvam AI

**Strengths:**
- Produced more fluent and continuous speech.
- Demonstrated better Hindi and Marathi pronunciation.
- Maintained language-appropriate numerical pronunciation.
- Delivered relatively consistent speech across tested inputs.

**Limitations:**
- The voice sometimes sounded monotonous.
- Speech lacked sufficient tonal variation and expression, particularly in Hindi and Marathi.

### Bodhan AI – India Speak

**Strengths:**
- Provided an alternative voice-generation system for comparison.
- Was evaluated using the same datasets as Sarvam.

**Limitations:**
- Frequently pronounced numerical values in English, even when the surrounding sentence was in Hindi or Marathi.
- Demonstrated comparatively lower fluency in the tested samples.
- Numerical localization was a notable weakness.

## 5. Most Important Finding: Numerical Pronunciation

The most interesting observation emerged from Test 2.

Sarvam generally pronounced numerical values according to the language of the sentence, irrespective of whether the numbers were written using Arabic numerals or native-language numerals.

For example, numbers such as 250, 500, and 180 were generally spoken in Hindi when included in Hindi sentences.

The same behaviour was observed in Marathi.

In contrast, Bodhan frequently read numerical values in English, even when the rest of the sentence was in Hindi or Marathi.

**Why this matters:** In a cooking assistant, measurements are essential. Instructions involving 250 ml of milk, 500 grams of flour, or 180 degrees must be communicated naturally and accurately in the user's selected language.

## 6. Comparative Analysis

| Parameter | Sarvam AI | Bodhan AI |
|---|---|---|
| Pronunciation | Better in tested samples | Less consistent |
| Fluency | More fluent | Comparatively lower |
| Naturalness | Monotonous tone | Less fluent delivery |
| Language Accuracy | Better language-specific delivery | Some language-specific issues |
| Numerical Accuracy | Better language localization | Frequently used English pronunciation |
| Consistency | Relatively stable | Comparatively less consistent |

*Note: These are qualitative observations, not quantified benchmark scores.*

## 7. Final Verdict

**Preferred Model: Sarvam AI**

Based on the two tests, Sarvam AI was my preferred choice.

The main reasons were:

1. Better fluency in Hindi and Marathi.
2. More consistent language-specific pronunciation.
3. Better handling of numerical values and measurements.
4. More suitable multilingual numerical interpretation.
5. Relatively stable speech quality.

Although Sarvam had a monotonous tone, its overall performance was more suitable for the intended application.

## 8. Conclusion and Future Scope

The evaluation highlighted that multilingual TTS quality involves more than converting text into audio. Correct pronunciation of ingredients, quantities, measurements, and cooking instructions is essential for a reliable voice-based cooking assistant.

Sarvam AI is the preferred candidate for the next development stage.

Further evaluation should include native-speaker feedback, complete recipe narration, conversational commands, background kitchen noise, and repeated-generation consistency before final production integration.