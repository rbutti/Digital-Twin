# Gradio 6 custom CSS. Selectors match ChatInterface markup
# (.gradio-container, .user, .bot, .example, .input-container).
# Variables are set on the container so they override the theme
# for this app without fighting component stylesheets.

css = """
.gradio-container {
  --body-background-fill: #e7edf3;
  --body-text-color: #1c2834;
  --body-text-color-subdued: #5c6b7c;
  --background-fill-primary: #e7edf3;
  --background-fill-secondary: #ffffff;
  --block-background-fill: #ffffff;
  --block-border-color: #d5dee8;
  --block-border-width: 1px;
  --block-label-background-fill: #f4f7fb;
  --block-label-text-color: #1e3a5f;
  --block-title-background-fill: transparent;
  --block-title-text-color: #102033;
  --border-color-primary: #d5dee8;
  --border-color-accent: #1e4d7b;
  --border-color-accent-subdued: #c5d4e4;
  --color-accent: #1e4d7b;
  --color-accent-soft: #e7f0f8;
  --link-text-color: #1e4d7b;
  --link-text-color-hover: #163a5f;
  --input-background-fill: #ffffff;
  --input-border-color: #cfd8e3;
  --input-border-color-focus: #1e4d7b;
  --input-placeholder-color: #7b8b9c;
  --shadow-drop: 0 1px 2px rgba(16, 36, 58, 0.06);
  --shadow-drop-lg: 0 10px 28px rgba(16, 36, 58, 0.08);
  --button-primary-background-fill: #1e4d7b;
  --button-primary-background-fill-hover: #163a5f;
  --button-primary-text-color: #f8fafc;
  --button-primary-border-color: #1e4d7b;
  --button-secondary-background-fill: #ffffff;
  --button-secondary-background-fill-hover: #f4f7fb;
  --button-secondary-text-color: #1c2834;
  --button-secondary-border-color: #d5dee8;
  --block-radius: 12px;
  --input-radius: 12px;
  --radius-md: 12px;
  --radius-lg: 14px;
  --font: "Segoe UI", "Source Sans 3", "Helvetica Neue", Arial, sans-serif;
  --font-mono: "Cascadia Mono", "IBM Plex Mono", ui-monospace, Consolas, monospace;
  --chatbot-text-size: 15px;
  max-width: 920px;
  margin: 24px auto;
  padding: 8px 8px 0;
  border: 1px solid #d5dee8;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 16px 40px rgba(16, 36, 58, 0.08);
}

.dark .gradio-container,
.gradio-container.dark {
  --body-background-fill: #0f1720;
  --body-text-color: #e7eef6;
  --body-text-color-subdued: #9aabbd;
  --background-fill-primary: #0f1720;
  --background-fill-secondary: #17212c;
  --block-background-fill: #17212c;
  --block-border-color: #2a3a4c;
  --block-label-background-fill: #1c2938;
  --block-label-text-color: #d5e4f2;
  --block-title-text-color: #f3f7fb;
  --border-color-primary: #2a3a4c;
  --border-color-accent: #7eb0dc;
  --border-color-accent-subdued: #2c4a66;
  --color-accent: #8ebbe4;
  --color-accent-soft: #1c3348;
  --link-text-color: #9ec8ea;
  --input-background-fill: #121b25;
  --input-border-color: #2a3a4c;
  --button-primary-background-fill: #2f6fa8;
  --button-primary-background-fill-hover: #3b82c4;
  --button-primary-text-color: #f8fafc;
  --button-primary-border-color: #2f6fa8;
  --button-secondary-background-fill: #17212c;
  --button-secondary-text-color: #e7eef6;
  --button-secondary-border-color: #2a3a4c;
  background: #121b25;
  border-color: #2a3a4c;
  box-shadow: none;
}

body {
  background: #e7edf3;
}

.dark body,
body.dark {
  background: #0f1720;
}

.gradio-container h1 {
  margin: 0.4rem 0 0.2rem;
  color: #102033;
  font-size: 1.7rem;
  font-weight: 650;
  letter-spacing: -0.03em;
}

.dark .gradio-container h1 {
  color: #f3f7fb;
}

.gradio-container .chatbot {
  border: 1px solid var(--border-color-primary);
  border-radius: 12px;
  background: #f7f9fb;
}

.dark .gradio-container .chatbot {
  background: #101820;
}

.gradio-container .user {
  background: #1e4d7b;
  border-color: #1e4d7b;
  color: #f8fafc;
  box-shadow: none;
}

.gradio-container .message-wrap .user .prose.chatbot.md,
.gradio-container .user .prose p,
.gradio-container .user .prose li,
.gradio-container .user .prose strong {
  color: #f8fafc;
  opacity: 1;
}

.gradio-container .bot {
  background: #ffffff;
  border: 1px solid #d5dee8;
  box-shadow: none;
}

.dark .gradio-container .user {
  background: #245a8a;
  border-color: #245a8a;
}

.dark .gradio-container .bot {
  background: #17212c;
  border-color: #2a3a4c;
  color: #e7eef6;
}

.gradio-container .examples {
  gap: 0.65rem;
  padding-top: 0.25rem;
}

.gradio-container .example {
  border: 1px solid #d5dee8;
  border-radius: 10px;
  background: #f7f9fb;
  box-shadow: none;
  transform: none;
}

.gradio-container .example:hover {
  border-color: #1e4d7b;
  background: #eef4fa;
  transform: none;
}

.gradio-container .example-text {
  color: #1c2834;
  font-size: 0.95rem;
  line-height: 1.4;
}

.dark .gradio-container .example {
  background: #17212c;
  border-color: #2a3a4c;
}

.dark .gradio-container .example:hover {
  background: #1c3348;
  border-color: #7eb0dc;
}

.dark .gradio-container .example-text {
  color: #e7eef6;
}

.gradio-container .input-container {
  border: 1px solid #d5dee8;
  border-radius: 12px;
  background: #ffffff;
  box-shadow: none;
}

.gradio-container .input-container:focus-within {
  border-color: #1e4d7b;
  box-shadow: 0 0 0 3px rgba(30, 77, 123, 0.15);
}

.gradio-container .submit-button {
  border-radius: 10px;
}

.gradio-container .info {
  border-top: 1px solid #e6edf4;
  color: #7b8b9c;
  font-size: 0.75rem;
}

.dark .gradio-container .input-container {
  background: #121b25;
  border-color: #2a3a4c;
}

.dark .gradio-container .info {
  border-top-color: #2a3a4c;
  color: #9aabbd;
}

@media (max-width: 640px) {
  .gradio-container {
    margin: 0;
    border: none;
    border-radius: 0;
    max-width: none;
    box-shadow: none;
  }
}
"""
