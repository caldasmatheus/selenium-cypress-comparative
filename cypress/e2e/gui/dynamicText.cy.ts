describe('Dynamic Text Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-dyanmic-text');
   });

   it('should wait for button to change its text', () => {
      cy.clickButton('dynamic-button1');
      cy.verifyButtonText('dynamic-button1', 'loading', 2000); // aguarda até 2 segundos
      cy.verifyButtonText('dynamic-button1', 'I am visible after 5 seconds', 10000); // até 10 segundos
   });
});