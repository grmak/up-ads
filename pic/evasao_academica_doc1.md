# 📊 Estudo sobre Evasão Acadêmica com Machine Learning

# 📐 SEMANA 0 – Nivelamento Matemático-Estatístico

## ⏱️ Carga horária: 10 horas

**Objetivo:** Nivelar os conceitos matemáticos e estatísticos essenciais para não travar durante a modelagem.

---

## 📅 Cronograma diário

| Dia | Tópico | Tempo | Recurso sugerido |
|-----|--------|-------|------------------|
| Seg | Média, mediana, moda, variância, desvio padrão | 2h | StatQuest: "Mean, Median, and Mode" (YouTube) |
| Ter | Percentis, boxplot, IQR, identificação de outliers | 2h | Khan Academy: "Box plots" |
| Qua | Correlação de Pearson, scatterplots, interpretação | 2h | StatQuest: "Correlation" (YouTube) |
| Qui | Probabilidade condicional, Teorema de Bayes | 2h | 3Blue1Brown: "Bayes' theorem" (YouTube) |
| Sex | Distribuição normal, distribuição binomial (intuição prática) | 1.5h | StatQuest: "Probability Distributions" |
| Sáb | Logaritmos naturais (para entender log-odds da regressão logística) | 0.5h | Revisão rápida: vídeo "Logarithms explained" |

---

## 📝 Conteúdo detalhado

### 1. Estatística descritiva (Segunda)

| Conceito | Fórmula | Aplicação no projeto |
|----------|---------|----------------------|
| Média | $\bar{x} = \frac{\sum x_i}{n}$ | Nota média do aluno |
| Mediana | Valor central | Nota mediana (robusta a outliers) |
| Moda | Valor mais frequente | Curso mais comum entre evadidos |
| Variância | $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$ | Dispersão das faltas |
| Desvio padrão | $s = \sqrt{s^2}$ | Variação típica de desempenho |

### 2. Boxplot e outliers (Terça)


**Aplicação:** Identificar alunos com número extremo de faltas (ex: > 50% do semestre).

### 3. Correlação de Pearson (Quarta)

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

| Valor de r | Interpretação |
|------------|---------------|
| +1 | Correlação positiva perfeita |
| 0 | Sem correlação linear |
| -1 | Correlação negativa perfeita |

**Aplicação:** Verificar se `faltas` e `nota final` são correlacionadas negativamente.

### 4. Probabilidade condicional (Quinta)

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Exemplo aplicado:**  
$P(\text{evasão} \mid \text{faltas} > 30\%) = \frac{P(\text{evasão e faltas} > 30\%)}{P(\text{faltas} > 30\%)}$

### 5. Teorema de Bayes (Quinta)

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

**Aplicação:** Base da regressão logística. Permite calcular a probabilidade de evasão dadas as características do aluno.

### 6. Distribuições (Sexta)

| Distribuição | Característica | Aplicação |
|--------------|----------------|-----------|
| Normal (Gaussiana) | Simétrica, sino | Notas de turmas grandes |
| Binomial | Sucesso/fracasso | Número de alunos que evadem em uma turma |

### 7. Logaritmos naturais (Sábado)

$$\ln(e^x) = x \quad \text{e} \quad e^{\ln(x)} = x$$

**Aplicação:** Regressão logística usa **log-odds**:

$$\text{log-odds} = \ln\left(\frac{p}{1-p}\right)$$

Onde $p$ = probabilidade de evasão.

---

## ✅ Entregável da Semana 0

Responda as 10 questões abaixo (respostas no final para autoavaliação):

1. Calcule a média de [5, 10, 15, 20, 50]
2. Qual o desvio padrão aproximado dos mesmos números?
3. O que significa uma correlação de -0.85 entre horas de estudo e evasão?
4. Se P(evasão) = 0.2 e P(faltas altas) = 0.3, e P(ambos) = 0.15, calcule P(evasão | faltas altas)
5. Qual a diferença entre variância e desvio padrão?
6. O que um boxplot mostra que um histograma não mostra?
7. Dê um exemplo de distribuição binomial no contexto acadêmico.
8. Por que usamos log-odds em vez de probabilidade direta na regressão logística?
9. Se o log-odds é 2, qual a probabilidade de evasão? (use $p = e^{log-odds}/(1+e^{log-odds})$)
10. O que significa um outlier no contexto de faltas de um aluno?

