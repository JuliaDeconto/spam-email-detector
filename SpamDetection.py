import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')

stopwords_pt = stopwords.words('portuguese')

data = pd.read_csv(r"C:\Users\julia\OneDrive\Área de Trabalho\Spam Email Detector\spam.csv")

data.drop_duplicates(inplace=True)
data['Categoria'] = data['Categoria'].replace(['ham','spam'],['Não Spam','Spam'])

mens = data ['Mensagem']
cat = data ['Categoria']

(mens_train,mens_test,cat_train,cat_test) = train_test_split(mens, cat, test_size=0.2)

cv =CountVectorizer(stop_words=stopwords_pt)
features = cv.fit_transform(mens_train)

#criando Modelo

model = MultinomialNB()
model.fit(features, cat_train)

#testando Modelo

features_test = cv.transform(mens_test)
print(model.score(features_test, cat_test))

#prevendo Dados em Tempo Real

mensagem = cv.transform(['Oferta especial de lançamento'])
result = model.predict(mensagem)
print(result)