Cypress.Commands.add('visitPracticePage', (page: string) => {
   cy.visit(`/${page}`);
});

// accordions_commands.ts
Cypress.Commands.add('clickAccordionButton', (accordionText: string) => {
   cy.contains('button', accordionText).click();
});

Cypress.Commands.add('verifyElementText', (selector: string, expectedText: string) => {
   cy.get(selector).should('have.text', expectedText);
});

Cypress.Commands.add('performClickAction', (selector: string) => {
   cy.get(selector).click();
});

Cypress.Commands.add('performDoubleClickAction', (selector: string) => {
   cy.get(selector).dblclick();
});

Cypress.Commands.add('performRightClickAction', (selector: string) => {
   cy.get(selector).rightclick();
});

Cypress.Commands.add('checkOption', (selector: string) => {
   cy.get(selector).check();
});

// apis_commands.ts
Cypress.Commands.add('waitForApiResponse', (url: string, alias: string) => {
   cy.intercept(url).as(alias);
});

Cypress.Commands.add('verifyApiStatusCode', (alias: string, expectedStatusCode: number) => {
   cy.wait(`@${alias}`).then((interception) => {
      expect(interception.response).to.have.property('statusCode', expectedStatusCode);
   });
});

Cypress.Commands.add('verifyApiResponseBody', (alias: string, expectedBody: object) => {
   cy.wait(`@${alias}`).then((interception) => {
      if (interception.response) {
         const responseBody = interception.response.body;
         expect(responseBody).to.deep.equal(expectedBody);
      } else {
         throw new Error(`Resposta não recebida para o alias ${alias}`);
      }
   });
});

// contact_form_commands.ts
Cypress.Commands.add('fillName', (name: string) => {
   cy.get('[data-testid=name]').type(name);
});

Cypress.Commands.add('fillEmail', (email: string) => {
   cy.get('[data-testid=email]').type(email);
});

Cypress.Commands.add('selectQueryType', (type: string) => {
   cy.get('[data-testid=query-type]').select(type);
});

Cypress.Commands.add('fillDob', (dob: string) => {
   cy.get('[data-testid=dob]').type(dob);
});

Cypress.Commands.add('checkPracticeCheckbox', () => {
   cy.get('[data-testid=practice-checkbox]').click();
});

Cypress.Commands.add('submitForm', () => {
   cy.get('[data-testid=submit-button]').click();
});

// drag_and_drop_commands.ts
Cypress.Commands.add('dragAndDrop', (dragSelector: string, dropSelector: string) => {
   cy.get(dragSelector).then($source => {
      cy.get(dropSelector).then($target => {
         const dataTransfer = new DataTransfer();

         cy.wrap($source)
            .trigger('dragstart', { dataTransfer })
            .trigger('drag', {});

         cy.wrap($target)
            .trigger('dragenter', { dataTransfer })
            .trigger('dragover', { dataTransfer })
            .trigger('drop', { dataTransfer })
            .trigger('dragend', { dataTransfer });
      });
   });
});

// dynamic_text_commands.ts
Cypress.Commands.add('clickButton', (testId: string) => {
   cy.get(`[data-testid=${testId}]`).click();
});

Cypress.Commands.add('verifyButtonText', (testId: string, expectedText: string, timeout: number = 5000) => {
   cy.get(`[data-testid=${testId}]`, { timeout }).should('have.text', expectedText);
});

// file_upload_commands.ts
Cypress.Commands.add('uploadFile', (selector: string, fileName: string) => {
   cy.get(selector).attachFile(fileName);
});

Cypress.Commands.add('clickButtonUpload', (selector: string) => {
   cy.get(selector).click();
});

Cypress.Commands.add('verifyAlert', (expectedMessage: string) => {
   cy.get('@alertStub').should('have.been.calledOnceWith', expectedMessage);
});

// general_components_commands.ts
Cypress.Commands.add('clickElement', (selector: string) => {
   cy.get(selector).click();
});

Cypress.Commands.add('doubleClickElement', (selector: string) => {
   cy.get(selector).dblclick();
});

Cypress.Commands.add('rightClickElement', (selector: string) => {
   cy.get(selector).rightclick();
});

Cypress.Commands.add('checkOption', (selector: string) => {
   cy.get(selector).check();
});

Cypress.Commands.add('selectOption', (selector: string, value: string) => {
   cy.get(selector).select(value);
});

Cypress.Commands.add('shouldHaveValue', (selector: string, expectedValue: string) => {
   cy.get(selector).should('have.value', expectedValue);
});

Cypress.Commands.add('verifySucceedText', (selector: string, expectedText: string) => {
   cy.get(selector).should('have.text', expectedText);
});