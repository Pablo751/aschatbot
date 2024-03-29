# AI Astrologer

The AI Astrologer is a Python script that uses the OpenAI API to generate personalized astrological insights based on a user's sign combination and a selected question.

## Prerequisites

Before running the script, you'll need to have the following prerequisites installed:

- Python 3.x
- OpenAI API key

### Installing Dependencies

1. Create a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Setting up the OpenAI API Key

- Obtain an OpenAI API key from the OpenAI website.
- Create a `.env` file in the root directory of the project and add the following line, replacing `your_api_key_here` with your actual API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

- Navigate to the `src` directory:

```bash
cd src
```

- Run the `ai_astrologer.py` script:

```bash
python ai_astrologer.py
```

- Follow the prompts in the terminal to enter your astrological sign combination and select a question.

## How it Works

The `ai_astrologer.py` script works as follows:

1. The script loads two CSV files: `realdata.csv` and `QA2.csv`. The `realdata.csv` file contains information about various astrological sign combinations, while `QA2.csv` contains a list of questions.
2. The user is prompted to enter their astrological sign combination (e.g., "Aries Metal Monkey").
3. The script checks if the entered sign combination exists in the `realdata.csv` file. If not, the user is asked to enter a valid combination.
4. The user is then presented with a list of questions from the `QA2.csv` file and asked to select one.
5. Based on the selected question and the user's sign combination, the script constructs a prompt that includes relevant information from the `realdata.csv` file.
6. The prompt is sent to the OpenAI API using the gpt-3.5-turbo model, which generates a response tailored to the user's sign combination and the selected question.
7. The generated response is displayed to the user.
8. The user can choose to ask another question or exit the script.

### Understanding and Modifying the CSV Files

The AI Astrologer script relies on two CSV files: `realdata.csv` and `QA2.csv`. These files play a crucial role in generating personalized astrological insights. Here's how they work and how you can modify them:

#### `realdata.csv`

This file contains detailed attributes for various astrological sign combinations. Each row represents a unique sign combination (e.g., "Aries Metal Monkey") and provides insights across several categories like love, career, self-traits, compatibility, etc.

**Columns:**

- **SIGN:** The combination of a zodiac sign and an element/animal (e.g., "Aries Metal Monkey").
- **LOVE - WORDS, LOVE LANGUAGE:** Descriptions and preferred love languages for the sign combination.
- **CAREER - CHARACTERISTICS, SECTOR, JOBS:** Attributes related to career preferences, ideal sectors, and job titles.
- **MYSELF - TRAITS, CHALLENGES, TYPE, RULING PLANET, GEMSTONES, FULL MOON, YEAR OF THE DRAGON:** Various personal traits, challenges, personality types, ruling planets, gemstones, effects during the full moon, and characteristics for the year of the Dragon.
- **COMPATIBILITY:** Compatibility with other signs.

**Modifying `realdata.csv`:**

To add a new sign combination or update an existing one, simply modify the CSV file accordingly. Ensure you maintain the format and provide information for each column relevant to the sign combination you're adding or updating.

#### `QA2.csv`

This file contains a list of questions that can be asked by the user, along with the mapping to the relevant columns in the `realdata.csv` file. This structure allows the script to fetch and construct responses based on the selected question and user's sign combination.

**Columns:**

- **Question:** The question that can be asked by the user.
- **Main category:** The broad category to which the question belongs (e.g., Love, Career, Myself, Compatibility).
- **Column 1, Column 2, Column 3:** These columns specify which columns from `realdata.csv` should be used to construct the answer. It allows the script to dynamically fetch relevant data based on the question.

**Modifying `QA2.csv`:**

To add new questions or modify existing ones:
1. Add a row for each new question.
2. Specify the main category.
3. Indicate which columns from `realdata.csv` are relevant for constructing the response to this question.


## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
