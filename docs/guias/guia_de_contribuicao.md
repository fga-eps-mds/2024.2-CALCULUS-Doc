# Guia de Contribuição

## Versionamento

| **Versão** | **Data** | **Modificação** | **Responsável** |
| :-: | :-: | :-: | :-: |
| 0.1 | 09/11/24 | Criação do documento | Gabriel Mariano e André Corrêa |
| 0.2 | 10/11/24 | Definição das políticas | Gabriel Mariano |
| 0.3 | 20/11/24 | Altera nomenclatura proposta para *branches* | Gabriel Mariano |

*Tabela 1: Versionamento*

---

## Objetivo

Dada a natureza colaborativa do desenvolvimento do presente projeto *Open Source*, este artefato visa estabelecer padrões e critérios de colaboração com o mesmo. O respeito às mesmas resultará em um processo de desenvolvimento mais linear, menos suscetível a erros e mais organizado, para além de permitir a rastreabilidade dos recursos e artefatos desenvolvidos.

## Políticas

### Issues

A criação de *issues* do projeto se dará através da plataforma *ZenHub* associada aos repositórios. Para tal, os membros responsáveis pelo projeto devem criar *issues* para cada atividade a ser realizada, de modo a seguir os princípios abaixo estabelecidos:

- O objetivo de cada *issue* criada deve ser único e "atômico". Para atividades com maior escopo e objetivo, recomenda-se a criação de épicos.
- Cada *issue* deve ter ao menos um *assignee* estabelecido. Este(s) se responsabilizará pela execução da mesma, ainda que de forma colaborativa.
- O título estabelecido para a *issue* deve ser simples e descritivo, visando apresentar de forma clara e sucinta o que deve ser feito.
  - Em caso de atividades mais complexas, pode-se adicionar uma descrição nos comentários da *issue* para esclarecer o que deve ser feito.
- Devem ser definidas *labels* relacionadas com o objetivo/escopo da *issue*.
- Em havendo, deve ser estabelecido o *milestone* para o qual a *issue* se relaciona.
- Ao longo do desenvolvimento da atividade da *issue*, recomenda-se que os responsáveis comentem com relação ao seu desenvolvimento nos comentários da *issue*, buscando esclarecer o que está sendo feito, dificuldades e eventuais pendências.
- Cada *issue* deverá ter um *estimate* estabelecido, preferencialmente via *planning poker*, onde um conjunto de membros (como a equipe geral responsável pela mesma para atividades mais específicas, ou então todos os membros do projeto para atividades de maior relevância) deverá estimar, através de uma pontuação definida com base na sequência de Fibonacci, o "esforço envolvido" na atividade. Alguns dos critérios para a escolha da pontuação são melhor definidos abaixo.

#### Pontuação

