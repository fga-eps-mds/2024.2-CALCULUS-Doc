# Planejamento de Risco

## Versionamento

| **Versão** | **Data** | **Modificação** | **Responsável** |
| :-: | :-: | :-: | :-: |
| 0.1 | 08/12/24 | Criação do documento | Gabriel Mariano, André Corrêa e Gabriel Costa |

*Tabela 1: Versionamento*

---

## Objetivos

Riscos são inerentes ao desenvolvimento de software, possuindo diferentes fontes (sejam internas ou externas à equipe, por exemplo), graus de previsibilidade e probabilidade e diferentes impactos na execução do projeto.

Para tal, a partir deste documento, objetiva-se estabelecer critérios para o acompanhamento do risco ao longo do projeto. Para além disso, propoẽ-se o efetivo monitoramento dos mesmos, com atualização constante no período citado.

## Classificações

### Quanto à Fonte

No tocante às origens dos riscos do projeto, foram determinadas algumas fontes para tais, conforme pode ser visto abaixo:

| **Fonte** | **Característica** |
| :-: | :-: |
| **Interno** | Riscos originados internamente ao projeto, isto é, no contexto do ambiente de trabalho e comunicação da equipe. |
| **Externo** | Riscos originados externamente ao projeto que possuem impacto direto ou indireto no mesmo. |
| **Gerencial** | Riscos originados a partir das atividades gerenciais da equipe. |
| **Técnico** | Riscos originados a partir de questões técnicas a serem executadas pela equipe. |
| **Pessoal** | Riscos originados a partir da equipe de desenvolvimento do projeto. |

*Tabela 2: Classificação dos riscos quanto à fonte*

### Quanto à Probabilidade

No tocante à probabilidade da ocorrência dos riscos do projeto, foram estabelecidos cinco graus a partir da divisão das probabilidades em *buckets*, para além da definição de *scores* para cada nível de probabilidade, como pode ser visto abaixo:

| **Nível de Risco** | **Grau de Probabilidade** | **Score** |
| :-: | :-: | :-: |
| Raro | < 0.1 | 0.1 |
| Improvável | 0.1 ~ 0.25 | 0.2 |
| Moderado | 0.25 ~ 0.5 | 0.4 |
| Provável | 0.5 ~ 0.75 | 0.6 |
| Quase Certo | > 0.75 | 0.8 |

*Tabela 3: Classificação dos riscos quanto à probabilidade*

### Quanto ao Impacto

No tocante ao impacto de cada risco no projeto, foram estabelecidos cinco graus de impacto a partir da divisão em *buckets*, para além da definição de *scores* para cada nível de impacto, como pode ser visto abaixo:

| **Nível de Impacto** | **Grau de Impacto** | **Score** |
| :-: | :-: | :-: |
| Quase Nulo | < 0.1 | 0.1 |
| Baixo | 0.1 ~ 0.25 | 0.2 |
| Moderado | 0.25 ~ 0.5 | 0.4 |
| Alto | 0.5 ~ 0.75 | 0.6 |
| Altíssimo | > 0.75 | 0.8 |

*Tabela 4: Classificação dos riscos quanto ao impacto*

### Quanto ao *Score*

A partir da definição do grau de probabilidade (*P*) e do nível de impacto (*I*) para cada risco, será calculado o *score* (*S*) de tal risco a partir da multiplicação dos scores para ambos os fatores, podendo assim obter uma definição quantitativa dos riscos para cada sprint.

$$
S = P * I
$$

*Fórmula 1: Cálculo do Score de Criticidade do Risco*

## Definição dos Riscos

A definição de riscos foi criada em uma planilha externa, a qual pode ser encontrada [NESSE LINK](https://docs.google.com/spreadsheets/d/1o43ntaEg_9Ez_WUeEvSivVT0YTsDGu8CkFLDqTU740E/edit?usp=sharing) e pode ser vista abaixo:

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSFCkM9vnQzb9I3ABhfvwZmqgLRthZEOeVp5lc45L3PjIHKW0aZ3qgj3ouBfVX8VeW2W8ke36tJlH_t/pubhtml?gid=1692350857&amp;single=true&amp;widget=true&amp;headers=false" width=650 height=600></iframe>

## Acompanhamento dos Riscos

Ainda na planilha acima, foram criadas abas para a avaliação do impacto e probabilidade de cada item de risco citado anteriormente, com o cálculo do *score* de cada um, para além do acompanhamento da evolução do risco por sprints em um gráfico, como pode ser acessado [NESSE LINK](https://docs.google.com/spreadsheets/d/1o43ntaEg_9Ez_WUeEvSivVT0YTsDGu8CkFLDqTU740E/edit?usp=sharing) ou então visto abaixo:

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSFCkM9vnQzb9I3ABhfvwZmqgLRthZEOeVp5lc45L3PjIHKW0aZ3qgj3ouBfVX8VeW2W8ke36tJlH_t/pubhtml?widget=true&amp;headers=false" width=1000 height=600></iframe>

## Plano de Ação

O plano de ação para cada risco elicitado também se encontra na tabela disponibilizada [NESSE LINK](https://docs.google.com/spreadsheets/d/1o43ntaEg_9Ez_WUeEvSivVT0YTsDGu8CkFLDqTU740E/edit?usp=sharing) e abaixo:

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSFCkM9vnQzb9I3ABhfvwZmqgLRthZEOeVp5lc45L3PjIHKW0aZ3qgj3ouBfVX8VeW2W8ke36tJlH_t/pubhtml?widget=true&amp;headers=false" width=1000 height=600></iframe>

## Referências

ROCHA, C.; NERI, H. R. Gestão de Portfólios e Projetos de Software - Fases ou Grupos de Processo: Planejamento II. Disponível em [repositório do GitHub](https://github.com/fga-eps-mds/A-Disciplina-MDS-EPS/blob/master/GPP_Material/06%20-%20Planejamento%20II/main.pdf).

JUNCKES, G. D.; MORGADO, P. Gerência de riscos em desenvolvimento de software. Disponível em: <https://www.devmedia.com.br/gerencia-de-riscos-em-desenvolvimento-de-software/28506>.

Calculus (2024.1). Estrutura Analítica de Riscos. Disponível em: <https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/planos/planos_riscos/>.

MeasureSoftGram (2024.1). Plano de Gestão de Riscos. Disponível em: <https://fga-eps-mds.github.io/2024.1-MeasureSoftGram-DOC/planejamento/riscos/>.

Sentinela (2024.1). Riscos do Projeto Sentinela. Disponível em: <https://fga-eps-mds.github.io/2024.1-SENTINELA-DOC/gestao/riscos/>.
