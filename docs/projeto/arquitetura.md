# Documentação de Arquitetura

## Versionamento

| **Versão** | **Data** | **Modificação** | **Responsável** |
| :-: | :-: | :-: | :-: |
| 0.1 | 09/12/24 | Criação do documento | Gabriel Mariano |

*Tabela 1: Versionamento*

---

## Objetivo

A documentação de arquitetura visa apresentar uma visão técnica da estutura organizacional do produto de software a ser desenvolvido, apresentando elementos como o *stack* da aplicação, a organização dos serviços, a estrutura da camada de persistência, os *endpoints* definidos e também instruções para a execução do projeto.

## Stack

Foram definidas as seguintes tecnologias para o projeto:

| **Tecnologia** | **Serviço (s)** | **Objetivo** |
| :-: | :-: | :-: |
| *NestJs* | UserService e StudioMaker | Back-End do Sistema |
| *NextJs* | FrontEnd | Front-End do Sistema |
| *Flutter* | APP | Aplicativo Móvel |
| *Swagger* | UserService e StudioMaker | Documentação das Rotas do Back-End |
| *Docker* | UserService, StudioMaker e FrontEnd | Conteinerização da Aplicação |

*Tabela 2: Stack do Sistema*

## Deploy

O *deploy* da aplicação foi realizado na plataforma **Render** e pode ser encontrado [NESSE LINK](https://arandu.onrender.com/).

## Documentação Anterior

Por se tratar de um sistema legado de outra equipe de desenvolvimento, uma documentação prévia da arquitetura do sistema pode ser encontrada na [Documentação de Arquitetura do Projeto Calculus 2024-1](https://fga-eps-mds.github.io/2024.1-CALCULUS-DOC/organizacoes/documento_arquitetura/).
