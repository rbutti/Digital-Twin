# Digital Twin

A Python-based AI career assistant that presents a conversational "digital twin" of a person through a Gradio chat interface. The app uses a resume pulled from GitHub as system context, answers professional questions about background and experience, and can record contact interest or unanswered questions for follow-up.

## What this project does

This project creates a website-like chat experience where visitors can ask about:

- career background and experience
- technical skills and project work
- professional interests and strengths
- how to get in touch

The app is built around a single Gradio chat interface and an OpenAI-compatible model (configured via OpenRouter). The system prompt is populated from a PDF resume stored in a private GitHub repository, so the model answers in-character as the represented person rather than as a generic assistant.

LIVE APP Link: https://agentic-professional-twin.onrender.com/

## Stack

- Language: Python 3.12
- UI: Gradio
- LLM API: OpenAI SDK with OpenRouter
- Resume ingestion: PyPDF
- Email capture: Resend
- Environment config: python-dotenv
- Deployment: Render

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

## Example prompts

The UI includes example prompts such as:

- Tell me about your background and experience.
- What kinds of projects are you working on now?
- What are your strongest technical skills?
- How can I get in touch with you?


## Considerations
- Contact capture requires valid Resend credentials.
- The project is designed for a personal portfolio use case and not a generic multi-purpose assistant.
- The repository is currently minimal and intentionally focused on one workflow: a professional AI twin for a personal site.

## License

No explicit license file is present in the repository.
