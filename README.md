# SaaS-ify: The VC Pitch Jargonizer

![Joke](https://img.shields.io/badge/purpose-a%20complete%20joke-red)
![For Founders](https://img.shields.io/badge/for-Founders%20&%20VCs-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tired of your brilliant deep-tech breakthrough getting no traction from VCs? This command-line tool translates your pitch into VC-friendly B2B SaaS jargon they actually want to hear.

> **Disclaimer:** This is a parody tool. Using this in a real pitch might get you laughed out of the room... or it might get you funded. Who knows?

### The Problem It Solves

It helps you turn your honest, technical pitch...

`"Our new material is lighter and stronger."`

...into a VC-ready pitch that sounds like this:

`"We've developed a proprietary, AI-driven materials discovery platform to create next-generation composites, disrupting the $500B legacy manufacturing sector. Our hyper-scalable, cloud-native solution provides a 10x improvement in strength-to-weight ratios, creating an unassailable moat. We're pre-revenue but are projecting a $15M ARR by Q4."`

***

### Setup and Installation

**1. Clone the Repository**

```bash
git clone [https://github.com/ion-fullstack/SaaS-ify.git](https://github.com/ion-fullstack/SaaS-ify.git)
cd SaaS-ify
```

**2. Install Dependencies**
Make sure you have Python 3 installed. Then, install the required libraries.

```bash
pip install -r requirements.txt

```

**3. Set Your API Key**
This tool requires an API key from either OpenAI or Google to power the jargon engine. It reads the key securely from an environment variable.

**Choose ONE provider and set the key:**

*   **For OpenAI:**
Get your key from [platform.openai.com](https://platform.openai.com/api-keys). Then set the environment variable.

    *   On macOS/Linux:

```bash
export OPENAI_API_KEY="your_secret_api_key_here"
```

    *   On Windows (Command Prompt):

```bash
set OPENAI_API_KEY="your_secret_api_key_here"
```

*   **For Google Gemini:**
    Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey). Then set the environment variable.

    *   On macOS/Linux:
    
```bash 
export GEMINI_API_KEY="your_secret_api_key_here"
```

    *   On Windows (Command Prompt):
    
```bash
set GEMINI_API_KEY="your_secret_api_key_here"
```

> **Note:** If using an IDE like PyCharm, it's recommended to set the environment variable in the "Run/Debug Configuration" instead.

### Usage

You can run the script in two ways: by providing text directly as an argument or through an interactive prompt.

**Metohod 1: Command-Line Argument**
Provide the AI provider and the deep-tech pitch line you want to translate.

Syntax:

```bash
python main.py --provider <openai_or_gemini> --text "Your honest pitch line here."
```

Example (Using OpenAI):

```bash
python main.py --provider openai --text "We built a sensor that can detect metal fatigue more accurately."
**Using OpenAI:**
```
Method 2: Interactive Mode

For a more conversational experience, run the script with only the provider argument. It will then prompt you to enter your text.
Syntax:

```bash
python main.py --provider <openai_or_gemini>
```

Example (Using Gemini):

```bash
python main.py --provider gemini
```

The script will then display:
```bash
Enter your deep-tech statement: 
```

Simply type your sentence and press Enter to get the output. 

And there you go! You can now translate all your deep/hard-tech cold emails, pitches, or application responses to B2B-SaaS-equivalent statements that VCs can actually understand!
