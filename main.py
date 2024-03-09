import feedparser

def safe_get(entry, field):
    """
    Return the value if field exists, otherwise return "N/A".
    """
    try:
        return getattr(entry, field)
    except AttributeError:
        return "N/A"
    
def parse_rss_feed(feed_url):
    # Parse RSS feed
    feed = feedparser.parse(feed_url)

    # Check if feed is parsed successfully
    if feed.bozo == 0:
        print("Feed title:", feed.feed.title)
        print("Feed URL:", feed.feed.link)

        for entry in feed.entries:
            print("\nTitle:", entry.title)
            print("Published date:", safe_get(entry, 'published'))
            print("Summary:", safe_get(entry, 'summary'))
            print("Link:", safe_get(entry, 'link'))
    else:
        print("Error parsing feed:", feed.bozo_exception)

if __name__ == "__main__":
    """
    Example usage
    """
    rss_feed_url = "https://feeds.megaphone.fm/newheights"
    parse_rss_feed(rss_feed_url)