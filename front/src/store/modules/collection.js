import axios from 'axios'


const API_URL = 'http://127.0.0.1:8000'

const collection = {
  namespaced: true,
  state: {
    myCollections: Array,
    MoviePick: Array,
  },
  getters: {
    getMyCollections: (state) => state.myCollections,
    getMoviePick: (state) => state.MoviePick
  },
  mutations: {
    MY_COLLECTIONS(state, res) {
        state.myCollections = res
    },
    CREATE_COLLECTION(state, res) {
        state.MoviePick = res
    }
  },
  actions: {
    myCollections({commit}, authHead) {
        axios({
          url: `${API_URL}/collects/collection/`,
          method: 'get',
          headers: authHead,
        })
          .then(res => {
            commit('MY_COLLECTIONS', res.data)
          })
          .catch(err => {
            console.log(err)
          })
      },
    CreateCollection({commit}, authHead) {
        axios({
          url: `${API_URL}/movies/select/`,
          method: 'get',
          headers: authHead,
        })
          .then(res => {
            console.log(res)
            commit('CREATE_COLLECTION', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
}

export default collection

