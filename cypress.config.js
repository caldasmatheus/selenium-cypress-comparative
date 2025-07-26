import { defineConfig } from 'cypress'
import allureWriter from '@shelex/cypress-allure-plugin/writer'

export default defineConfig({
   hideXHRInCommandLog: true,
   chromeWebSecurity: false,
   e2e: {
      viewportWidth: 1920,
      viewportHeight: 1080,
      baseUrl: 'https://commitquality.com',
      env: {
         allure: true,
         allureResultsPath: 'allure-results',
      },

      setupNodeEvents(on, config) {
         allureWriter(on, config)
         return config
      },
   },
})