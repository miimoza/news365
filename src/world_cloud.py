from stopwords import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def world_cloud(str, mask):

    if type(str) is list:
        str = " ".join(str)

    ignored = [ ".", ",", "!", "?", ";" ]
    for e in ignored:
        str = str.replace(e, "")

    str = str.split(" ");
    str[:] = [word.title() for word in str]
    str = " ".join(str)
    str = uncap_cities(str)

    wordcloud = WordCloud(
        width=1000,
        height=1000,
        stopwords=stopwords,
        max_words=100,
        mask=mask,
        contour_width=1,
        contour_color="silver",
        background_color="white",
        colormap="Dark2",
        regexp=r"\w[\w-][\w'’-]+"
    )

    wordcloud = wordcloud.generate(str)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("output.png",
        format="png",
        dpi=250,
        bbox_inches='tight'
    )
    #plt.show()
