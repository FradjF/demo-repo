from modules.env_setup import env_load
from modules import prompt_setup as p_s
from rich.console import Console
from rich.markdown import Markdown
# from IPython.display import Markdown, display

console = Console()

def display_summary(summary):
    md = Markdown(summary)
    console.print(md)

env_load()
url = input("Enter the URL: ")
url_summary = p_s.summarize(url)
display_summary(url_summary)