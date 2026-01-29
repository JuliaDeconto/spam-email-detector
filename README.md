## Spam Email Detector

Projeto de **Machine Learning** desenvolvido em Python para classificação de mensagens de e-mail como **Spam** ou **Não Spam**, utilizando técnicas básicas de **Processamento de Linguagem Natural (NLP)**.


## Objetivo

Desenvolver um modelo de Machine Learning capaz de identificar mensagens de spam a partir do conteúdo textual, aplicando conceitos fundamentais de aprendizado supervisionado.


## Tecnologias Utilizadas

- Python  
- Pandas  
- Scikit-learn  
- NLTK  


## Dataset

O dataset utilizado contém mensagens de e-mail escritas em **português**, rotuladas originalmente como `spam` e `ham`.

Antes do treinamento, foram realizadas as seguintes etapas:
- Remoção de mensagens duplicadas
- Renomeação das classes:
  - `ham` → **Não Spam**
  - `spam` → **Spam**

Os dados utilizados para treinamento e teste deste modelo foram obtidos do seguinte repositório:

- Repositório original: [wesleyc00/spam-detector](https://github.com/wesleyc00/spam-detector)
- Dataset: [dataset_pt_br](https://github.com/wesleyc00/spam-detector/tree/main/dataset_pt_br)
- Descrição: Conjunto de mensagens em português para classificação de spam e não spam

Créditos do dataset: @wesleyc00 (GitHub)


## Pré-processamento dos Dados

As seguintes etapas de pré-processamento foram aplicadas:

- Remoção de dados duplicados  
- Vetorização do texto utilizando **CountVectorizer**
- Remoção de **stopwords em português** utilizando a biblioteca NLTK  


## Modelo de Machine Learning

O modelo utilizado foi o **Multinomial Naive Bayes**, amplamente empregado em tarefas de classificação de texto.

Os dados foram divididos da seguinte forma:
- 80% para treinamento  
- 20% para teste  


## Avaliação do Modelo

O desempenho do modelo foi avaliado utilizando a métrica de **acurácia**.

O modelo apresentou uma acurácia aproximada de **90%**, podendo variar conforme a divisão aleatória dos dados entre treino e teste.


## Previsão em Tempo Real

O projeto permite realizar previsões para novas mensagens.

Exemplo de mensagem testada:
"Oferta especial de lançamento"

Resultado esperado:
- Spam

Resultado obtido pelo modelo:
- Spam


## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/JuliaDeconto/spam-email-detector.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o script:
```bash
python SpamDetection.py
```

-----

As dependências do projeto estão listadas no arquivo `requirements.txt`.

-----

## Observações

A acurácia pode variar a cada execução devido à divisão aleatória dos dados entre treino e teste.

-----

Este projeto foi desenvolvido com fins educacionais, visando o aprendizado prático de técnicas de Machine Learning e NLP.