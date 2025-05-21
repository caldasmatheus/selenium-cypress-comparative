declare namespace Cypress {
   interface Chainable<Subject = any> {
      visitPracticePage(page: string): Chainable<void>;
      clickAccordionButton(accordionText: string): Chainable<void>;
      verifyElementText(selector: string, expectedText: string): Chainable<void>;
      performClickAction(selector: string): Chainable<void>;
      performDoubleClickAction(selector: string): Chainable<void>;
      performRightClickAction(selector: string): Chainable<void>;
      checkOption(selector: string): Chainable<void>;
   }
}