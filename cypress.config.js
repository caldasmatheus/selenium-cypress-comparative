import { defineConfig } from 'cypress'

export default defineConfig({
   hideXHRInCommandLog: true,
   chromeWebSecurity: false,
   e2e: {
      viewportWidth: 1920,
      viewportHeight: 1080,
      baseUrl: 'https://commitquality.com',

      setupNodeEvents(on, config) {
         return config
      },
   },
})