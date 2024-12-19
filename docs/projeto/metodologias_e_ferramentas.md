# Metodologias e Ferramentas

## Versionamento

| **Versão** | **Data** | **Modificação** | **Responsável** |
| :-: | :-: | :-: | :-: |
| 0.1 | 18/12/24 | Criação do documento e definição do Scrum | Gabriel Mariano e André Corrêa |
| 0.2 | 19/12/24 | Definição das demais metodologias e das ferramentas | Gabriel Mariano |

*Tabela 1: Versionamento*

---

## Objetivo

Ao decorrer do projeto, é proposto o uso de diversas metodologias ágeis em prol da organização, eficiência e adaptabilidade do desenvolvimento. Deste modo, este artefato visa documentar as principais metodologias utilizadas no projeto, para além das principais ferramentas utilizadas neste.

## Metodologias, Frameworks e Workshops

### Scrum

Conforme proposto por Schwaber e Sutherland (2020), o Scrum é um *framework* que visa guiar o desenvolvimento de maneira adaptável, incremental e colaborativa. O Scrum se baseia fundamentalmente em um conjunto de papéis e ritos.

Dentre os papeis, o Scrum cita o *Product Owner (P.O.)*, o *Scrum Master (S.M.)* e o *Scrum Team*, sendo o *P.O.* pela formação do *backlog*, o *S.M.* o responsável pela execução dos ritos e o *S.T.* a equipe responsável pela execução e validação das atividades que geram valor ao projeto.

Dentre os ritos, pode-se citar a *Sprint Planning* (onde há a construção do *backlog* da *sprint* e uma definição dos responsáveis), a *Sprint Review* (onde há uma revisão - ou inspeção - geral dos artefatos entregues) e a *Sprint Retrospective* (onde há uma discussão geral de fatores positivos, negativos e possíveis melhorias com base na *sprint* passada).

No contexto do projeto, buscamos realizar todos os ritos supracitados nas *sprints* ao decorrer do projeto, para além de reuniões presenciais (*standups*) em dias pré-definidos, sendo geralmente no intervalo entre as aulas da presente disciplina. Com relação aos papéis, há uma divisão "natural" seguindo algumas das propostas da disciplina, com a definição de um *P.O.*, a definição de um *Scrum Master* responsável pelos ritos e a consequente definição de um *Scrum Team*.

### Extreme Programming (XP)

Voltada para o desenvolvimento de software, o *Extreme Programming (XP)* - criado por Kent Beck nos anos 90 - é, aliado às outras metodologias, um importante *framework* que auxiliará no desenvolvimento do projeto. Através do estabelecimento de boas práticas e princípios, o XP nos permite o desenvolvimento de um bom produto de *software* de maneira adaptável e cíclica.

No contexto do atual projeto, são utilizadas práticas como o *Pair Programming*, o desenvolvimento iterativo com validação do cliente, o estabelecimento de histórias de usuário validadas pelo P.O. e há constante validação dos artefatos produzidos. Como pode ser visto no [**Planejamento de Comunicação**](../equipe/planejamento_de_comunicacao.md), também há uma valorização da comunicação, um dos valores propostos pelo *XP*.

### Kanban

Surgindo no meio industrial do Japão na década de 40, o Kanban é um método comumente utilizado em paralelo à outras metodologias ágeis em prol da definição de um fluxo linear de trabalho, facilitando a organização, acompanhamento e visualização do mesmo. O Kanban se baseia em um quadro composto por raias e cartões, onde cada cartão representa uma tarefa a ser executada, sendo alocado em uma raia que, por sua vez, representa o "estado atual" da atividade em questão. Uma estrutura básica de raias é composta por: "A fazer", "Em andamento" e "Concluído".

Em nosso projeto, o *Kanban* é aplicado através da ferramenta *ZenHub*, a qual será melhor detalhada na seção de "Ferramentas".

### Lean Inception

