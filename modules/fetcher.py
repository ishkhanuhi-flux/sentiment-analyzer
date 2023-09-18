import feedparser


def fetch_google_alerts(rss_url):
    feed = feedparser.parse(rss_url)
    mentions = []
    for entry in feed.entries:
        mention_data = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        }
        mentions.append(mention_data)
    return mentions
