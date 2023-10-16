# required libraries
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from keras.preprocessing.sequence import pad_sequences

# download NLTK stopwords
nltk.download('stopwords')
nltk.download('wordnet')


# define a function to clean the text
def clean_doc(doc):
    # Remove HTML tags using regex
    doc = re.sub(r'<[^>]+>', '', doc)

    # Convert text to lowercase
    doc = doc.lower()

    # Split into tokens by white space
    tokens = doc.split()

    # Prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))

    # Remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]

    # Remove non-alphabetic tokens
    tokens = [word for word in tokens if word.isalpha()]

    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Perform lemmatization on each word
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]

    # Filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]

    # Join the tokens back into a single string
    cleaned_text = ' '.join(tokens)

    return cleaned_text


def generate_credibility_message(result_dict):
    probability = result_dict.get('probability', 0.0)
    classification = result_dict.get('classification', '')

    inverted_probability = 1 - probability

    if classification == 'credible':
        message = f"Based on the analysis, the probability that the source is credible is approximately `{inverted_probability * 100:.2f}%`. This points to an indication of the source being **credible**. However, you still need to check multiple sources and make sure you are getting the correct information."
    elif classification == 'incredible':
        message = f"Based on the analysis, the probability that the source is credible is approximately `{inverted_probability * 100:.2f}%`. This points to an indication of the source **not being credible**. Do some research and check your sources to make sure you are getting the correct information."
    else:
        message = "Invalid classification. Please provide 'credible' or 'not credible'."

    return message


# create a function to make the prediction
def get_prediction(source, content, classifier, tokenizer, label_encoder):
    post = f'{source} {content}'

    post = clean_doc(post)

    post = [post]

    post = tokenizer.texts_to_sequences(post)

    max_seq_length = 45
    post = pad_sequences(post, maxlen=max_seq_length, padding="post")

    result = dict()

    result["probability"] = classifier.predict(post, verbose=0)[0][0]

    if result["probability"] >= 0.5:
        result["classification"] = label_encoder.inverse_transform([1])[0]
    else:
        result["classification"] = label_encoder.inverse_transform([0])[0]

    return result