---

## 🔑 Respostas (não olhe antes de tentar)

1. 20
2. ~17.1
3. Quanto mais horas de estudo, menor a evasão (forte correlação negativa)
4. 0.15 / 0.3 = 0.5 (50%)
5. Variância é o quadrado do desvio padrão; desvio padrão está na unidade original
6. Outliers explícitos e quartis
7. Número de alunos reprovados em uma turma de 40, com probabilidade de reprovação 0.2
8. Log-odds varia de -∞ a +∞ (sem restrições), probabilidade fica entre 0 e 1
9. $e^2/(1+e^2) = 7.389/8.389 \approx 0.88$ (88%)
10. Um aluno com faltas muito acima do padrão da turma (ex: mais que Q3 + 1.5×IQR)

---

# 📊 TABELA RESUMO – Matemática por Modelo de Machine Learning

## Nível de exigência matemática para cada modelo usado no projeto

| Modelo | Conceitos matemáticos | Nível | Obrigatório? |
|--------|----------------------|-------|---------------|
| **Regressão Logística** | Função sigmoide, log-odds, máxima verossimilhança (intuição), logaritmos | 🟡 Médio | ✅ Sim |
| **Árvore de Decisão** | Entropia, ganho de informação, Gini, divisão recursiva | 🟢 Baixo | ✅ Sim |
| **Random Forest** | Bootstrap, agregação por maioria/média, bagging | 🟢 Baixo | ✅ Sim |
| **XGBoost / LightGBM** | Gradiente descendente (intuição), função de perda (log-loss), regularização L1/L2 | 🟡 Médio | ✅ Sim (pelo menos um) |
| **SHAP (explicabilidade)** | Shapley values (teoria dos jogos cooperativos), média marginal | 🟠 Médio-Alto | ✅ Sim (para apresentação) |
| **SVM (se usado)** | Hiperplanos, kernel trick, margem máxima | 🔴 Alto | ❌ Opcional |
| **Redes Neurais** | Backpropagation, ativações (ReLU, sigmoide), gradiente descendente | 🔴 Alto | ❌ Opcional (avançado) |

---

## 🎯 Detalhamento por conceito

### 🟢 Nível Baixo (essencial para todos)

| Conceito | Onde é usado |
|----------|--------------|
| Média aritmética | Random Forest (agregação) |
| Contagem/frequência | Árvore (divisões) |
| Porcentagem | Balanceamento de classes |
| Probabilidade básica | Regressão logística |

### 🟡 Nível Médio (necessário para entender o modelo)

| Conceito | Onde é usado | Fórmula relevante |
|----------|--------------|-------------------|
| Função sigmoide | Regressão logística | $\sigma(z) = \frac{1}{1+e^{-z}}$ |
| Log-odds | Regressão logística | $\ln(\frac{p}{1-p}) = \beta_0 + \beta_1 x$ |
| Entropia de Shannon | Árvore de decisão | $H = -\sum p_i \log_2(p_i)$ |
| Índice Gini | Árvore de decisão | $G = 1 - \sum p_i^2$ |
| Log-loss | XGBoost | $L = -[y \ln(p) + (1-y) \ln(1-p)]$ |
| Curva ROC / AUC | Avaliação de qualquer classificador | AUC = área sob a curva |

### 🟠 Nível Médio-Alto (para dominar o modelo)

| Conceito | Onde é usado | Intuição |
|----------|--------------|----------|
| Shapley values | SHAP | Distribuição justa da "contribuição" de cada variável |
| Gradiente descendente | XGBoost, Redes Neurais | Caminhar na direção que reduz o erro |
| Regularização L1/L2 | XGBoost, Regressão Logística | Penalizar coeficientes grandes para evitar overfitting |
| Bootstrap | Random Forest | Amostragem com reposição |

