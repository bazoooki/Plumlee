var merge = require('webpack-merge')
var prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  api: JSON.stringify({
    // BASE_URL: 'https://v2api.biggercake.com/api/'
    BASE_URL: 'http://localhost:8000/api/'
  })
})
