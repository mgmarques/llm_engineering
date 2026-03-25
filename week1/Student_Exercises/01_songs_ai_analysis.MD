# Radio Calico - Song Details Summarizer Prototype

## Overview

This prototype is a **music information assistant** that takes song details from Radio Calico (a music streaming/radio service) and generates rich, formatted summaries using a local LLM (Llama 3.2) via Ollama.

## How It Works

### Architecture

```
Radio Calico song metadata → Prompt construction → Ollama (Llama 3.2) → Markdown response → Jupyter display
```

1. **Input**: Song details string containing track name, artist, album, and album cover URL (as broadcast by Radio Calico)
2. **LLM Backend**: Uses Ollama running locally (`localhost:11434`) with OpenAI-compatible API via the `openai` Python SDK
3. **Output**: Rendered Markdown in a Jupyter notebook

### Components

| Component | Purpose |
|---|---|
| `system_prompt` | Instructs the LLM to act as a genre-aware music enthusiast. Directs it to extract metadata, look up facts, provide lyrics, album tracklists, and related products. Strips the "Radio Calico" source attribution. |
| `user_prompt` | The query template — asks for song meaning, lyrics, facts, album tracklist table, related products, and a funny multilingual closing note. |
| `messages_for(song_details, language)` | Builds the chat message array, appending the target language to the system prompt and song details to the user prompt. |
| `summarize(song_details, language)` | Sends the messages to Ollama's `llama3.2` model and returns the raw text response. |
| `display_summary(song_details, language)` | Orchestrates the call and renders the result as Markdown in Jupyter. |

### Configuration

- **LLM**: Llama 3.2 via Ollama (local, no API key needed — `api_key="anything"` is a placeholder)
- **Language**: Configurable per call — supports `"English"`, `"Portuguese"`, `"Spanish"`, etc.
- **Model swap**: Change the `model` parameter in `summarize()` to use any Ollama-hosted model

### Example Input

```
Listening to "Under the Milky Way" by The Church (Starfish (Deluxe Edition)) on Radio Calico!
Album cover: https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/.../300x300bb.jpg
```

### Expected Output

A Markdown document containing:
- Song description/meaning
- Lyrics
- Interesting facts about the song, album, and artists
- Album tracklist table with durations
- Related products summary (if applicable)
- A humorous closing quote in a rotating language

## Limitations & Notes

- **Lyrics accuracy**: LLMs hallucinate lyrics — the model generates from training data, not a lyrics database. For production, integrate a lyrics API (e.g., Musixmatch, Genius).
- **Album cover analysis**: The system prompt mentions checking the album cover URL/image metadata, but the current implementation passes it as text only — the model cannot actually fetch or view the image. A multimodal model or a separate image-fetch step would be needed.
- **Local-only**: Requires Ollama running on the same machine. For production deployment, consider a hosted LLM or containerized Ollama.
- **No error handling**: Network failures, Ollama downtime, or malformed input will raise unhandled exceptions.

## Suggested Improvements for Production (Radio Calico)

1. **Add error handling** around the Ollama API call
2. **Integrate a real lyrics API** instead of relying on LLM-generated lyrics
3. **Use a multimodal model** (or fetch the album cover separately) if image analysis is needed
4. **Cache responses** — the same song doesn't need to be summarized twice
5. **Parameterize the model name** instead of hardcoding `"llama3.2"`
6. **Structured output** — consider returning JSON for programmatic consumption alongside Markdown for display
