from stopwords import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def world_cloud(str):

    if type(str) is list:
        str = " ".join(str)

    ignored = [ ".", ",", "!", "?", ";" ]
    for e in ignored:
        str = str.replace(e, "")

    str = str.split(" ");
    str[:] = [word.capitalize() for word in str]
    str = " ".join(str)

    wordcloud = WordCloud(
        width=1920,
        height=1080,
        stopwords=stopwords,
        max_words=500,
        background_color="white",
        colormap="Dark2",
        regexp=r"\w[\w-][\w'’-]+"
    )
    wordcloud = wordcloud.generate(str)
    plt.imshow(wordcloud, interpolation='bilinear', aspect='auto')
    plt.axis("off")
    plt.show()
