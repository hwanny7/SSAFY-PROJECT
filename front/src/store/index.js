import Vue from 'vue'
import Vuex from 'vuex'
import login from '@/store/modules/login.js'
import collection from '@/store/modules/collection.js'
import createPersistedState from 'vuex-persistedstate' // locali storage 에 저장




Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    login: login,
    collection: collection,
  },
  plugins: [
    createPersistedState(),
  ]
})
