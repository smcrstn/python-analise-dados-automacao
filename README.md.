Detecção de Fraudes em Cartões de Crédito com Machine Learning

Objetivo

Projeto desenvolvido durante os estudos de Python e Machine Learning, com foco na identificação de transações potencialmente fraudulentas e na avaliação de modelos de classificação em um cenário de classes desbalanceadas.

Tecnologias utilizadas

- Python
- Google Colab
- Pandas e NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- SHAP
- imbalanced-learn (SMOTE)

Etapas do projeto

1. Preparação dos dados e transformação logarítmica da variável `Amount`.
2. Separação dos dados em conjuntos de treinamento e teste, com estratificação.
3. Treinamento de modelos de Regressão Logística, Random Forest e XGBoost.
4. Avaliação utilizando precision, recall, F1-score e ROC-AUC.
5. Análise das curvas ROC e Precision-Recall.
6. Experimentação com limiar de classificação, undersampling e SMOTE.
7. Ajuste de hiperparâmetros utilizando GridSearchCV.
8. Interpretação da importância das variáveis com XGBoost e SHAP.

Resultados

Resultados obtidos no conjunto de teste:

| Modelo | Precision — fraude | Recall — fraude | F1-score — fraude |
|---|---:|---:|---:|
| Regressão Logística | 0,86 | 0,61 | 0,72 |
| Random Forest | 0,83 | 0,76 | 0,80 |
| XGBoost original | 0,94 | 0,78 | 0,85 |
| XGBoost otimizado | 0,84 | 0,72 | 0,78 |

O XGBoost original apresentou o melhor F1-score entre os modelos avaliados. Seu ROC-AUC foi de aproximadamente 0,9569.

O GridSearchCV selecionou os parâmetros `max_depth=5` e `n_estimators=100`. O modelo otimizado apresentou ROC-AUC de aproximadamente 0,9134.

Principais aprendizados

- A acurácia isolada pode ser enganosa em problemas com classes desbalanceadas.
- O recall permite avaliar a proporção de fraudes identificadas.
- A precision ajuda a entender a proporção de alertas de fraude que são realmente fraudes.
- A escolha do modelo e do limiar depende do equilíbrio entre fraudes não detectadas e falsos positivos.
- Ferramentas como GridSearchCV e SHAP ajudam, respectivamente, na otimização e interpretação dos modelos.

Observação

Projeto educacional. Os resultados são específicos ao conjunto de teste utilizado e não representam garantia de desempenho em transações reais.

Autor

Cristiano Gonçalves
