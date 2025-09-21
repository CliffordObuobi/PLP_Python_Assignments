import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import collections
import re
from io import StringIO
import base64
import os

# Set a clean style for all plots
sns.set_style('whitegrid')

# --- Part 1: Data Loading & Exploration ---

@st.cache_data
def load_and_prepare_data():
    """
    Loads and cleans the CORD-19 metadata.csv file.
    This function is cached to prevent reloading the data on every interaction.
    """
    try:
        # Check if the file exists in the current directory
        file_path = 'metadata.csv'
        if not os.path.exists(file_path):
            st.error(f"Error: The file '{file_path}' was not found.")
            st.info("Please make sure 'metadata.csv' is in the same directory as this Python script.")
            return None

        st.write("### Part 1: Data Loading and Basic Exploration")
        st.write("---")

        # Load the dataset
        df = pd.read_csv(file_path)
        
        # Check the DataFrame dimensions
        st.subheader("DataFrame Dimensions")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        
        # Display the first few rows
        st.subheader("First 5 Rows")
        st.dataframe(df.head())
        
        # Check data types and missing values
        st.subheader("DataFrame Structure")
        buffer = StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        
        st.subheader("Missing Values")
        st.write("Count of missing values per column:")
        st.table(df.isnull().sum())
        
        # --- Part 2: Data Cleaning and Preparation ---
        st.write("### Part 2: Data Cleaning and Preparation")
        st.write("---")
        
        # Handle missing data: drop rows with missing abstracts
        df_cleaned = df.dropna(subset=['abstract']).copy()
        st.write("Dropping rows with missing abstracts...")
        st.write(f"New number of rows: {df_cleaned.shape[0]}")
        
        # Prepare data for analysis
        df_cleaned['publish_year'] = pd.to_datetime(df_cleaned['publish_time']).dt.year
        
        # Create a new column for abstract word count
        df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(x.split()) if pd.notnull(x) else 0)
        st.write("Created `publish_year` and `abstract_word_count` columns.")
        st.dataframe(df_cleaned.head())
        
        return df_cleaned

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.write("Please check your file and try again.")
        return None

# --- Main Streamlit App Layout ---

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("CORD-19 Data Explorer")
    st.write("A simple interactive exploration of COVID-19 research papers.")
    st.write("---")
    
    # Load and prepare the data (cached for performance)
    df = load_and_prepare_data()

    if df is not None:
        # --- Part 3: Data Analysis and Visualization ---
        st.write("### Part 3: Data Analysis and Visualization")
        st.write("---")
        
        st.subheader("Publications Over Time")
        # Group by year and count publications
        yearly_counts = df['publish_year'].value_counts().sort_index()
        
        # Plot number of publications over time
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', ax=ax)
        plt.title('Number of Publications by Year', fontsize=16)
        plt.xlabel('Publication Year', fontsize=12)
        plt.ylabel('Number of Papers', fontsize=12)
        plt.xticks(yearly_counts.index)
        st.pyplot(fig)
        
        st.subheader("Top Publishing Journals")
        # Identify top journals
        top_journals = df['journal'].value_counts().head(5)
        
        # Create a bar chart of top journals
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax)
        plt.title('Top 5 Publishing Journals', fontsize=16)
        plt.xlabel('Number of Papers', fontsize=12)
        plt.ylabel('Journal', fontsize=12)
        st.pyplot(fig)
        
        st.subheader("Word Cloud of Paper Titles")
        # Combine all titles into a single string
        all_titles = " ".join(title for title in df['title'] if pd.notnull(title))
        
        # Generate a word cloud image
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
        
        # Display the generated image
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        st.subheader("Distribution of Abstract Word Count")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(df['abstract_word_count'], bins=20, kde=True, color='skyblue', ax=ax)
        plt.title('Distribution of Abstract Word Counts', fontsize=16)
        plt.xlabel('Word Count', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        st.pyplot(fig)
        
        st.subheader("Most Frequent Words in Titles")
        # Simple word frequency analysis
        all_words = " ".join(df['title'].dropna()).lower()
        # Remove punctuation
        all_words = re.sub(r'[^\w\s]', '', all_words)
        words = all_words.split()
        word_counts = collections.Counter(words)
        
        # Exclude common stop words for better results
        stop_words = set(['a', 'an', 'the', 'of', 'in', 'and', 'for', 'on', 'with', 'is', 'from'])
        filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stop_words}
        
        st.write("Top 10 most frequent words in paper titles:")
        st.json(dict(collections.Counter(filtered_word_counts).most_common(10)))


if __name__ == "__main__":
    main()
