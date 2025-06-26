# selenium-cypress-comparative-web-test

### Descrição

Este projeto contém o código responsável por testar funcionalmente o site [@CommitQuality](https://commitquality.com).

- [Allure 2.13.5](https://allurereport.org)
- [Cypress 14.0.3](https://docs.cypress.io/app/get-started/why-cypress)
- [TypeScript 5.7.3](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
- [Node v22.14.0](https://nodejs.org/pt)

### Clone e Execução do projeto

Para clonar o projeto siga os seguintes passos:

No terminal:
```
git clone git@github.com:caldasmatheus/selenium-cypress-comparative.git
```

No contexto onde o projeto foi clonado:
```
cd selenium-cypress-comparative
```

Mude para branch do selenium:
```
git checkout cypress
```

Na raiz do projeto:
```
npm i
```

:exclamation: **Observação**: Para questões relacionadas a autenticação por SSH, consulte a documentação do GitHub em "[Crie e Adicione seu Par de Chaves SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh)".

### Tipos de Execução dos Testes

Para executar o projeto **selenium-cypress-comparative** siga as etapas:

* Exemplo de execução dos testes no modo Interativo, abra o terminal no VS Code e execute o comando:

```
npx cypress open
```

* Exemplo de execução dos testes no modo Headless, abra o terminal e execute o comando:

```
npx cypress run
```

* Exemplo de execução dos testes no modo Headless e gerar allure-results, abra o terminal e execute o comando:

```
npx cypress run
npx allure generate allure-results --clean -o allure-report
npx allure open allure-report
```

### Contribuições

Para contribuir com o projeto, siga estas etapas:

1. Crie um *branch*: *`git checkout -b <branch_name>`*;
2. Faça suas alterações e confirme-as: *`git commit -m '<commit_message>'`*;
3. Envie a *branch* local para o repositório remoto: *`git push origin <branch_name>`*;
4. Crie o *pull request*.

:exclamation: **Observação**: Como alternativa, consulte a documentação do GitHub em "[Criando um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)".

### Contato

Em caso de dúvidas: <raimundo.matheus@dcx.ufpb.br>. :incoming_envelope: