"""Scrap StatBlocks from https://wfrp1e.fandom.com/wiki/Category:Bestiary and save to file."""

import json

from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
    },
    "verbose": True,
    "headless": False,
}

prompt = "Extract the statblock(s) from the page. WFRP1e uses the stats `M`, `WS`, `BS`, ... `Fel`"

source = "https://wfrp1e.fandom.com/wiki/Amoeba"

beast_scraper = SmartScraperGraph(
    prompt = prompt,
    source = source,
    config = graph_config,
)


if __name__ == "__main__":
    stats = beast_scraper.run()

    print(json.dumps(stats, indent=4))  # noqa: T201
