from nandini.models import liner_model 
from nandini.sequence import text
a = liner_model.LinearRegression()
b = text.Preprocessing()
c = 'Sharulatha is an Canadian girl , she doesnt know swimming , she doesnt have brain too'
print(b.text_lemmatize(b.text_remove_stopwords(b.text_normalize(c))))