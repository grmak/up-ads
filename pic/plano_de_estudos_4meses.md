# 📅 Plano de Estudos Detalhado – Evasão Acadêmica com Machine Learning

## 🎯 Objetivo
Ficar apto a desenvolver um projeto de previsão de evasão acadêmica em **4 meses**, com carga de **10–12 horas semanais**, usando Python, SQL e modelos de classificação.

---

## 📦 Recursos Gratuitos Recomendados

| Tipo | Nome | Como acessar |
|------|------|---------------|
| Cursos interativos | Kaggle Learn (Pandas, ML Intro, Intermediate ML) | kaggle.com/learn |
| Vídeos | StatQuest com Josh Starmer (Random Forest, XGBoost, SHAP) | YouTube |
| Livro online | "Python Data Science Handbook" (VanderPlas) | gratuito via GitHub |
| Prática | UCI Machine Learning Repository (dados de evasão) | archive.ics.uci.edu |
| Simulação | Criar dados falsos com `make_classification` (sklearn) | documentação sklearn |

---

# 📅 MÊS 1 – FUNDAÇÃO (Dados, SQL, Python, Definição do Problema)

## Semana 1 – Python essencial para dados
**Objetivo:** Manipular DataFrames sem sofrer.

| Dia | Tópico | Tempo | Recurso sugerido |
|-----|--------|-------|------------------|
| Seg | Tipos de dados, listas, dicionários, loops | 2h | Curso Python para Data Science (Kaggle) |
| Ter | NumPy básico (arrays, operações vetorizadas) | 2h | NumPy quickstart tutorial |
| Qua | Pandas: Series, DataFrame, leitura de CSV | 2h | Pandas: 10 minutos to pandas |
| Qui | Seleção, filtro, `loc`, `iloc` | 2h | DataCamp: Pandas Foundations (gratuito) |
| Sex | `groupby`, `agg`, `merge` (joins) | 2h | Kaggle: Pandas course (micro-lessons) |
| Sáb | Exercício integrado: limpar uma base de alunos falsa | 2h | Criar seu próprio notebook |

**Entregável:** Notebook que lê um CSV, filtra alunos com nota > 7, agrupa por curso e conta.

---

## Semana 2 – Estatística descritiva + visualização
**Objetivo:** Entender e comunicar padrões nos dados.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Média, mediana, desvio padrão, quartis | 2h |
| Ter | Histograma, boxplot, scatterplot (matplotlib) | 2h |
| Qua | Seaborn: pairplot, heatmap de correlação | 2h |
| Qui | Identificar outliers e missing values | 2h |
| Sex | Storytelling com gráficos (evasão por curso, por renda) | 2h |
| Sáb | Mini-projeto: análise exploratória de dados públicos de evasão | 2h |

**Entregável:** Relatório com 4 gráficos e 3 insights sobre fatores de risco.

---

## Semana 3 – SQL para extrair dados acadêmicos
**Objetivo:** Buscar dados reais (ou simulados) de alunos, matrículas, notas, faltas.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | SELECT, WHERE, ORDER BY | 1.5h |
| Ter | JOIN (INNER, LEFT) entre alunos, matrículas, disciplinas | 2h |
| Qua | GROUP BY + COUNT, AVG (ex: média de faltas por aluno) | 2h |
| Qui | Subconsultas e CTEs (WITH) | 2h |
| Sex | Criar tabela com target (evasão: sim/não via regra de negócio) | 2h |
| Sáb | Exportar query final para CSV + integrar com pandas | 1.5h |

**Entregável:** Query SQL que gera uma base pronta para modelagem (aluno_id, features, target).

---

## Semana 4 – Definir evasão + baseline simples
**Objetivo:** Ter uma regra de negócio clara e um modelo burro para comparar.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Estudar definições de evasão (2 semestres sem matrícula, abandono, etc.) | 2h |
| Ter | Criar variável target no pandas (ex: `evadiu = 1 se data_saida - data_entrada > 365 dias`) | 2h |
| Qua | Baseline DummyClassifier (estratégia: sempre "não evade") | 2h |
| Qui | Métricas: acurácia, mas entender sua falha com dados desbalanceados | 2h |
| Sex | Documentar tudo: regra de evasão, suposições, limitações | 2h |
| Sáb | Revisão do mês 1 + gravação de 5 min explicando o baseline | 2h |

**Entregável:** Documento de 1 página: "O que é evasão neste projeto e como mediremos sucesso".

---

# 📅 MÊS 2 – MODELAGEM INICIAL E MÉTRICAS

