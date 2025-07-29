import os
import argparse
import random
import sys

# Try to import AI libraries, and provide a helpful error message if they're not installed.
try:
    import openai
    from openai import OpenAI
except ImportError:
    print("OpenAI library not found. Please run 'pip install openai'")
    openai = None

try:
    import google.generativeai as genai
except ImportError:
    print("Google Generative AI library not found. Please run 'pip install google-generativeai'")
    genai = None

# --- Prompt Engineering: The "Brain" of the AI ---
# This detailed prompt tells the AI how to behave.
def create_prompt(deep_tech_statement):
    """Creates the detailed instruction prompt for the AI model."""

    # Randomly select a ridiculous, made-up ARR number for exaggeration.
    random_arr = f"${random.randint(1, 15)}.{random.randint(0, 9)}M"
    random_mrr = f"${random.randint(100, 950)}k"

    return f"""
    You are a 'B2B SaaS Vertical AI Agent Jargonizer 9000'.
    Your job is to translate boring, literal deep-tech statements into over-the-top, exaggerated B2B SaaS jargon. This is for a satirical joke project.

    **Your Translation Rules:**
    1.  **Exaggerate Wildly:** Turn any small improvement into a world-changing disruption. A 10% efficiency gain is now a "10x paradigm shift."
    2.  **Inject SaaS Metrics:** Always mention unbelievable financial metrics like Monthly Recurring Revenue (MRR) or Annual Recurring Revenue (ARR). Use these fake numbers: ARR of **{random_arr}** and MRR of **{random_mrr}**.
    3.  **Use Buzzwords:** Liberally sprinkle in terms like 'AI-powered', 'next-generation', 'disruptive', 'hyper-scalable', 'cloud-native', 'synergistic', 'MLOps-driven', 'LLM-infused', 'vertical AI agent', and 'paradigm shift'.
    4.  **Identify a Target:** Frame the company as a "B2B SaaS" or "vertical AI agent" business that is attacking a "traditional," "legacy," "billion-dollar" industry.
    5.  **Be Confident:** The tone should be arrogant, visionary, and slightly unhinged, like a caricature of a tech founder.

    **Example:**
    *   **Boring Input:** "We are a deep tech organic chemistry research company producing new methods for drug discovery and testing."
    *   **Your Jargonized Output:** "We are a hyper-scalable, AI-powered vertical agent for the pharma sector, disrupting a multi-billion dollar legacy industry with our proprietary LLM-infused platform. We're pre-product but are already projecting a **{random_arr}** ARR by Q4."

    Now, translate the following deep-tech statement. Be as ridiculous as possible.

    **Boring Input:** "{deep_tech_statement}"
    **Your Jargonized Output:**
    """
    
def call_openai(api_key, prompt):
    """Calls the OpenAI API and returns the response."""
    if not openai:
        sys.exit("OpenAI library is required but not installed.")
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful but satirical AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8 # Higher temperature for more "creative" and unhinged responses
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred with OpenAI: {e}"

def call_gemini(api_key, prompt):
    """Calls the Google Gemini API and returns the response."""
    if not genai:
        sys.exit("Google Generative AI library is required but not installed.")
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred with Gemini: {e}"

def main():
    """Main function to parse arguments and run the tool."""
    parser = argparse.ArgumentParser(
        description="SaaS-ify: The Deep Tech Jargonizer 9000 (A Joke Tool)",
        epilog="Example: python main.py --provider openai --text \"Our new battery lasts 20% longer.\""
    )
    parser.add_argument(
        "--provider",
        type=str,
        choices=["openai", "gemini"],
        required=True,
        help="The AI provider to use."
    )
    parser.add_argument(
        "--text",
        type=str,
        help="The deep-tech sentence to be jargonized."
    )

    args = parser.parse_args()

    if args.text:
        input_text = args.text
    else:
        input_text = input("Enter your deep-tech statement: ")

    api_key = None
    if args.provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            sys.exit("Error: OPENAI_API_KEY environment variable not set. Please set it before running.")
        translator_func = call_openai

    elif args.provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            sys.exit("Error: GEMINI_API_KEY environment variable not set. Please set it before running.")
        translator_func = call_gemini

    # Create the detailed prompt and get the jargonized output
    full_prompt = create_prompt(input_text)
    jargon_output = translator_func(api_key, full_prompt)

    print("\n--- Deep Tech Statement ---\n")
    print(f"\"{input_text}\"")
    print("\n--- SaaS-ified Jargon! ---\n")
    print(jargon_output)

if __name__ == "__main__":
    main()