O *Lean Inception* é um workshop definido por Caroli (2018, p. 16) como "uma sequência de atividades para a criação de produtos de forma enxuta fortemente influenciadas por Design Thinking e Lean Startup". Em nosso contexto, o *workshop Lean Inception*, seguindo a abordagem proposta por Caroli (2018) e dando continuidade à [visão de produto proposta pela equipe do semestre anterior](https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/lean/canvas_mvp/), foi de fundamental relevância para a evolução e definição de nossa visão de produto, obtendo como resultado a definição de nosso [*Minimum Viable Product (MVP)*](../Lean_Inception/canvas_mvp.md).

Todas as etapas do *workshop* realizado pela equipe estão documentados nos artefatos da aba "*Lean Inception*".

## Ferramentas

Para a evolução do projeto, são utilizadas diversas ferramentas com fins específicos ou não. Abaixo, são listadas algumas dessas em conjunto com sua(s) finalidade(s). As ferramentas utilizadas para a comunicação do grupo estão listadas no [**Planejamento de Comunicação**](../equipe/planejamento_de_comunicacao.md).

| **Ferramenta** | **Objetivo** |
| :-: | :-: |
| [*Visual Studio Code*](https://code.visualstudio.com/) | Editor de código, utilizado para o desenvolvimento de *software*.  |
| [*Neovim*](https://neovim.io/) | Editor de texto/código *CLI* baseado em *Vim*. |
| [*Android Studio*](https://developer.android.com/studio?hl=pt-br) | *Ambiente de Desenvolvimento Integrado* para aplicações mobile. Compatível com o [*Flutter*](https://docs.flutter.dev/). |
| [*Mongo Atlas*](https://www.mongodb.com/pt-br/atlas) | Plataforma *cloud* para o uso do banco de dados *Mongo*. |
| [*Render*](https://render.com/) | Plataforma *cloud* para o *deploy* dos microserviços. |
| [*MongoDB Compass*](https://www.mongodb.com/pt-br/products/tools/compass) | Ferramenta *GUI desktop* para acesso ao banco de dados *Mongo*.  |
| [*Insomnia*](https://insomnia.rest/) (ou [*Postman*](https://www.postman.com/)) | Ferramentas para, dentre outras funcionalidades, envio de requisições *HTTP* para os microserviços. |
| [*Docker*](https://www.docker.com/) | Plataforma para a conteinerização de aplicações. Usada juntamente com a ferramenta **Docker-Compose**, cujo objetivo é realizar a "orquestração" dos conteineres. |
| [*Zenhub*](https://www.zenhub.com/) | Plataforma para a gestão de projetos capaz de se integrar ao *GitHub*. Conta com um quadro *Kanban* para o acompanhamento das histórias (e demais atividades) desenvolvidas. |
| [*Github*](https://github.com/) | Plataforma para o armazenamento e gestão de repositórios. |

*Tabela 2: Ferramentas*

## Fontes

SCHWABER, K.; SUTHERLAND, J. **O Guia do Scrum: O Guia Definitivo para o Scrum**. Scrum Guides, 2020. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf>.

LambdaTest. **Extreme Programming Tutorial: Comprehensive Guide With Best Practices**, por Irshad Ahamed. Disponível em: <https://www.lambdatest.com/learning-hub/extreme-programming>.

Nimble. **What Is Extreme Programming (XP)? It's Values, Principles, And Practices**, por Marjan Venema (2024). Disponível em: <https://www.nimblework.com/agile/extreme-programming-xp/>.

Atlassian. **Kanban: Como a metodologia Kanban é aplicada ao desenvolvimento de software**. Disponível em: <https://www.atlassian.com/br/agile/kanban#:~:text=O%20m%C3%A9todo%20Kanban%20%C3%A9%20uma,e%20transpar%C3%AAncia%20total%20de%20trabalho.>.

CAROLI, Paulo. **Lean Inception: como alinhar pessoas e construir o produto certo**. Primeira edição atualizada. São Paulo: Editora Caroli, 2018.
