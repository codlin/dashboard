import Vue from 'vue'
import Vuex from 'vuex'
import breadcrums from './modules/breadcrums'
import createLogger from 'vuex/dist/logger'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const store = new Vuex.Store({
  modules: {
    breadcrums
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})

export default store
