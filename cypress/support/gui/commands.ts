Cypress.Commands.add('visitPracticePage', (page: string) => {
   cy.visit(`/${page}`);
});

// accordions_commands.ts
Cypress.Commands.add('clickAccordionButton', (accordionText: string) => {
   cy.contains('button', accordionText).click();
});

Cypress.Commands.add('verifyElementText', (selector: string, expectedText: string) => {
   cy.get(selector).should('have.text', expectedText);
});

Cypress.Commands.add('performClickAction', (selector: string) => {
   cy.get(selector).click();
});

Cypress.Commands.add('performDoubleClickAction', (selector: string) => {
   cy.get(selector).dblclick();
});

Cypress.Commands.add('performRightClickAction', (selector: string) => {
   cy.get(selector).rightclick();
});

Cypress.Commands.add('checkOption', (selector: string) => {
   cy.get(selector).check();
});

// apis_commands.ts
Cypress.Commands.add('waitForApiResponse', (url: string, alias: string) => {
   cy.intercept(url).as(alias);
});

Cypress.Commands.add('verifyApiStatusCode', (alias: string, expectedStatusCode: number) => {
   cy.wait(`@${alias}`).then((interception) => {
      expect(interception.response).to.have.property('statusCode', expectedStatusCode);
   });
});

Cypress.Commands.add('verifyApiResponseBody', (alias: string, expectedBody: object) => {
   cy.wait(`@${alias}`).then((interception) => {
      if (interception.response) {
         const responseBody = interception.response.body;
         expect(responseBody).to.deep.equal(expectedBody);
      } else {
         throw new Error(`Resposta não recebida para o alias ${alias}`);
      }
   });
});