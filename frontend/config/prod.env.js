'use strict'

require('dotenv').config()
let _ = require('lodash')
let env = {}

env = _(process.env)
  .pickBy((value, key) => key.match(/^VUE_APP_/))
  .mapKeys((value, key) => key.substring('VUE_APP_'.length))
  .mapValues(value => `"${value}"`)
  .value()

module.exports = env
