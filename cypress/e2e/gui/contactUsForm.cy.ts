describe('Contact Us Form Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-contact-form');
   });

   it('should successfully submit the form', () => {
      cy.fillName('User Test');
      cy.fillEmail('user@test.com');
      cy.selectQueryType('Technical');
      cy.fillDob('2000-01-01');
      cy.checkPracticeCheckbox();
      cy.submitForm();

      cy.get('.success-message').should('have.text', 'Thanks for contacting us, we will never respond!');
   });
});