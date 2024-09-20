import openai
import random
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

client = openai.OpenAI(api_key=OPENAI_KEY)

BASE_PROMPT = "I need you to generate an image of a supermassive, {cat}, cat who is {emotion} trying to {verb} {noun}. Use a {style} style. Absolutely no text."

# Lists of words to use in the prompt
CATS = ["grey", "black", "white", "orange", "tabby", "calico", "siamese", "persian", "ragdoll", "sphynx", "maine coon", "bengal", "scottish fold", "british shorthair", "exotic shorthair", "norwegian forest", "chartreux"]
EMOTIONS = ["angrily", "pleasantly", "cautiously", "confusedly", "timidly", "joyfully", "scaredly", "melancholically", "indifferently", "euphorically", "disappointedly", "mysteriously", "playfully", "curiously", "thoughtfully", "intensely"]
VERBS = ["consume", "destroy", "play with", "observe", "protect", "manipulate", "chase", "absorb", "contemplate", "capture", "explore", "challenge", "transform", "haunt", "unleash", "investigate", "monitor", "navigate"]
NOUNS = ["a black hole", "the earth", "the moon", "a pulsar", "a quasar", "a neutron star", "a white dwarf", "the Milky Way", "a collapsing star", "an asteroid belt", "a cosmic storm", "a wormhole", "an alien spacecraft", "a floating city", "an entire galaxy", "an alternate dimension", "a futuristic space station", "an unknown planet"]
STYLES = ["hyper-realistic", "surreal", "1990s cartoon", "pop art", "new age", "graffiti street art", "psychedelic", "steampunk", "dark fantasy", "futuristic neon", "abstract expressionism", "minimalist sci-fi", "cyberpunk", "retro-futurism", "vintage comic book", "space opera"]

def prompt_gen():
    """Uses python to generate a random prompt using the lists above"""
    cat = random.choice(CATS)
    emotion = random.choice(EMOTIONS)
    verb = random.choice(VERBS)
    noun = random.choice(NOUNS)
    style = random.choice(STYLES)
    return cat, emotion, verb, noun, style

def enhance_prompt(cat, emotion, verb, noun, style):
    """Enhance the generated prompt using GPT-4"""
    base_prompt = BASE_PROMPT.format(cat=cat, emotion=emotion, verb=verb, noun=noun, style=style)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": '''
                 You are a DALL·E 3 prompt engineer. 
                 Your goal is to enhance the user's prompt by adding creative and imaginative details that evoke a strong visual while retaining the basic prompt parameters. 
                 Focus on improving the scene's description, ensuring it's clear, engaging, and visually compelling to generate the best galactic cat image.
                 Keep the enhanced description concise but visually rich.
                 The following is the user's prompt that you need to enhance provide the enhanced prompt and nothing else.
                 '''},
                {"role": "user", "content": base_prompt}
            ],
            max_tokens=1320,
            temperature=0.333
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error enhancing prompt: {e}")
        return base_prompt

def image_gen(prompt):
    """Generate an image using OpenAI's DALL·E"""
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            quality="hd",
            style="vivid",
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def main():
    cat, emotion, verb, noun, style = prompt_gen()
    enhanced_prompt = enhance_prompt(cat, emotion, verb, noun, style)
    image_url = image_gen(enhanced_prompt)

    if image_url:
        print(f"Generated Image URL: {image_url}")
        print(f"Random Prompt: {BASE_PROMPT.format(cat=cat, emotion=emotion, verb=verb, noun=noun, style=style)}")
        print(f"Prompt: {enhanced_prompt}")
    else:
        print("Error generating image")
        main()

if __name__ == "__main__":
    main()
