from openai import OpenAI
from url_scrape import fetch_url_content

openai =OpenAI()
system_prompt = """
You are a helpful assistant that analyzes the contents of a website,
and provides a summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""
def prompt_message(website):
    messages = [{"role": "system", "content": system_prompt},
               {"role": "user", "content": user_prompt_prefix + website}]
    return messages

def summarize(url):
    website = fetch_url_content(url)
    response = openai.chat.completions.create(
        model = "gpt-5-nano",
        messages = prompt_message(website)
    )
    return response.choices[0].message.content