---

## ✅ Checklist de matemática por semana do plano

| Semana | Modelo | Pré-requisito matemático | Status no plano |
|--------|--------|--------------------------|-----------------|
| 0 (nova) | Nivelamento | Estatística descritiva, probabilidade, log | ✅ Adicionado |
| 5 | Regressão Logística | Sigmoide, log-odds, Bayes | ✅ Coberto pela Semana 0 |
| 6 | Árvore de Decisão | Entropia, Gini | ⚠️ Adicionar explicação rápida |
| 7 | Random Forest | Bootstrap, média | ✅ Simples, OK |
| 8 | Métricas | Curva ROC, AUC | ⚠️ Detalhar na semana 8 |
| 9-10 | XGBoost | Gradiente, função de perda | ⚠️ Adicionar intuição na semana 9 |
| 11 | SHAP | Shapley values | ⚠️ Explicar antes de usar |

---

## 📚 Recursos gratuitos para a matemática

| Tópico | Melhor recurso gratuito |
|--------|-------------------------|
| Estatística descritiva | Khan Academy - Statistics and probability |
| Probabilidade condicional | 3Blue1Brown - Bayes' theorem (YouTube) |
| Entropia e Gini | StatQuest - Decision Trees (YouTube) |
| Regressão logística | StatQuest - Logistic Regression (YouTube) |
| Curva ROC | StatQuest - ROC and AUC (YouTube) |
| Shapley values | StatQuest - SHAP (YouTube) |
| Gradiente descendente | 3Blue1Brown - Gradient Descent (YouTube) |

---

## 🚀 Conclusão

Com a **Semana 0** concluída, você terá a base matemática para:

- Entender **por que** cada modelo funciona
- Interpretar coeficientes da regressão logística
- Explicar árvores de decisão para a banca
- Usar SHAP com propriedade
- Não depender cegamente das bibliotecas

**Agora você está pronto para começar o Mês 1! 🎓**


## 🧠 1. Uso de Regressão Linear

A regressão linear é adequada quando a variável alvo (Y) é contínua.

### ✅ Exemplos de uso:
- Tempo até evasão (meses/semestres)
- Percentual de curso concluído
- Desempenho acadêmico

### ⚠️ Premissas:
- Linearidade
- Independência dos erros
- Homoscedasticidade
- Normalidade dos resíduos
- Baixa multicolinearidade

### ❌ Não recomendado:
- Quando Y é binário (evasão: sim/não)

---

## 🤖 2. Modelos de Machine Learning

### 🟢 Modelos básicos:
- Regressão logística
- Árvore de decisão

### 🟡 Intermediários:
- Random Forest
- Gradient Boosting (XGBoost, LightGBM)
- SVM

### 🔵 Avançados:
- Redes neurais
- Modelos de sobrevivência (Cox)

### 📊 Variáveis comuns:
- Notas
- Frequência
- Dados financeiros
- Perfil do aluno
- Engajamento

---

## 🤔 Quantidade de algoritmos

Apesar de existirem muitos algoritmos, os principais são:
- Regressão logística
- Random Forest
- Gradient Boosting

---

## 🎓 3. Pré-requisitos para PIC

### 📊 Técnicos:
- Estatística básica
- Python (pandas, scikit-learn)
- Tratamento de dados
- Avaliação de modelos

### 🧠 Cognitivos:
- Entendimento do problema
- Definição correta do alvo
- Interpretação dos resultados
- Evitar vieses

---

## ⚠️ Dívidas comuns

### 🔴 Técnica:
- Dados inconsistentes
- Falta de integração

### 🔴 Cognitiva:
- Problema mal definido
- Métricas mal interpretadas

---

## 💡 Estrutura do Projeto

1. Definir evasão
2. Coletar dados
3. Limpar dados
4. Análise exploratória
5. Modelagem
6. Avaliação
7. Interpretação
8. Propostas de ação

---

## 🧾 Resumo

- Regressão linear: para variáveis contínuas
- Classificação: melhor para evasão
- Clareza do problema é mais importante que técnica
