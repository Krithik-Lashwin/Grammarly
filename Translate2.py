from textblob import TextBlob
text = TextBlob('I love to learn about dinosaurs and Science')
print(text.translate(from_lang='en', to='fr'))
print(text.translate(from_lang='en', to='ar'))
print(text.translate(from_lang='en', to='ja'))