declare namespace Cypress {
   interface Chainable<Subject = any> {
      visitPracticePage(page: string): Chainable<void>;
      clickAccordionButton(accordionText: string): Chainable<void>;
      verifyElementText(selector: string, expectedText: string): Chainable<void>;
      performClickAction(selector: string): Chainable<void>;
      performDoubleClickAction(selector: string): Chainable<void>;
      performRightClickAction(selector: string): Chainable<void>;
      checkOption(selector: string): Chainable<void>;
      waitForApiResponse(url: string, alias: string): Chainable<void>;
      verifyApiStatusCode(alias: string, expectedStatusCode: number): Chainable<void>;
      verifyApiResponseBody(alias: string, expectedBody: object): Chainable<void>;
      fillName(name: string): Chainable<void>;
      fillEmail(email: string): Chainable<void>;
      selectQueryType(queryType: string): Chainable<void>;
      fillDob(dob: string): Chainable<void>;
      checkPracticeCheckbox(): Chainable<void>;
      submitForm(): Chainable<void>;
      dragAndDrop(source: string, target: string): Chainable<void>;
   }
}