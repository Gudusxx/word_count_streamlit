import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(words_and_frequencies, dark_mode=False):
    wordcloud = WordCloud(width=800, height=400, background_color="black" if dark_mode else "white").generate_from_frequencies(words_and_frequencies)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    
    # Pass the figure explicitly to st.pyplot()
    st.pyplot(fig)

def main():
    st.title("Word Cloud Generator")


    st.subheader("Enter Words and Frequencies (separated by commas)")
    input_text = st.text_area("Example: apple, banana, cherry:2, grape:3", height=100)
    words_and_frequencies = {}

    if input_text:
        word_freq_pairs = [pair.strip() for pair in input_text.split(',')]

        for pair in word_freq_pairs:
            parts = pair.split(':')
            word = parts[0].strip()
            frequency = int(parts[1].strip()) if len(parts) > 1 else 1
            words_and_frequencies[word] = frequency

    frequency = st.slider("Select Frequency", min_value=1, max_value=10, value=1)

    if not words_and_frequencies:
        st.warning("Please enter words and frequencies.")
    else:
        # Apply the selected frequency to all words
        words_and_frequencies = {word: frequency * frequency_value for word, frequency_value in words_and_frequencies.items()}

        # Display the button
        if st.button("Generate Word Cloud"):
            # Generate the word cloud when the button is clicked
            generate_word_cloud(words_and_frequencies, dark_mode)

if __name__ == "__main__":
    main()
