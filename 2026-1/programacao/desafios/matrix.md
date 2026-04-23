
---

## Algoritmo em Passos Lógicos

### Fase 1: Inicialização

1. **Obter dimensões** do terminal
   - Descobrir número de linhas (altura)
   - Descobrir número de colunas (largura)

2. **Criar matriz vazia**
   - Para cada linha de 0 até altura-1
     - Para cada coluna de 0 até largura-1
       - Definir célula.caractere = " "
       - Definir célula.intensidade = 0
       - Definir célula.tipo = "vazio"

3. **Configurar parâmetros da simulação**
   - Velocidade de atualização = 30 frames por segundo
   - Probabilidade base de nova cabeça = 10% por coluna por frame
   - Variação de velocidade entre colunas = 1 a 5

4. **Criar vetor de controle das colunas**
   - Para cada coluna de 0 até largura-1
     - Definir coluna.tem_cabeca = falso
     - Definir coluna.velocidade = número aleatório entre 1 e 5
     - Definir coluna.comprimento_rastro = número aleatório entre 3 e 8
     - Definir coluna.probabilidade_novo = número aleatório entre 0.05 e 0.15

---

### Fase 2: Loop Principal da Animação

Repetir **continuamente**:

#### Passo 1: Limpar a tela do terminal

- Mover cursor para posição (linha 0, coluna 0)
- Limpar todo o conteúdo visível
- Manter fundo preto

#### Passo 2: Atualizar o estado da matriz

**Para cada coluna** (da esquerda para a direita):

##### 2.1 Decidir se cria uma nova "cabeça" na coluna

- Gerar número aleatório entre 0 e 1
- Se número < coluna.probabilidade_novo E coluna.tem_cabeca == falso:
  - Selecionar caractere aleatório do conjunto disponível
  - Posicionar na linha 0 (topo), coluna atual
  - Definir célula.caractere = caractere_sorteado
  - Definir célula.tipo = "cabeca"
  - Definir célula.intensidade = 3 (brilhante)
  - Marcar coluna.tem_cabeca = verdadeiro
  - Definir coluna.posicao_cabeca = 0

##### 2.2 Mover cabeças existentes para baixo

**Se coluna.tem_cabeca == verdadeiro:**

- Calcular nova_linha = coluna.posicao_cabeca + coluna.velocidade
- Se nova_linha >= altura (ultrapassou o fundo da tela):
  - Remover cabeça:
    - célula[linha_antiga][coluna].tipo = "vazio"
    - célula[linha_antiga][coluna].caractere = " "
    - coluna.tem_cabeca = falso
  - **Pular para próxima coluna**

- **Senão** (está dentro da tela):
  - Caractere_cabeca = célula[linha_antiga][coluna].caractere
  - Intensidade_cabeca = célula[linha_antiga][coluna].intensidade
  
  - **Limpar posição antiga** (transformar em rastro):
    - célula[linha_antiga][coluna].tipo = "rastro"
    - célula[linha_antiga][coluna].intensidade = 2 (médio)
  
  - **Mover cabeça para nova posição**:
    - célula[nova_linha][coluna].caractere = caractere_cabeca
    - célula[nova_linha][coluna].tipo = "cabeca"
    - célula[nova_linha][coluna].intensidade = 3
    - coluna.posicao_cabeca = nova_linha

##### 2.3 Gerenciar o rastro (caracteres que seguem a cabeça)

**Para cada célula da coluna atual (de baixo para cima):**

- Se célula.tipo == "rastro":
  - **Diminuir intensidade em 1**
  - Se intensidade <= 0:
    - Remover caractere: célula.tipo = "vazio", célula.caractere = " "
  - Se intensidade == 2:
    - Manter caractere (pode continuar caindo lentamente ou ficar fixo)
  - Se intensidade == 1:
    - Caractere pode piscar ou mudar aleatoriamente com baixa probabilidade

##### 2.4 Atualizar células "soltas" (sem cabeça)

**Para cada célula da coluna atual:**

- Se célula.tipo == "solto" (caracteres sem movimento contínuo):
  - Com probabilidade de 5% a cada frame:
    - Mudar caractere aleatoriamente
    - Piscar (intensidade alterna entre 1 e 2)

---

#### Passo 3: Desenhar a matriz na tela

**Para cada linha** (de 0 até altura-1):
  
  **Para cada coluna** (de 0 até largura-1):
    
    - **Se célula.tipo == "vazio":**
      - Imprimir caractere de espaço (" ")
    
    - **Se célula.tipo == "cabeca":**
      - Aplicar cor verde brilhante (código ANSI: cor 92)
      - Imprimir célula.caractere
    
    - **Se célula.tipo == "rastro" E intensidade == 2:**
      - Aplicar cor verde médio (código ANSI: cor 32)
      - Imprimir célula.caractere
    
    - **Se célula.tipo == "rastro" E intensidade == 1:**
      - Aplicar cor verde escuro (código ANSI: cor 30, fundo preto)
      - Imprimir célula.caractere
    
    - **Se célula.tipo == "solto":**
      - Aplicar cor verde médio (código ANSI: cor 32)
      - Imprimir célula.caractere
  
  - **Ao final da linha**: pular para a próxima linha (Carriage Return + Line Feed)

