# ai-llm-simple-chat

## Description
ai-llm-simple-chat is a Flask-based web application that provides a simple chat interface powered by Large Language Models (LLMs). It demonstrates how to build a basic chat application using Python, Flask, and OpenAI's API. The application features a clean, user-friendly interface for real-time conversations with an AI assistant.

## How It Works
1. **User Interface**: The application provides a web-based chat interface built with Flask and modern CSS.
2. **Message Handling**: When a user sends a message, it's processed through Flask routes and securely sent to the OpenAI API.
3. **LLM Integration**: The application communicates with OpenAI's Language Models to generate contextually relevant responses.
4. **Response Display**: The AI's response is returned to the user interface and displayed in real-time in the chat window.
5. **Environment Management**: The application uses environment variables for secure API key storage and configuration management.

## File Structure
```
ai-llm-simple-chat/
├── .venv/                 # Virtual environment directory
├── app/                   # Main application directory
│   ├── static/           # Static files directory
│   └── templates/        # HTML templates directory
│   ├── __init__.py       # Package initializer
│   ├── main.py           # Main application logic
│   ├── models.py         # Data models
│   ├── routes.py         # API routes
├── tests/              # Test directory
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── .python-version        # Python version file
├── LICENSE               # License file
├── main.py              # Entry point
├── pyproject.toml       # Project metadata and dependencies
├── README.md            # This file
└── uv.lock             # UV package manager lock file
```

## Getting Started
1. Clone the repository:
     ```sh
     git clone https://github.com/NormLorenz/ai-llm-simple-chat.git
     ```
2. Navigate to the project directory:
     ```sh
     cd ai-llm-simple-chat
     ```

3. Install uv (if not already installed)
     ```sh
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```
4. Install the dependencies:
     ```sh
     uv sync
     ```
5. Run the application:
     ```sh
     uv run run.py
     ```

6. Test the application:
     ```sh
     python -m unittest discover -s tests
     ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Convert pip (using a requirments.txt file) to uv (using a uv.lock file) package manager
```ps
uv init
uv sync
uv add -r requirements.txt
uv pip freeze # to list requirments
uv lock
```

## Create a new .env file
```ps
New-Item -Path ".\.env" -ItemType File
```

## Remove old pip files
```ps
rm requirements.txt
rm config.py
rm run.py (if it exists)
``` 