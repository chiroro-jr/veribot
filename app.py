import streamlit as st
from keras.saving import load_model
from pickle import load
from helpers import get_prediction, generate_credibility_message

# load the classifier
classifier = load_model("./models/classifier.h5")

# load the tokenizer
tokenizer = load(open('./models/tokenizer.pkl', 'rb'))

# load the label_encoder
label_encoder = load(open('./models/label_encoder.pkl', 'rb'))

"""
# Veribot
A deep neural network application that determines the credibility of a social media
post given its `source` for example Facebook or Instagram and it's `content`.
"""
st.divider()
"""
### Get a classification
"""
source = st.text_input("Post source", placeholder="For example: Facebook, Instagram, Twitter")
content = st.text_area("Post content", placeholder="I said something of Facebook the other day. It may or may not be "
                                                   "credible.")

if st.button("Classify", type="secondary"):
    if not (len(source) == 0 or len(content) == 0):
        """
        ### Classification Result
        """
        result = get_prediction(source, content, classifier, tokenizer, label_encoder)
        result_message = generate_credibility_message(result)
        st.write(result_message)
    else:
        """
        ### Input Error
        You need to provide the both `source` and `content` to get a prediction.
        """


else:
    """
    ### Classification Result
    No result. Enter the `source` and `content` and then press **Classify** to get a result.  
    """
st.divider()

"""
## Reference Links
- [Github repository for project](https://github.com/chiroro-jr/veribot) - This contains all the code for this app (jupyter notebooks, 
datasets, saved models and so on.)
- [Google Colab notebook](https://colab.research.google.com/drive/1HUYQWTKNbrPVC56BbzRlkxeOvZFl07zk?usp=sharing) - 
used to scrape the data and train the model. 
"""