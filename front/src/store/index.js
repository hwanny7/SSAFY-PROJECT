import Vue from 'vue'
import Vuex, { mapGetters } from 'vuex'
import login from '@/store/modules/login.js'
import collection from '@/store/modules/collection.js'
import createPersistedState from 'vuex-persistedstate' // locali storage 에 저장




Vue.use(Vuex)
import axios from 'axios'

export default new Vuex.Store({
  state: {

  },
  getters: {
    
  },
  mutations: {
    LIKEMOVIE () {

    },

  },
  actions: {
    getLikeMovie(context, ahead){
      axios({
        url: 'http://127.0.0.1:8000/like/',
        method: 'get',
       context.authHead,
      })
        .then(res => {
          console.log()
          context.commit('LIKEMOVIE', res.data)
        })
        .catch(err => {
          console.log(err)
        })
        
    }
      
  },
  modules: {
    login: login,
    collection: collection,
  },
  plugins: [
    createPersistedState(),
  ]
})