## Semana 5 – Regressão logística + validação cruzada
**Objetivo:** Primeiro modelo real.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Teoria da regressão logística (função sigmoide, odds ratio) | 2h |
| Ter | Implementar com scikit-learn: `LogisticRegression` | 2h |
| Qua | Treino/teste split (70/30) + validação cruzada k-fold | 2h |
| Qui | Interpretar coeficientes (quais variáveis mais pesam) | 2h |
| Sex | Matriz de confusão (VP, VN, FP, FN) | 2h |
| Sáb | Calcular precisão, recall, F1 manualmente e com sklearn | 2h |

**Entregável:** Notebook que treina regressão logística e mostra os 5 coeficientes mais importantes.

---

## Semana 6 – Árvore de decisão e overfitting
**Objetivo:** Entender modelos que podem "decorar" os dados.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Como funciona árvore de decisão (ganho de informação, Gini) | 2h |
| Ter | `DecisionTreeClassifier` com profundidade padrão (overfitting) | 2h |
| Qua | Controlar overfitting: `max_depth`, `min_samples_split` | 2h |
| Qui | Visualizar a árvore (plot_tree) | 1h |
| Sex | Comparar árvore vs regressão logística (mesmas métricas) | 2h |
| Sáb | Escrever conclusão: quando árvore é melhor? | 1h |

**Entregável:** Gráfico da árvore + tabela comparativa de F1 entre os dois modelos.

---

## Semana 7 – Random Forest (o modelo curinga)
**Objetivo:** Modelo robusto que já resolve 80% dos problemas.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Teoria: bagging, amostragem bootstrap, agregação | 2h |
| Ter | `RandomForestClassifier` com parâmetros padrão | 2h |
| Qua | Importância de variáveis (feature importance) | 2h |
| Qui | Ajustar `n_estimators`, `max_features` | 2h |
| Sex | Comparar com regressão logística e árvore simples | 2h |
| Sáb | Documentar: o Random Forest ganhou? Por quê? | 1h |

**Entregável:** Ranking das 10 variáveis mais importantes para evasão.

---

## Semana 8 – Dados desbalanceados (a grande armadilha)
**Objetivo:** Não ser enganado por acurácia 95%.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Gerar base artificial com 5% de evasão (simular real) | 1.5h |
| Ter | Ver como acurácia engana (modelo que só chama "não evade") | 2h |
| Qua | Técnica 1: `class_weight='balanced'` no sklearn | 2h |
| Qui | Técnica 2: SMOTE (síntese de minoritários) | 2h |
| Sex | Técnica 3: undersampling da maioria | 2h |
| Sáb | Comparar F1, AUC-ROC, Precision-Recall curve | 2h |

**Entregável:** Tabela comparando 4 estratégias de balanceamento + melhor escolha justificada.

---

# 📅 MÊS 3 – MODELOS AVANÇADOS E EXPLICABILIDADE

## Semana 9 – XGBoost (estado da arte para tabelas)
**Objetivo:** Máximo desempenho com pouco esforço.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Instalar XGBoost, entender boosting sequencial | 2h |
| Ter | `XGBClassifier` com parâmetros padrão | 2h |
| Qua | GridSearchCV para `n_estimators`, `max_depth`, `learning_rate` | 2h |
| Qui | Early stopping para evitar overfitting | 2h |
| Sex | Comparar XGBoost vs Random Forest (mesmo dataset) | 2h |
| Sáb | Plotar curvas de aprendizado (learning curves) | 1h |

**Entregável:** Notebook com XGBoost tunado + ganho percentual em relação ao Random Forest.

---

## Semana 10 – LightGBM (mais rápido e tão bom quanto)
**Objetivo:** Velocidade para quando tiver muitos dados.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Diferenças LightGBM vs XGBoost (leaf-wise vs depth-wise) | 2h |
| Ter | Implementar `LGBMClassifier` | 2h |
| Qua | Ajustar `num_leaves`, `min_child_samples` | 2h |
| Qui | Comparar tempo de treino e performance | 2h |
| Sex | Escolher o melhor modelo final (entre Logística, RF, XGB, LGBM) | 2h |
| Sáb | Salvar modelo com `joblib` ou `pickle` | 1h |

**Entregável:** Modelo final salvo em disco + métricas em um DataFrame comparativo.

---

## Semana 11 – SHAP (explicar cada predição)
**Objetivo:** Convencer a instituição a confiar no modelo.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Teoria SHAP (Shapley values) – sem medo da matemática | 2h |
| Ter | Instalar shap, calcular valores para uma predição | 2h |
| Qua | Gráfico de resumo (summary_plot): variáveis globais | 2h |
| Qui | Gráfico de força (waterfall) para um aluno específico | 2h |
| Sex | Criar relatório automático: "Aluno X tem 80% de risco devido a falta e nota baixa" | 2h |
| Sáb | Integrar SHAP com o melhor modelo (XGB ou LGBM) | 2h |

**Entregável:** Dashboard simples (no notebook) que mostra explicação para 3 alunos de exemplo.

