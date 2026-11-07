# Promptfoo prompt evaluation

## Quick start

1. Copy `.env.example` to `.env` and fill in the keys you use
   (Google, Groq, OpenRouter, Cloudflare). Install the pinned promptfoo version:

```bash
npm install
```

2. Edit `promptfooconfig.yaml` to customize prompts, providers, and test cases.

3. Run the evaluation:

```bash
npm run eval          # promptfooconfig.yaml (AI triage)
npm run eval:smoke    # API connection check
npm run eval:chatbot  # shop chatbot tests
```

4. View results in your browser:

```bash
npm run view
```

## Learn more

- Configuration guide: https://promptfoo.dev/docs/configuration/guide
- All providers: https://promptfoo.dev/docs/providers
- Assertions & metrics: https://promptfoo.dev/docs/configuration/expected-outputs
- Examples: https://github.com/promptfoo/promptfoo/tree/main/examples
