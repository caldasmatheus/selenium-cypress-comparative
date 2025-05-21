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