Os critérios para a definição da pontuação da *issue* se basearam no artigo [Story Point Estimation and Planning Poker](https://fatihyazici7.medium.com/story-point-estimation-and-planning-poker-2bf55f5bf5b2). Abaixo, os mesmos:

| **Pontuação** | **Critério geral (Esforço)** |
| :-: | :-: |
| 01 | Atividade trivial, breve, de baixo esforço |
| 02 | Atividade básica, de curta duração, com algum esforço |
| 03 | Atividade simples, duração razoável, exigindo certo esforço |
| 05 | Atividade razoável, duração um pouco maior, exigindo maior esforço |
| 08 | Atividade complexa, de grande duração, exigindo muito esforço |
| 13+ | Atividade difícil, com alta duração e alta exigência de esforço. Pode-se considerar uma eventual divisão da atividade. |

*Tabela 2: Critérios de Pontuação do Planning Poker*

### Branching

O fluxo de *branching* dos repositórios de desenvolvimento seguirá, em um escopo maior, algumas das ideias estabelecidas no [*GitFlow*](https://nvie.com/posts/a-successful-git-branching-model/) e, de maneira mais definida, o fluxo estabelecido nos [Guias de Contribuição](https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/guias/guia-contribuicao/) da equipe do semestre anterior deste projeto.

Para tal, são estabelecidas as seguintes *branches*:

| **Branch** | **Objetivo** | **Nomenclatura da Branch** |
| :-: | :-: | :-: |
| *main* | Abriga o código de produção do projeto, isto é, a versão mais estável e com garantia de funcionamento do mesmo. Todo o conteúdo a ser adicionado nesta deve originar apenas de *Pull Requests* a partir da *branch* de *qa*. | *main* |
| *qa* | Abriga o código do projeto em fase de testes e garantia da qualidade. O conteúdo a ser adicionado nesta pode ser proveniente de *pull requests* a partir das *branches* *dev* ou *fix* (para correções mais pontuais e/ou urgentes). | *qa* |
| *dev* | *Branch* destinada ao código em desenvolvimento. Pode não ser necessariamente estável. O conteúdo a ser adicionado nesta deve ser proveniente de *pull requests* a partir das *branches*  | *dev* |
| *feat* | *Branch* destinada ao desenvolvimento de funcionalidades. Devem ser associadas ao desenvolvimento de alguma funcionalidade, seguindo o proposto pela *issue* da respectiva funcionalidade. Nesta, podem ser adicionados *commits* diretamente. Esta deve se originar necessariamente a partir da *branch* *dev* e devem ser mescladas à mesma. | *feat#número-da-issue/nome-da-issue* |
| *fix* | *Branch* destinada à correção de problemas. Devem ser associadas à uma *issue* de correção/*fix*. Nesta, também podem ser adicionados *commits* diretamente. Esta deve se originar a partir das *branches* *dev* ou *qa*, sendo mescladas à *branch* de origem. | *fix#número-da-issue/nome-da-issue* |
| *doc* | *Branch* destinada à documentação. Devem ser associadas à uma *issue* de documentação. Nesta, também podem ser adicionados *commits* diretamente. | *doc#número-da-issue/nome-da-issue* |

*Tabela 3: Detalhamento das branches*

### Commiting

A política de *commiting* será inspirada no proposto pelo [*Conventional Commits*](https://www.conventionalcommits.org/pt-br/v1.0.0/#especifica%c3%a7%c3%a3o). Abaixo, um detalhamento da mesma:

#### Estrutura

Os *commits* devem seguir a estrutura abaixo:

```bash
<tipo>(#numero-da-issue): <breve descrição do conteúdo do *commit*>

[eventuais comentários, se necessário]

[eventuais coautores, caso existam]
Co-authored-by: handle_coautor <email_do_coautor@dominio.com>
```

Seguindo a possibilidade de referência à *issues* em diferentes repositórios (conforme apresentada [**AQUI**](https://github.blog/news-insights/the-library/issues-2-0-the-next-generation/)), uma alternativa para a realização de *commits* pode ser vista abaixo:

```bash
<tipo>(fga-eps-mds/2024.2-ARANDU-DOC#numero-da-issue): <breve descrição do conteúdo do *commit*>

[eventuais comentários, se necessário]

[eventuais coautores, caso existam]
Co-authored-by: handle_coautor <email_do_coautor@dominio.com>
```

#### Tipos

Os possíveis tipos para os *commits* são:

| **Tipo** | **Objetivo** |
| :-: | :-: |
| *feat* | Adiciona algum recurso/funcionalidade ao código/projeto. |
| *fix* | Corrige algum recurso/funcionalidade do código/projeto. |
| *docs* | Adiciona algum artefato à documentação. |
| *chore* | Atividade corriqueira, cotidiana, simples. |
| *style* | Adiciona algum componente de estilização ao projeto. |
| *ref* | Refatora algum recurso/funcionalidade do código/projeto. |
| *test* | Adiciona algum teste ao código/projeto. |
| *ci* | Adiciona algum recurso de *CI* ao projeto. |
| Outros | Caso o *commit* não se adeque à nenhum dos tipos supracitados, recomenda-se que tal situação seja informada aos responsáveis pelo projeto para que este guia seja incrementado. Para além, recomenda-se o uso de algum dos tipos citados no repositório do [*@commitlint/config-conventional*](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional) ou na documentação do [**Conventional Commits**](https://www.conventionalcommits.org/pt-br/v1.0.0/#especifica%c3%a7%c3%a3o) que por ventura se adeque ao tipo do *commit*.  |

*Tabela 4: Detalhamento dos tipos de commit*

#### Recomendações

Abaixo, algumas recomendações pertinentes para a realização dos *commits*:

- O título dos *commits* deve ser sucinto e auto-explicativo. Preferencialmente em português e definindo o que foi realizado naquele *commit* (exemplo: docs(#00): adiciona nova ata de reunião).
- *Commits* devem ser **atômicos**, isto é, deve conter as alterações relativas a apenas uma funcionalidade/artefato em específico.

### Pull Requests

Os *pull requests* serão utilizados para mesclar *branches* dos repositórios. Estes devem seguir o fluxo de *branching* especificado anteriormente. Todos os pull requests devem ser revisados por membro alheio ao conteúdo desenvolvido que consta nas modificações introduzidas pelo *pull request* em questão.

A estrutura descritiva dos *pull requests* será baseado no template espeficicado pela equipe do projeto no semestre anterior, conforme consta no [Guia de Contribuição](https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/guias/guia-contribuicao/) dos mesmos, para além do conteúdo descrito no artigo [*GitHub pull request template*](https://axolo.co/blog/p/part-3-github-pull-request-template).

#### Template

##### Título

```md
[TIPO] Título descritivo com o conteúdo adicionado ou modificado (#numero-da-issue)
```

Ou, alternativamente:

```md
[TIPO] Título descritivo com o conteúdo adicionado ou modificado (fga-eps-mds/2024.2-ARANDU-DOC#numero-da-issue)
```

Destaca-se que o tipo segue, majoritariamente, a tabela abaixo:

| **Tipo** | **Objetivo** |
| :-: | :-: |
| *FEATURE* | Adiciona/Modifica alguma *feature*. |
| *FIX* | Corrige algum recurso/funcionalidade do código/projeto. |
| *DOCS* | Adiciona/Modifica algum artefato de documentação. |
| *CHORE* | Adiciona alguma mudança corriqueira, cotidiana, simples. |
| *STYLE* | Adiciona/Modifica algum componente de estilização . |
| *REFACTOR* | Refatora algum recurso/funcionalidade do código/projeto. |
| *TEST* | Adiciona/Modifica algum teste do código/projeto. |
| *CI* | Adiciona/Modifica algum recurso de *CI* no projeto. |
| Outros | Caso o *pull request* não se adeque à nenhum dos tipos supracitados, recomenda-se que tal situação seja informada aos responsáveis pelo projeto para que este guia seja incrementado.  |

*Tabela 5: Detalhamento dos tipos de pull request*

##### Descrição do Pull Request

```md
# Descrição

Este *pull request* adiciona/modifica [...], conforme previsto na *issue* fga-eps-mds/2024.2-ARANDU-DOC#numero-da-issue.
```

##### Revisão das Alterações Introduzidas

```md
# Revisão

- [x] Descrição de uma das alterações introduzidas;
- [x] Descrição de outra das alterações introduzidas;
- [x] ...
```

##### Checklist

```md
# Checklist

- [x] O conteúdo adicionado nesse PR segue o código de conduta do projeto;
- [x] Foram seguidos os padrões estabelecidos no guia de contribuição;
- [x] O conteúdo adicionado foi devidamente testado;
- [x] O conteúdo do PR foi revisado por membro alheio ao mesmo;
- [x] O conteúdo deste PR foi devidamente identado, comentado e documentado;
- [x] Para conteúdos de documentação, foi adicionada tabela de versionamento aos artefatos.
```

##### Exemplo

```md
[DOCS] Adiciona Guia de Contribuição ao Projeto (fga-eps-mds/2024.2-ARANDU-DOC#22)

# Descrição

Este *pull request* adiciona o guia de contribuição ao projeto, incluindo as políticas de *issues*, *branching*, *commiting* e *pull request*, para além do código de conduta do mesmo, conforme previsto na *issue* fga-eps-mds/2024.2-ARANDU-DOC#22.

# Revisão

- [x] O **código de conduta** foi adicionado com o nome devido, no lugar devido;
- [x] Foi criado o arquivo do guia de contribuição com o nome devido, no lugar devido;
- [x] O guia de contribuição apresenta política de *issues* válida;
- [x] O guia de contribuição apresenta política de *branching* válida;
- [x] O guia de contribuição apresenta política de *commiting* válida;
- [x] O guia de contribuição apresenta política de *pull requests* válida;

# Checklist

- [x] O conteúdo adicionado nesse PR segue o código de conduta do projeto;
- [x] Foram seguidos os padrões estabelecidos no guia de contribuição;
- [x] O conteúdo adicionado foi devidamente testado;
- [x] O conteúdo do PR foi revisado por membro alheio ao mesmo;
- [x] O conteúdo deste PR foi devidamente identado, comentado e documentado;
- [x] Para conteúdos de documentação, foi adicionada tabela de versionamento aos artefatos.
```

## Fontes de Pesquisa e Referências

- [Repositório: *A-Disciplina-MDS-EPS*](https://github.com/fga-eps-mds/A-Disciplina-MDS-EPS)
- [*Contributor Covenant*](https://www.contributor-covenant.org/)
- [*Conventional Commits*](https://www.conventionalcommits.org/en/v1.0.0/)
- [Repositório: *commitlint*](https://github.com/conventional-changelog/commitlint)
- [Guia de Contribuição - GEROcuidado (2024.1)](https://fga-eps-mds.github.io/2024-1-GEROcuidado-Doc/gestaoDoProjeto/guia_contribuicao/)
- [Políticas do Repositório - Acácia (2019.2)](https://github.com/fga-eps-mds/2019.2-Acacia/blob/develop/docs/policies.md)
- [Guia de Contribuição - CALCULUS (2024.1)](https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/guias/guia-contribuicao/)
- [Tópico no *StackOverFlow*: *Link to the issue number on GitHub within a commit message*](https://stackoverflow.com/questions/1687262/link-to-the-issue-number-on-github-within-a-commit-message)
- [*GitHub Blog: Closing Issues Across Repositories*](https://github.blog/news-insights/product-news/closing-issues-across-repositories/)
- [*GitHub Blog: Issues 2.0: The Next Generation*](https://github.blog/news-insights/the-library/issues-2-0-the-next-generation/)
- [*Git branching strategy diagrams*](https://brntn.me/blog/git-branching-strategy-diagrams/)
- [*A successful Git branching model* por Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/)
- [*Planning Poker*: A melhor maneira de estimar qualquer atividade](https://metodoagil.com/planning-poker/)
- [*Story Point Estimation and Planning Poker* por Fatih YAZICI](https://fatihyazici7.medium.com/story-point-estimation-and-planning-poker-2bf55f5bf5b2)
- [*GitHub pull request template* por Arthur Coudouy](https://axolo.co/blog/p/part-3-github-pull-request-template)
