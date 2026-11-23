# Illusionator

**Illusions for machines: do vision models fall for the same optical illusions we do?**

A Columbia AI Club project.

## The question

Humans reliably misjudge certain images: equal lines look unequal (Müller-Lyer), identical grays look different (checker shadow), static patterns seem to move, and two equal circles look different sizes depending on what surrounds them (Ebbinghaus). These illusions are not bugs in human vision. They are side effects of the shortcuts our visual system takes to make sense of the world.

Vision models learn their own shortcuts from data. Illusionator asks whether they learned ours:

- Do vision models and vision-language models make the same mistakes on classic illusions that people do?
- When they do, is that because they perceive the illusion, or because they recognize a famous image and remember the "right" answer?
- When an illusion is changed so that the textbook answer no longer holds, do models follow the pixels or the memory?
- Do bigger or newer models become more human-like, or less?

## Approach

1. **Generate illusions as code.** Every stimulus is drawn by a parameterized generator, so we control the ground truth exactly (line lengths, gray values, circle sizes) and can produce many variants, including ones that never appear on the internet.
2. **Ask models measurable questions.** "Which line is longer?" or "Are these two squares the same color?" on both the illusion and a control image with the context removed.
3. **Compare against human baselines** from the perception literature, and from club members where we can collect it.
4. **Separate perception from memorization** with altered illusions, where the true answer differs from the famous one.

## Status

Just getting started. Structure, illusion set, and model list are still being decided.

## Development

### Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 for you if needed).

```bash
git clone https://github.com/Eladhirsh/Illusionator.git
cd Illusionator
uv sync
uv run pytest
```

Code lives in `src/illusionator/`, tests in `tests/`. Add a dependency with `uv add <package>` (or `uv add --dev <package>` for test-only tools) and commit `uv.lock`. CI runs `pytest` on every pull request.

### Workflow

This project is built test-first:

1. Write a failing test for the behavior.
2. Run it and watch it fail.
3. Write the smallest code that makes it pass, then refactor.

We use [gstack](https://github.com/garrytan/gstack) skills for the workflow (`/plan-eng-review` before building a feature, `/verify` to run checks, `/review` before merging, `/ship` to open a PR). Review findings should come with a failing test or a reproduction.

## Contributing

Columbia AI Club members are welcome. Open an issue or a pull request, and keep changes small and tested.
