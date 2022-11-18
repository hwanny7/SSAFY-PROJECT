import Vue from 'vue'
import Vuex from 'vuex'
import login from '@/store/modules/login.js'
import collection from '@/store/modules/collection.js'




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
  }
})
