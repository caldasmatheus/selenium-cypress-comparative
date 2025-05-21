describe('Drag and Drop Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-drag-and-drop');
   });

   it('should drag and drop elements', () => {
      cy.dragAndDrop('[data-testid=small-box]', '[data-testid=large-box]');
      cy.get('[data-testid=large-box]').should('have.text', 'Success!');
   });
});