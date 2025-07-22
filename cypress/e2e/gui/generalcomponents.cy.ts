import 'cypress-wait-until';

describe('General Components Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-general-components');
   });

   it('should handle basic click button', () => {
      cy.clickElement('[data-testid=basic-click]');
      cy.verifySucceedText('[data-testid=basic-click]+p', 'Button clicked');
   });

   it('should handle double click button', () => {
      cy.doubleClickElement('[data-testid=double-click]');
      cy.verifySucceedText('[data-testid=double-click]+p', 'Button double clicked');
   });

   it('should handle right click button', () => {
      cy.rightClickElement('[data-testid=right-click]');
      cy.verifySucceedText('[data-testid=right-click]+p', 'Button right mouse clicked');
   });

   it('should handle radio buttons', () => {
      cy.checkOption('[data-testid=option1]');
      cy.get('.radio-buttons-container p').should('have.text', 'option1 clicked');
      cy.checkOption('[data-testid=option2]');
      cy.get('.radio-buttons-container p').should('have.text', 'option2 clicked');
   });

   it('should handle select options', () => {
      cy.selectOption('[data-testid=dropdown] > select', 'Option 1');
      cy.shouldHaveValue('[data-testid=dropdown] > select', 'option1');

      cy.selectOption('[data-testid=dropdown] > select', 'Option 2');
      cy.shouldHaveValue('[data-testid=dropdown] > select', 'option2');

      cy.selectOption('[data-testid=dropdown] > select', 'Option 3');
      cy.shouldHaveValue('[data-testid=dropdown] > select', 'option3');
   });

   it('should handle checkboxes', () => {
      cy.checkOption('[data-testid=checkbox1]');
      cy.get('.checkbox-container:nth-child(1) p').should('have.text', 'Checkbox 1 checked');

      cy.checkOption('[data-testid=checkbox2]');
      cy.get('.checkbox-container:nth-child(2) p').should('have.text', 'Checkbox 2 checked');

      cy.checkOption('[data-testid=checkbox3]');
      cy.get('.checkbox-container:nth-child(3) p').should('have.text', 'Checkbox 3 checked');
   });

   it('should navigate to different domain', () => {
      cy.get('[data-testid=link-same-tab]').then($link => {
         $link.removeAttr('target');
      }).click();

      cy.url().should('include', 'https://www.youtube.com/@commitquality');
   });

   it('should open popup on different domain', () => {
      cy.window().then((win) => {
         cy.stub(win, 'open').as('windowOpen');
      });

      cy.clickElement('[data-testid=link-newtab]')
         .should('have.attr', 'href')
         .and('include', 'https://www.youtube.com/@commitquality');

      cy.get('[data-testid=link-newtab]').then($link => {
         $link.removeAttr('target');
      }).click();

      cy.url().should('include', 'https://www.youtube.com/@commitquality');
   });

   it('should open popup on same domain', () => {
      cy.window().then((win) => {
         cy.stub(win, 'open').as('windowOpen');
      });

      cy.clickElement('[data-testid=link-newtab-practice]')
         .should('have.attr', 'href')
         .and('include', '/practice');

      cy.get('[data-testid=link-newtab-practice]').then($link => {
         $link.removeAttr('target');
      }).click();

      cy.url().should('include', Cypress.config().baseUrl + '/practice');
   });
});