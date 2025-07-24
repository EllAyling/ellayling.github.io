import feedparser
import yaml
from bs4 import BeautifulSoup

RSS_URL = "https://medium.com/feed/@EllAyling"

feed = feedparser.parse(RSS_URL)

posts = []
for entry in feed.entries:
    # Get HTML content from summary or content
    html_content = entry.get('summary', '') or entry.get('content', [{}])[0].get('value', '')
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract first image if any
    img_tag = soup.find('img')
    thumbnail = img_tag['src'] if img_tag else "/img/icon.png"  # default image

    # Extract text, remove extra whitespace and truncate
    text = soup.get_text(separator=' ', strip=True)
    excerpt = (text[:150] + '...') if len(text) > 150 else text

    posts.append({
        "title": entry.title,
        "url": entry.link,
        "thumbnail": thumbnail,
        "date": entry.published,
        "excerpt": excerpt
    })

with open("_data/medium_posts.yml", "w") as f:
    yaml.dump(posts, f, default_flow_style=False)