#LangChain Hands on work
This is a simple example of using LangChain with the OpenRouter API to generate jokes using the Gemini 2.5 Pro model.

## Setup

1. Install the required packages:
   ```bash
   pip install langchain-openrouter langchain-core python-dotenv
   ```
2. Create a `.env` file in the project root and add your OpenRouter API key:
   ```plaintext
    OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

## Usage

Run the `main.py` script:

```bash
python main.py
```

This will generate and print a joke about beets using the Gemini 2.5 Pro model.

You can change the topic of the joke by modifying the input in the `chain.invoke` method in `main.py`:

```python
result = chain.invoke({"topic": "your_topic_here"})
print("Gemini 2.5 Joke:", result)
```

If you want to give a topic as an input in CLI then

```python
topic = input("Enter a topic for the joke: ")
result = chain.invoke({"topic": topic})
```
