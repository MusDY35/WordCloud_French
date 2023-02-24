import os
import nltk
from nltk.corpus import stopwords
from os import path
from wordcloud import WordCloud

nltk.download("stopwords")
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.

# text = open(path.join(d, 'frenchweek.txt')).read()
text = "Dans tes yeux, je vois la lumière Qui brille si fort, elle me rend fière De t'avoir à mes côtés, mon amour Je t'aime tellement, mon cher Tu es mon étoile, mon univers Sans toi, je suis perdue dans l'obscurité Je t'aime tellement, pour l'éternité Ton sourire illumine mes journées Ta voix douce me fait rêver Je suis folle de toi, mon amour Tu es ma raison de vivre chaque jour Je t'aime tellement, mon cher Tu es mon étoile, mon univers Sans toi, je suis perdue dans l'obscurité Je t'aime tellement, pour l'éternité Je ne peux pas imaginer la vie sans toi Tu es mon tout, ma raison de vivre Je te promets mon amour pour toujours Je t'aime tellement, mon cher amour Je t'aime tellement, mon cher Tu es mon étoile, mon univers Sans toi, je suis perdue dans l'obscurité Je t'aime tellement, pour l'éternité.Je veux vivre pleinement,Profiter de chaque moment,Respirer l'air frais de la vie,Et danser sous le ciel de minuit.Je ne veux pas rester coincéDans une vie qui n'est pas complète,Je veux explorer le monde entier,Et découvrir de nouvelles choses chaque jour.Je veux sentir le vent sur mon visage,Et écouter les sons de la nature,Je veux m'immerger dans les cultures,Et apprendre de nouvelles langues.Je sais que la vie peut être difficile,Mais je veux la vivre avec passion,Je veux savourer chaque instant,Et vivre pleinement sans hésitation.Je veux rencontrer des gens de tous horizons,Et partager mes histoires et mes passions,Je veux créer des souvenirs inoubliables,Et me rappeler toujours de ce que j'ai vécu.Je veux rire, je veux chanter,Je veux danser sous la pluie,Je veux aimer et être aimé,Et vivre pleinement ma vie.Je veux vivre pleinement,Profiter de chaque moment,Respirer l'air frais de la vie,Et danser sous le ciel de minuit."

stopwords = stopwords.words('french')

#creating a proper string (convertion from unicode to str) required for the wordcloud method
set_of_srt_stopwords = set()
for word in stopwords:
    word_str= word.encode("utf-8")
set_of_srt_stopwords.add(word_str)

#adding 2 new stopwords to my set of stopwords strings
set_of_srt_stopwords.add("Bélier")
set_of_srt_stopwords.add("samedi")

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

# lower max_font_size
wordcloud = WordCloud(
    width=800,
    height=1600,
    colormap="GnBu",
    stopwords=set_of_srt_stopwords
).generate(text)
plt.figure(figsize=(20,40),facecolor='k')
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')