---

## Semana 12 – Pipeline completa e prevenção de data leakage
**Objetivo:** Código pronto para rodar todo semestre.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Criar `Pipeline` do sklearn (escalador + modelo) | 2h |
| Ter | Usar `ColumnTransformer` para variáveis categóricas | 2h |
| Qua | Simular data leakage: usar nota final do semestre para prever evasão no meio | 2h |
| Qui | Corrigir: usar apenas dados disponíveis até o momento da predição | 2h |
| Sex | Criar validação temporal (treinar com 2019-2022, testar em 2023) | 2h |
| Sáb | Documentar checklist anti-leakage | 1h |

**Entregável:** Pipeline completa + validação temporal documentada.

---

# 📅 MÊS 4 – PROJETO SIMULADO + PREPARAÇÃO PARA O REAL

## Semana 13 – Mini-projeto completo (dados públicos)
**Objetivo:** Simular o projeto real de ponta a ponta.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Baixar dados públicos de evasão (ex: UCI "Student Performance" ou Kaggle "Dropout Prediction") | 1h |
| Ter | Limpeza + criação do target | 3h |
| Qua | Análise exploratória + 3 hipóteses | 3h |
| Qui | Modelagem (Logística + Random Forest + XGB) | 3h |
| Sex | Avaliação com métricas balanceadas + SHAP | 2h |
| Sáb | Escrever conclusões em 10 slides | 2h |

**Entregável:** Apresentação de 10 slides + notebook limpo e comentado.

---

## Semana 14 – Infra e operação (como rodar todo ano)
**Objetivo:** Não ser um modelo de uma vez só.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Versionar dados com DVC (ou salvar raw/processed) | 2h |
| Ter | Criar script `.py` (não só notebook) para reprodutibilidade | 2h |
| Qua | Agendar execução mensal com cron (ou GitHub Actions) | 2h |
| Qui | Salvar predições em CSV: alunos em risco na próxima semana | 2h |
| Sex | Criar alerta simples: e-mail com lista de alunos prioritários | 2h |
| Sáb | Documentar fluxo de atualização do modelo | 1h |

**Entregável:** Script Python que roda do zero e gera arquivo `alunos_em_risco.csv`.

---

## Semana 15 – Estruturar o projeto real (1 ano)
**Objetivo:** Deixar tudo pronto para começar a executar.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Mapear fontes de dados reais (sistema acadêmico, financeiro, pedagógico) | 2h |
| Ter | Criar dicionário de variáveis (nome, tipo, origem, periodicidade) | 2h |
| Qua | Definir janela de predição (ex: início do semestre, dados do semestre anterior) | 2h |
| Qui | Esboçar timeline do ano: mês 1-2 extração, mês 3-4 modelo, mês 5-6 validação, etc. | 2h |
| Sex | Listar riscos (dados faltando, mudança de regra de evasão) | 2h |
| Sáb | Revisar tudo com um colega (ou simular apresentação) | 2h |

**Entregável:** Documento "Plano do Projeto Real - 12 meses" com cronograma e riscos.

---

## Semana 16 – Revisão final + simulado de banca
**Objetivo:** Testar se você realmente aprendeu.

| Dia | Tópico | Tempo |
|-----|--------|-------|
| Seg | Revisar métricas (F1, AUC, recall) com exemplos | 2h |
| Ter | Revisar prevenção de data leakage (fazer 5 perguntas e responder) | 2h |
| Qua | Revisar SHAP: explicar para um leigo | 2h |
| Qui | Simular apresentação de 15 min (grave) | 2h |
| Sex | Identificar gaps e revisar tópicos fracos | 2h |
| Sáb | Descanso e celebração | - |

**Entregável:** Você mesmo confiante para começar o projeto de 1 ano.

---

## ✅ Checklist final – O que você saberá após 4 meses

- [ ] Manipular dados com Pandas e SQL
- [ ] Criar visualizações que geram insights
- [ ] Definir target de evasão corretamente
- [ ] Treinar Regressão Logística, Árvore, Random Forest, XGBoost, LightGBM
- [ ] Avaliar modelos com métricas adequadas para dados desbalanceados (F1, AUC)
- [ ] Explicar predições com SHAP
- [ ] Construir pipeline sem data leakage
- [ ] Criar um mini-projeto completo do zero
- [ ] Planejar a execução do projeto real de 1 ano

---

## ⚡ Resumo para você imprimir e colar na parede

> **Em 4 meses você precisa saber:**
> 1. Pandas + SQL (manipular dados)
> 2. Regressão logística, Random Forest, XGBoost
> 3. Métricas para dados desbalanceados (F1, AUC)
> 4. SHAP para explicar o modelo
> 5. Pipeline sem data leakage

**Bons estudos! 🚀**

