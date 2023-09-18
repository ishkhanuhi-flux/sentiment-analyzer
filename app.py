import streamlit as st
from modules import fetch_google_alerts
from modules import analyze_sentiment
import matplotlib.pyplot as plt

BRAND_RSS_URLS = {
    'Samsung': 'https://www.google.com/alerts/feeds/10432254465216124981/8551231511754676176',
    'Coca Cola': 'https://www.google.com/alerts/feeds/10432254465216124981/16715693543102106788',
    'Pepsi': 'https://www.google.com/alerts/feeds/10432254465216124981/3763137046895005697',
    'Apple': 'https://www.google.com/alerts/feeds/10432254465216124981/14723713437188394551',
    'Adidas': 'https://www.google.com/alerts/feeds/10432254465216124981/2237199936254488151',
    'Nike': 'https://www.google.com/alerts/feeds/10432254465216124981/14590602689292939912'
}


def main():
    st.title('Google Alerts Sentiment Analysis')

    # Dropdown for brand selection
    selected_brand = st.selectbox('Select a brand:', list(BRAND_RSS_URLS.keys()))

    if st.button('Analyze'):
        mentions = fetch_google_alerts(BRAND_RSS_URLS[selected_brand])
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        for mention in mentions:
            polarity = analyze_sentiment(mention['summary'])
            if polarity > 0:
                sentiment = 'Positive'
                positive_count += 1
            elif polarity < 0:
                sentiment = 'Negative'
                negative_count += 1
            else:
                sentiment = 'Neutral'
                neutral_count += 1
            st.write(f"Title: {mention['title']}")
            st.write(f"Link: {mention['link']}")
            st.write(f"Sentiment: {sentiment}")
            st.write('-' * 50)

        # Display bar chart
        labels = ['Positive', 'Negative', 'Neutral']
        values = [positive_count, negative_count, neutral_count]
        plt.bar(labels, values, color=['green', 'red', 'blue'])
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.title(f'Sentiment Analysis for {selected_brand}')
        st.pyplot(plt)


if __name__ == "__main__":
    main()
