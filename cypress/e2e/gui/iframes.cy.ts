describe('Iframe Interaction Tests', () => {
   beforeEach(() => {
      cy.visit('/practice-iframe');
   });

   it('should click on element inside an iframe', () => {
      cy.get('h2').should('have.text', 'IFrame');

      cy.getIframeBody('[data-testid=iframe]')
         .find('[data-testid=navbar-addproduct]')
         .click();

      cy.getIframeBody('[data-testid=iframe]')
         .find('h1')
         .should('have.text', 'Add Product');

      cy.get('h2').should('have.text', 'IFrame');
   });
});