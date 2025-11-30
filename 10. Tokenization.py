#experiment 10

import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure required NLTK resources are available
for resource in ['punkt', 'punkt_tab', 'stopwords']:
    try:
        nltk.data.find(f'tokenizers/{resource}' if 'punkt' in resource else f'corpora/{resource}')
    except LookupError:
        nltk.download(resource)

# Sample text
text = """Perform tokenization, stemming, and stop-word removal on sample text."""

# 1. Tokenization (keep hyphenated words as single tokens)
tokenizer = RegexpTokenizer(r'\b\w+(?:-\w+)?\b')  # Matches words and hyphenated words
tokens = tokenizer.tokenize(text)

# 2. Stop-word Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# 3. Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Output results
print("Original Tokens:", tokens)
print("Filtered Tokens (no stop-words):", filtered_tokens)
print("Stemmed Tokens:", stemmed_tokens)