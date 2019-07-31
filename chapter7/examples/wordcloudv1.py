import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud(background_color="white")
w.generate(txt)
w.to_file("pywcloud.png")
