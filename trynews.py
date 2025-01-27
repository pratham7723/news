import streamlit as st
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import pipeline
import requests

# Load pre-trained model and tokenizer from Hugging Face
model_name = 'roberta-base-openai-detector'
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaForSequenceClassification.from_pretrained(model_name)

# Load a pipeline for fake news classification
nlp = pipeline('text-classification', model=model, tokenizer=tokenizer)

# Function to fetch news articles using NewsAPI
def fetch_news_articles(query):
    api_key = '2dc66a93be62487e8ea8f2031911b5fa'  # Your NewsAPI key
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&language=en'
    
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        st.error(f"Error fetching news: {response.status_code}")
        return []

# Streamlit Interface
def main():
    st.set_page_config(page_title="Fake News Detection", page_icon="📰", layout="centered")

    # Add a custom header and description
    st.title("Fake News Detection App")
    st.markdown("Welcome to the **Fake News Detection App**. Enter a news article or headline below to check if it's real or fake.")
    
    # Input text area for the user to input news
    news_input = st.text_area("Enter the news article or headline:")

    label = None
    confidence = None

    # Add the Check News button
    if st.button("Check News"):
        if news_input:
            # Use the NLP model to classify the news text
            result = nlp(news_input)
            label = result[0]['label']
            confidence = result[0]['score']

            # Fetch related articles from well-known publishers
            articles = fetch_news_articles(news_input)

            # Display the classification result
            st.write(f"**Classification:** {label}")
            st.write(f"**Confidence Score:** {confidence:.4f}")

            # Set color for the marquee based on classification
            if label == "Fake":
                color = "red"
                text = "FAKE NEWS"
                
            else:
                color = "green"
                text = "REAL NEWS"
                

            # Create a marquee for the classification result
            st.markdown(f"""
                <div style="background-color:{color}; color:white; padding:5px; border-radius:5px; width:100%;">
                    <marquee behavior="scroll" direction="left">{text}</marquee>
                </div>
            """, unsafe_allow_html=True)

            # Show related articles only if articles are available
            if articles:
                st.subheader("Related Articles from Trusted Sources:")
                for article in articles[:3]:  # Show top 3 related articles
                    # Ensure that the article has necessary data before displaying
                    title = article.get('title', 'No title available')
                    source = article.get('source', {}).get('name', 'Unknown source')
                    url = article.get('url', '#')

                    st.write(f"**Source:** {source}")
                    st.write(f"**Title:** {title}")
                    st.write(f"**URL:** [Read More]({url})")
            else:
                st.write("No related articles found.")
        else:
            st.write("Please enter some news text to classify.")

    # Optional: Display the news history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Save the current news to history only if label and confidence are valid
    if news_input and label and confidence is not None:
        st.session_state['history'].append((news_input, label, confidence))

    # Display history of previously checked news
    if st.button("Show History"):
        if st.session_state['history']:
            st.subheader("News History:")
            for i, (news, label, score) in enumerate(st.session_state['history']):
                st.write(f"{i + 1}. **News:** {news}")
                st.write(f"   **Classification:** {label}, **Confidence:** {score:.4f}")
        else:
            st.write("No history available.")

if __name__ == "__main__":
    main()
