#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from openai import OpenAI
import pandas as pd
import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load the CSV data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')
df = pd.read_csv(os.path.join(data_dir, 'realdata.csv'))
questions_df = pd.read_csv(os.path.join(data_dir, 'QA2.csv'))

def get_all_sign_info(sign_combination):
    """
    Fetch all information for a given sign combination from the CSV data.
    """
    print(f"Fetching info for: {sign_combination}")  # Debug print
    row = df[df['SIGN'].str.casefold() == sign_combination.casefold()]

    if row.empty:
        return "No information found for this sign combination."

    all_info = ' | '.join([f"{col}: {row[col].values[0]}" for col in df.columns[1:]])  # Adjust if needed
    return all_info

def generate_response(question_row, sign_combination):
    """
    Generate a response from the OpenAI API based on the provided question and sign combination,
    including only relevant category information in the prompt.
    """
    # Fetch the row for the sign combination
    row = df[df['SIGN'].str.casefold() == sign_combination.casefold()]
    if row.empty:
        return "No information found for this sign combination."

    # Only select columns specified in the question_row from the QA sheet
    relevant_columns = [col for col in question_row[['Column 1', 'Column 2', 'Column 3']].dropna()]
    relevant_info = ' | '.join([f"{col}: {row.iloc[0][col]}" for col in relevant_columns if col in row.columns])

    opening_phrases = [
        "you're a force to be reckoned with",
        "you're the embodiment of magnetism",
        "you're a fiery enigma wrapped in a tantalizing package",
        "you're a captivating blend of traits",
        "you're an irresistible mystery waiting to be unraveled",
        "you're a walking, talking enchantment",
        "you're a spellbinding combination of elements",
        "you're a mesmerizing paradox",
        "you're an alluring riddle that everyone wants to solve",
        "you're a tantalizing fusion of characteristics"
    ]

    random_opening = random.choice(opening_phrases)

    prompt = f"You are a sassy and mysterious Life Coach with expertise in astrology, offering insights to someone with the combined astrological sign '{sign_combination}', which represents a unique blend of traits from each element. They are exhibiting traits such as {', '.join([row.iloc[0][col] for col in relevant_columns if col in row.columns])}. They are on a journey of personal growth and self-discovery, asking, '{question_row['Question:']}' Respond in a fun, sassy, and mysterious way, providing wisdom, encouragement, and practical tips to help them embrace their authentic self, considering the combined traits of their astrological sign '{sign_combination}'. Use bold statements, playful language, and a touch of intrigue in your response. Start the answer by referring to their combined sign in a playful manner, e.g., 'As a {sign_combination}, {random_opening}...'. Focus on delivering the core message with sass and mystery, leaving them yearning for more. Avoid generic starting lines, sign-off messages, and the phrase 'my dear'."

    print("\n--- Prompt Info ---")
    print(f"Prompt: {prompt}\n")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sassy and mysterious AI astrologer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    response = completion.choices[0].message.content.strip()
    return response

def main():
    while True:
        sign_combination = input("Enter your astrological sign combination (e.g., 'Aries Metal Monkey'): ").casefold()
        if df['SIGN'].str.casefold().str.contains(sign_combination).any():
            break
        else:
            print("The sign combination entered was not found. Please try again.")

    while True:
        print("Available questions:")
        for i, row in questions_df.iterrows():
            print(f"{i+1}. {row['Question:']}")

        question_index = input("Select a question by number: ")
        try:
            question_index = int(question_index) - 1
            if question_index < 0 or question_index >= len(questions_df):
                raise ValueError
            question_row = questions_df.iloc[question_index]
        except ValueError:
            print("Invalid selection. Please enter a valid question number.")
            continue

        all_info = get_all_sign_info(sign_combination)
        print(f"Information for {sign_combination}: {all_info}")
        response = generate_response(question_row, sign_combination)
        print(f"Response: {response}")

        another_question = input("Would you like to ask another question? [y/n]: ").lower()
        if another_question != 'y':
            break

    print("Thank you for using the AI Astrologer!")

if __name__ == "__main__":
    main()

