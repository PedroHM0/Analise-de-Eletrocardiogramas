# Análise de Sinais de Eletrocardiogramas para Detecção de Arritmias

## 📋 Descrição do Projeto

Este projeto implementa uma solução completa para análise de sinais de eletrocardiograma (ECG) com o objetivo de detectar automaticamente casos de arritmia cardíaca. A abordagem combina técnicas avançadas de processamento de sinais, extração de características estatísticas e espectrais, e aplicação de algoritmos de aprendizado de máquina para classificação binária.

## 🎯 Objetivos

- **Processamento de Sinais**: Análise estatística e espectral de sinais de ECG
- **Extração de Características**: Cálculo de métricas discriminantes (média, desvio padrão, skewness, kurtosis, energia, extremos)
- **Classificação Inteligente**: Implementação de modelo de Machine Learning para detecção automática de arritmias
- **Avaliação de Performance**: Análise da eficácia do modelo através de métricas de classificação

## 🛠️ Tecnologias Utilizadas

### Linguagens e Bibliotecas
- **Python 3.x**
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação científica e operações matriciais
- **SciPy**: Processamento de sinais digitais (FFT, filtros)
- **Scikit-learn**: Algoritmos de Machine Learning
- **Matplotlib**: Visualização de dados e gráficos
- **Seaborn**: Visualizações estatísticas avançadas

### Técnicas Implementadas
- Processamento digital de sinais biomédicos
- Transformada Rápida de Fourier (FFT)
- Análise estatística multivariada
- Regressão Logística para classificação
- Validação cruzada e métricas de avaliação

## 📁 Estrutura do Projeto

```
projeto-ecg-analysis/
│
├── treino_eletro.csv                           # Dataset principal
├── Analise_De_Sinais_Eletrocardiogramas.py    # Análise exploratória e FFT
├── Regressao_Logistica_Eletrocardiogramas.py  # Modelo de classificação
└── README.md                                   # Documentação
```

## 📊 Dataset

O dataset `treino_eletro.csv` contém **300 amostras** de sinais de ECG processados, com as seguintes características:

### Features Extraídas
- **Media_arritmia**: Valor médio do sinal
- **Desviopadrao_arritmia**: Medida de dispersão dos dados
- **Skewness_arritmia**: Assimetria da distribuição
- **SKurtosis_arritmia**: Curtose (achatamento da distribuição)
- **Energia_arritmia**: Energia total do sinal
- **Max_arritmia**: Valor máximo registrado
- **Min_arritmia**: Valor mínimo registrado
- **resultado**: Target binário (0 = Normal, 1 = Arritmia)

## 🔬 Metodologia

### 1. Análise Exploratória (`Analise_De_Sinais_Eletrocardiogramas.py`)
- **Cálculo de Estatísticas**: Implementação de funções customizadas para métricas estatísticas
- **Análise Espectral**: Aplicação de FFT para identificação de componentes frequenciais
- **Visualização Comparativa**: Gráficos de dispersão e análise de correlação
- **Separação de Grupos**: Comparação visual entre sinais normais e arrítmicos

### 2. Modelagem Preditiva (`Regressao_Logistica_Eletrocardiogramas.py`)
- **Pré-processamento**: Divisão treino/teste (70/30)
- **Algoritmo**: Regressão Logística com parâmetros otimizados
- **Avaliação**: Matriz de confusão e cálculo de acurácia
- **Visualização**: Heatmap da matriz de confusão

## 📈 Principais Resultados

### Análise Exploratória
- Identificação clara de padrões diferenciadores entre ECGs normais e arrítmicos
- Componentes espectrais específicas correlacionadas com arritmias
- Visualizações que evidenciam a separabilidade dos dados

### Performance do Modelo
- **Algoritmo**: Regressão Logística
- **Métricas**: Matriz de confusão detalhada
- **Acurácia**: Calculada automaticamente pelo sistema
- **Interpretabilidade**: Modelo linear facilita compreensão clínica

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install pandas numpy scipy scikit-learn matplotlib seaborn
```

### Execução da Análise
```bash
# Análise exploratória e visualizações
python Analise_De_Sinais_Eletrocardiogramas.py

# Treinamento e avaliação do modelo
python Regressao_Logistica_Eletrocardiogramas.py
```

## 📋 Funcionalidades Implementadas

### Processamento de Sinais
- [x] Extração de características estatísticas
- [x] Análise espectral com FFT
- [x] Cálculo de métricas de dispersão
- [x] Análise de correlação entre grupos

### Machine Learning
- [x] Implementação de Regressão Logística
- [x] Divisão automática treino/teste
- [x] Geração de matriz de confusão
- [x] Cálculo automático de métricas

### Visualização
- [x] Gráficos de dispersão comparativos
- [x] Visualização da FFT
- [x] Heatmap da matriz de confusão
- [x] Análise visual de correlações

## 🎓 Aplicações e Relevância

### Área Biomédica
- Auxílio no diagnóstico precoce de arritmias
- Triagem automatizada de exames de ECG
- Suporte a decisões clínicas baseadas em evidências

### Engenharia de Dados
- Demonstração de pipeline completo de dados biomédicos
- Implementação de técnicas de feature engineering
- Aplicação prática de algoritmos de classificação

### Potencial de Expansão
- Integração com sistemas hospitalares
- Implementação de outros algoritmos de ML
- Análise em tempo real de sinais cardíacos

## 🏆 Diferenciais Técnicos

- **Implementação Robusta**: Código modular e bem estruturado
- **Análise Completa**: Combina estatística descritiva e análise espectral
- **Visualização Rica**: Múltiplas perspectivas dos dados
- **Aplicação Prática**: Relevância direta para área médica
- **Escalabilidade**: Base sólida para expansões futuras

## 👨‍💻 Autor

Pedro Henrique Macedo de Oliveira
- Graduando em Engenharia da Computação
