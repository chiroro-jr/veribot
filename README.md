# Veribot
A deep neural network application that determines the credibility of a social media
post given its `source` for example Facebook or Instagram and it's `content`. You
can view the architecture of the model in [this image.](./models/classifier.png)

## Reference links
- [veribot.streamlit.com](https://veribot.streamlit.app/) - the deployed app on Streamlit
- [Google Colab notebook](https://colab.research.google.com/drive/1HUYQWTKNbrPVC56BbzRlkxeOvZFl07zk?usp=sharing) - 
used to scrape the data and train the model.
- [Youtube video](https://youtube.com) - explanation of how the app works 

## Tools used to build the application
- Python
- Pipenv
- Streamlit
- Tensorflow and keras
- Numpy
- NLTK
- SKLearn
> For in depth explanations of these tools read the contents of [tools.md](tools.md)

## Running the app locally on your machine
1. Make sure you have Python installed, specifically Python version `3.11` as it is the one used in this project.
You can check if python is installed using `python --version`. This will display the version of Python installed.
For instructions on how to install
Python, visit [this website](https://realpython.com/installing-python/).
2. Make sure you have Pipenv install. Pipenv is the package manager and virtual environment manager
used in this project. You can check if Pipenv is installed using `pipenv --version`. This will display
the version of Pipenv install. For instructions on how to install Pipenv, visit [this website](https://www.infoworld.com/article/3561758/how-to-manage-python-projects-with-pipenv.html).
3. Clone this repository by running the command below:
```shell
git clone https://github.com/chiroro-jr/veribot.git
```
4. Change into the project folder using the command `cd veribot`
5. Run `pipenv install` to create a virtual environment and install project dependencies
6. Run `pipenv shell` to activate the newly created virtual environment
7. Run `streamlit run app.py` to start the application. The app will be opened in your browser.