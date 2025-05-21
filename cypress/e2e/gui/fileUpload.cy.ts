describe('File Upload Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-file-upload');

      cy.window().then((win) => {
         cy.stub(win, 'alert').as('alertStub');
      });
   });

   it('should upload a file successfully', () => {
      cy.uploadFile('[data-testid=file-input]', 'example.xml');
      cy.clickButtonUpload('.file-upload button[type=submit]');
      cy.verifyAlert('File successfully uploaded!');
   });
});