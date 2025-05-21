describe('Accordions Tests', () => {
   beforeEach(() => {
      cy.visitPracticePage('practice-accordions');
   });

   it('should test basic click button inside accordion', () => {
      cy.clickAccordionButton('Accordion 1');
      cy.performClickAction('[data-testid=basic-click]');
      cy.verifyElementText('[data-testid=basic-click]+p', 'Button clicked');
   });

   it('should test double click button inside accordion', () => {
      cy.clickAccordionButton('Accordion 1');
      cy.performDoubleClickAction('[data-testid=double-click]');
      cy.verifyElementText('[data-testid=double-click]+p', 'Button double clicked');
   });

   it('should test right click button inside accordion', () => {
      cy.clickAccordionButton('Accordion 1');
      cy.performRightClickAction('[data-testid=right-click]');
      cy.verifyElementText('[data-testid=right-click]+p', 'Button right mouse clicked');
   });

   it('should test click radio buttons inside accordion', () => {
      cy.clickAccordionButton('Accordion 2');
      cy.checkOption('[data-testid=option1]');
      cy.verifyElementText('.component-container > p', 'option1 clicked');
      cy.checkOption('[data-testid=option2]');
      cy.verifyElementText('.component-container > p', 'option2 clicked');
   });

   it('should test click checkboxes inside accordion', () => {
      cy.clickAccordionButton('Accordion 3');
      cy.checkOption('[data-testid=checkbox1]');
      cy.verifyElementText('.checkbox-container:nth-child(1) p', 'Checkbox 1 checked');
      cy.checkOption('[data-testid=checkbox2]');
      cy.verifyElementText('.checkbox-container:nth-child(2) p', 'Checkbox 2 checked');
      cy.checkOption('[data-testid=checkbox3]');
      cy.verifyElementText('.checkbox-container:nth-child(3) p', 'Checkbox 3 checked');
   });
});