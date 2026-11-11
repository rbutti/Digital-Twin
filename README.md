# Digital Twin

A Python-based AI career assistant that presents a conversational "digital twin" of a person through a Gradio chat interface. The app uses a resume pulled from GitHub as system context, answers professional questions about background and experience, and can record contact interest or unanswered questions for follow-up.

## What this project does

This project creates a website-like chat experience where visitors can ask about:

- career background and experience
- technical skills and project work
- professional interests and strengths
- how to get in touch

The app is built around a single Gradio chat interface and an OpenAI-compatible model (configured via OpenRouter). The system prompt is populated from a PDF resume stored in a private GitHub repository, so the model answers in-character as the represented person rather than as a generic assistant.

## Stack

- Language: Python 3.12
- UI: Gradio
- LLM API: OpenAI SDK with OpenRouter
- Resume ingestion: PyPDF
- Email capture: Resend
- Environment config: python-dotenv

## Repository structure

```text
.
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── unknownQues.txt
└── src/
    └── digital_twin/
        ├── __init__.py
        ├── app.py
        ├── context.py
        ├── styles.py
        └── tools.py
```

### Main modules

- `src/digital_twin/app.py`  
  Starts the Gradio chat interface, sends prompts to the model, and handles tool-calling loops.

- `src/digital_twin/context.py`  
  Loads environment variables, downloads a resume PDF from GitHub, extracts text, and builds the system prompt used by the assistant.

- `src/digital_twin/tools.py`  
  Defines tool schemas for recording user details and unknown questions, plus the functions that trigger email sending and file logging.

- `src/digital_twin/styles.py`  
  Adds custom CSS for the chat UI so the interface looks polished and branded.

## How the app works

The flow is straightforward:

1. The app loads environment variables from a `.env` file.
2. `context.py` fetches a PDF resume from a GitHub repository (`rbutti/private-store`) using a GitHub token.
3. The text is extracted with `pypdf` and embedded into `TWIN_SYSTEM_PROMPT`.
4. `app.py` sends the system prompt, chat history, and user message to the configured model via OpenRouter.
5. If the model requests a tool call, `handle_tool_calls()` executes it.
6. Tool actions include:
   - `record_user_details` to log contact interest and send an email via Resend
   - `record_unknown_question` to append a question to `unknownQues.txt`

## Environment variables

Create a `.env` file in the project root with values like:

```env
OPENROUTER_API_KEY=your_openrouter_key
GITHUB_TOKEN=your_github_token
RESEND_API_KEY=your_resend_api_key
EMAIL_ADDRESS=you@example.com
```

Notes:

- `GITHUB_TOKEN` is used to fetch the resume PDF from the private GitHub repo.
- `RESEND_API_KEY` and `EMAIL_ADDRESS` are used for contact capture emails.
- `OPENROUTER_API_KEY` is required for model access.

## Local setup

This project uses `uv` and includes a `pyproject.toml`.

```bash
# install dependencies
uv sync

# run the app
uv run python src/digital_twin/app.py
```

You can also run it with a standard virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python src/digital_twin/app.py
```

## Running notes

- The app launches a Gradio chat interface with example prompts.
- The default model is configured as `openrouter/free` with the OpenRouter base URL.
- The app is intended to act as a professional digital twin for a personal website or portfolio.

## Example prompts

The UI includes example prompts such as:

- Tell me about your background and experience.
- What kinds of projects are you working on now?
- What are your strongest technical skills?
- How can I get in touch with you?

## Key implementation details

The main logic is intentionally small and focused:

- `chat()` builds the message list and loops while the model requests tool calls.
- `tools.py` defines the function calling schema the model can invoke.
- `styles.py` customizes Gradio to feel more tailored to a portfolio or professional site.
- `context.py` is the memory layer that keeps the model grounded in the represented person's resume.

## Limitations and considerations

- The app assumes access to a valid GitHub token and a publicly accessible private-resume endpoint.
- Contact capture requires valid Resend credentials.
- The project is designed for a personal portfolio use case and not a generic multi-purpose assistant.
- The repository is currently minimal and intentionally focused on one workflow: a professional AI twin for a personal site.

## License

No explicit license file is present in the repository.
