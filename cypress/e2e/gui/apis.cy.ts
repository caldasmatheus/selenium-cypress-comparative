describe('APIs Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-api');
   });

   it('should capture API response', () => {
      cy.intercept({ method: 'GET', url: '**/todos/1' }).as('getTodo');

      cy.get('[data-testid=get-button]').click();

      cy.wait('@getTodo').then((interception) => {
         expect(interception.response).to.have.property('statusCode', 200);
         const responseBody = interception.response?.body;
         const expectedBody = {
            userId: 1,
            id: 1,
            title: "delectus aut autem",
            completed: false
         };
         expect(responseBody).to.deep.equal(expectedBody);
         cy.get('.api-container > p').should('have.text', `Status Code: 200`);
         cy.get('.api-container > pre').should('have.text', JSON.stringify(expectedBody, null, 2));
      });
   });
});