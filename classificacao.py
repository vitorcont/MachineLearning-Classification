from sklearn.naive_bayes import MultinomialNB
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

train_x = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]
train_y = [1, 1, 1, 0, 0, 0]
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
test_x=[misterioso1,misterioso2,misterioso3]
test_y=[0,1,0]

modelo = MultinomialNB()
modelo.fit(train_x,train_y)
resultado=modelo.predict(test_x)
print(resultado)
print(resultado-test_y)
diferenca=resultado-test_y

acertos=[d for d in diferenca if d==0]
total_acertos=len(acertos)
total_elementos=len(test_x)
taxa_acerto= total_acertos/total_elementos *100

print(taxa_acerto)