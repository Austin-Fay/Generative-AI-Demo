# Generative AI Python Demo (Prompt-Based)

This project is a proof-of-concept demonstrating generative ai using programmed randomized prompt generation. Built on OpenAI's GPT and DALL·E models, the script generates creative prompts and produces high-quality AI-generated images. In this case, endless Galactic Cats.

## How It Works

1. **Randomized Prompt Generation:**  
   The script randomly selects values for the type of cat, an emotion, an action (verb), an object (noun), and an artistic style.  
   Example: "A supermassive grey cat who is joyfully trying to play with a black hole in a surreal style."

   ```python
   BASE_PROMPT = "I need you to generate an image of a supermassive, {cat}, cat who is {emotion} trying to {verb} {noun}. Use a {style} style. Absolutely no text."

    CATS = ["grey", "black", "white", "orange", "tabby", "calico", "siamese", "persian", "ragdoll", "sphynx", "maine coon", "bengal", "scottish fold", "british shorthair", "exotic shorthair", "norwegian forest", "chartreux"]
    EMOTIONS = ["angrily", "pleasantly", "cautiously", "confusedly", "timidly", "joyfully", "scaredly", "melancholically", "indifferently", "euphorically", "disappointedly", "mysteriously", "playfully", "curiously", "thoughtfully", "intensely"]
    VERBS = ["consume", "destroy", "play with", "observe", "protect", "manipulate", "chase", "absorb", "contemplate", "capture", "explore", "challenge", "transform", "haunt", "unleash", "investigate", "monitor", "navigate"]
    NOUNS = ["a black hole", "the earth", "the moon", "a pulsar", "a quasar", "a neutron star", "a white dwarf", "the Milky Way", "a collapsing star", "an asteroid belt", "a cosmic storm", "a wormhole", "an alien spacecraft", "a floating city", "an entire galaxy", "an alternate dimension", "a futuristic space station", "an unknown planet"]
    STYLES = ["hyper-realistic", "surreal", "1990s cartoon", "pop art", "new age", "graffiti street art", "psychedelic", "steampunk", "dark fantasy", "futuristic neon", "abstract expressionism", "minimalist sci-fi", "cyberpunk", "retro-futurism", "vintage comic book", "space opera"]

    def prompt_gen():
    """Generate a random prompt for image generation"""
    cat = random.choice(CATS)
    emotion = random.choice(EMOTIONS)
    verb = random.choice(VERBS)
    noun = random.choice(NOUNS)
    style = random.choice(STYLES)
    return cat, emotion, verb, noun, style


2. **Prompt Enhancement:**  
   The generated prompt is refined using OpenAI's GPT model to make the description more engaging and visually rich.

   ```python
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

3. **Image Generation:**  
   The enhanced prompt is used to generate an image via DALL·E, resulting in a unique visual based on the input description.

    ```python
    def generate_img(prompt):
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


4. **Output:**  
   The generated image URL is printed, along with the enhanced prompt.

   ```bash
   Random Prompt: I need you to generate an image of a supermassive, calico, cat who is disappointedly trying to investigate a floating city. Use a steampunk style. Absolutely no text.
   
   Prompt: A supermassive calico cat, with vibrant patches of orange, black, and white fur, sits atop a cloud, its large, expressive eyes filled with curiosity and disappointment. Below, a sprawling steampunk city floats majestically in the sky, adorned with brass gears, intricate clockwork mechanisms, and billowing steam. Airships glide gracefully between towering spires, while whimsical contraptions dangle from the edges. The cat, with its oversized paws and fluffy tail, leans forward, peering down at the bustling city, its whiskers twitching in intrigue. The scene is bathed in a warm, golden light, casting a magical glow over the fantastical landscape.


## Built on OpenAI

This project relies entirely on OpenAI's GPT and DALL·E models for both text-based prompt refinement and image generation. 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Austin-Fay/Generative-AI-Demo.git
   cd Generative-AI-Demo

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
    ```bash
    pip install openai python-dotenv

4. Set up environment variables in a .env file:
    ```bash
    OPENAI_KEY=your_key_here

## Usage
- Run the script to generate an AI-enanced image and prompt:

    ```bash
    python main.py

## Requirements
    - Python 3.x
    - OpenAI API key

## License
This project is licensed under the MIT License. 