---

#### Passo 4: Aguardar o próximo frame

- Pausar a execução por **0.033 segundos** (aproximadamente 30 frames por segundo)
- Voltar ao Passo 1 (Limpar tela)

---

### Fase 3: Efeitos Especiais e Variações

#### Velocidade Variável por Coluna

- Cada coluna tem sua própria velocidade (1 a 5 linhas/frame)
- Colunas mais rápidas parecem "na frente"
- Colunas mais lentas parecem "atrasadas" ou mais pesadas

#### Efeito de Esteira (Comprimento do Rastro)

- Cabeça deixa um rastro de N caracteres (ex: 5)
- Primeiro caractere atrás da cabeça: intensidade 2
- Segundo caractere: intensidade 1
- Terceiro em diante: intensidade 0 (desaparece)

#### Aleatoriedade de Caracteres

- Caracteres no rastro podem mudar aleatoriamente a cada frame
- Isso cria o efeito de "código mutante"

#### Ondas de Queda

- Evento especial (probabilidade 1% por frame):
  - Criar cabeças simultâneas em todas as colunas
  - Velocidade aumentada temporariamente

#### Variação de Cores

- Cabeça: Verde brilhante (#00FF00)
- Rastro recente: Verde médio (#00AA00)
- Rastro antigo: Verde escuro (#005500)
- Fundo: Preto (#000000)

---

## Fluxo Visual Esperado (Exemplo)
┌────────────────────────────────────────┐
│ 1. INICIALIZAÇÃO                       │
│ - Ler dimensões do terminal            │
│ - Criar matriz vazia                   │
│ - Configurar parâmetros                │
│ - Inicializar vetor de controle        │
└────────────────┬───────────────────────┘
                 ↓
╔════════════════════╗
║ LOOP INFINITO      ║
╚════════════════════╝
                ↓
┌────────────────────────────────────────┐
│ 2. LIMPAR TELA                         │
└────────────────┬───────────────────────┘
                 ↓
┌────────────────────────────────────────┐
│ 3. ATUALIZAR MATRIZ                    │
│ Para cada coluna:                      │
│ - Sortear nova cabeça                  │
│ - Mover cabeças existentes             │
│ - Gerenciar rastros                    │
│ - Atualizar células soltas             │
└────────────────┬───────────────────────┘
                 ↓
┌────────────────────────────────────────┐
│ 4. DESENHAR TELA                       │
│ Para cada linha:                       │
│ Para cada coluna:                      │
│ Aplicar cor conforme intensidade       │
│ Imprimir caractere ou espaço           │
└────────────────┬───────────────────────┘
                 ↓
┌────────────────────────────────────────┐
│ 5. AGUARDAR FRAME                      │
│ Pausar por 0.033 segundos              │
└────────────────┬───────────────────────┘
                 ↓
│
└──────→ voltar ao passo 2


---

## Parâmetros Configuráveis

| Parâmetro | Valor Padrão | Efeito |
|-----------|--------------|--------|
| FPS (frames por segundo) | 30 | Suavidade da animação |
| Probabilidade nova cabeça | 0.10 (10%) | Densidade de caracteres |
| Velocidade base | 2 linhas/frame | Rapidez da queda |
| Variação de velocidade | 1 a 5 | Assincronismo entre colunas |
| Comprimento do rastro | 3 a 8 | Tamanho da esteira |
| Probabilidade mutação | 0.05 (5%) | Frequência de mudança dos caracteres |

---

## Considerações de Performance

1. **Matriz redimensionável**: Se o usuário redimensionar o terminal, recriar matriz automaticamente

2. **Taxa de atualização**: 
   - 30 FPS oferece boa fluidez sem sobrecarregar CPU
   - Reduzir para 15-20 FPS em hardware mais antigo

3. **Uso de memória**:
   - Matriz 80x24 ≈ 2.000 células
   - Cada célula com 3 atributos ≈ 6KB de memória (muito leve)

4. **Otimização de desenho**:
   - Evitar redesenhos desnecessários (redesenhar apenas células que mudaram)
   - Usar buffer duplo (desenhar em memória, depois enviar ao terminal)

---

## Variações Avançadas

### Interatividade com Mouse

- Posição do mouse detectada:
  - Na área do mouse: caracteres aceleram
  - Cabeças "fogem" do mouse
  - Efeito de "splash" de caracteres ao clicar

### Modo Chuva

- Todas as colunas têm cabeça ativa simultaneamente
- Velocidades variam entre colunas
- Chuva intensa com rastros longos

### Modo Onda

- Cabeças começam no topo e descem em formato de onda senoidal
- Velocidade varia conforme posição na tela

### Modo Espectro

- Cores mudam ciclicamente (verde → ciano → azul → verde)
- Velocidade de mudança configurável

---
