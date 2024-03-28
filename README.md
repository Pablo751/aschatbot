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

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
