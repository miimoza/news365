from wordcloud import WordCloud
import matplotlib.pyplot as plt

def world_cloud(str):

    if type(str) is list:
        str = " ".join(str)

    determinant = ["le","la","un","une","de","du","des","en","dans","pour","par"]
    for d in determinant:
        str.replace(d,"")


    print("Generating world cloud for:", str)
    wordcloud = WordCloud().generate(str)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
