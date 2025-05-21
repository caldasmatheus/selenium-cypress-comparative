// eslint.config.js
import { defineConfig } from 'eslint-define-config'

// Configuração base do ESLint (recomendado)
const eslintRecommended = {
   languageOptions: {
      globals: {
         browser: true,
         commonjs: true,
         node: true,
      },
      parserOptions: {
         ecmaVersion: 12,
      },
   },
   rules: {
      indent: ['error', 3],
      'linebreak-style': 'off',
      quotes: ['error', 'single'],
      semi: ['error', 'never'],
      'no-trailing-spaces': ['error'],
   },
}

// Configuração do plugin Cypress (recomendado)
const cypressConfig = {
   languageOptions: {
      globals: {
         cy: true,
         Cypress: true,
      },
   },
}

export default defineConfig([
   eslintRecommended,  // Configurações recomendadas do ESLint
   cypressConfig,      // Configurações do plugin Cypress
   {
      // Outras regras ou configurações específicas
      files: ['*.js', '*.ts'],
      rules: {
         // Defina regras específicas para esses arquivos se necessário
      },
   },
])