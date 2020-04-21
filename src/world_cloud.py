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

    blacklist = [
        "il", "elle", "on",
        "le",  "la", "un", "une", "du", "de", "les", "des",
        "ce", "cet", "cette", "ces", "mais", "ou", "et", "donc",
        "que", "quoi", "qui", "où",
        "en", "dans", "pour", "par", "à",
        "est", "a", "fait"
    ]

    str = str.replace("-", "_")

    wordcloud = WordCloud(
        width=1920,
        height=1080,
        stopwords=blacklist,
        max_words=500,
        background_color="white",
        colormap="Dark2"
    )
    wordcloud = wordcloud.generate(str)
    plt.imshow(wordcloud, interpolation='bilinear', aspect='auto')
    plt.axis("off")
    plt.show()
