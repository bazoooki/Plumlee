
import Vue from 'vue'
import Vuex from 'vuex'
import api from './modules/api'

Vue.use(Vuex)

const createStore = () => {
  return new Vuex.Store({
    modules: { api }
    // plugins: process.env.NODE_ENV !== 'production'
    //   ? [createLogger()]
    //   : []
  })
}

export default createStore()
