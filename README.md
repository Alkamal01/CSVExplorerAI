# CSVExplorerAI

CSVExplorerAI is a Streamlit-powered web application that allows users to interactively explore and query CSV data using natural language.

## Features

- Upload and explore CSV files.
- Ask questions about your data using natural language.
- Receive answers and insights based on OpenAI language models.
- Simple and user-friendly interface.

## Getting Started

### Prerequisites

- Python (version >= 3.7)
- [Streamlit](https://streamlit.io/)
- [OpenAI API Key](https://beta.openai.com/signup/) (Set it as an environment variable: `OPENAI_API_KEY`)

### Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/Alkamal01/CSVExplorerAI.git]
    cd CSVExplorerAI
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Set your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY="your_api_key_here"
    ```

2. Run the application:

    ```bash
    streamlit run main.py
    ```

3. Open your web browser and go to `http://localhost:8501`.

## Contributing

If you'd like to contribute to CSVExplorerAI, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

