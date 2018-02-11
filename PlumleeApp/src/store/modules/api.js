import api from '@/api' // Not this module, but the api at parent
// import Vue from 'vue'
// import { filter } from 'lodash'
// const LOGIN = 'LOGIN'
// import router from '../../router'
const USER = 'USER'
const state = {
  user: null
}

const actions = {
  getUser ({ state, commit, dispatch }, id) {
    return api.getUser(id).then(user => {
      commit(USER, user)
      return user
    }).catch((err) => {
      if (err.response.status === 401) {
        dispatch('logout')
      }
    })
  },
  pullPlayers ({ commit }) {
    return api.pullPlayers()
  },
  login ({ state, commit, dispatch }, data) {
    return api.login(data).then(user => {
      commit(USER, user)
      return user
    }).catch((err) => {
      if (err.response.status === 401) {
        dispatch('logout')
      }
    })
  },
  register ({ commit }, data) {
    return api.register(data).then((response) => {
      if (response.data.status === 0) {
        // Error
        return response.data
      } else {
        let user = response.data.user
        commit(USER, user)
        return user
      }
    })
  },
  whoami ({ commit }) {
    return api.whoami()
  }
}

const mutations = {
  [USER] (state, user) {
    state.user = user
  }
}

const getters = {
  user: state => state.user
}

export default {
  state, actions, mutations, getters
}
