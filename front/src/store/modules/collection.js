import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

const collection = {
  namespaced: true,
  state: {
    myCollections: Array,
    MoviePick: Array,
    allCollections: Array,
    comments: Object,
    backImg: String,
  },
  getters: {
    getMyCollections: (state) => state.myCollections,
    getAllCollections: (state) => state.allCollections,
    getMoviePick: (state) => state.MoviePick, 
    getComments: (state) => state.comments,
    getBackImg: (state) => state.backImg,
  },
  mutations: {
    MY_COLLECTIONS(state, res) {
        state.myCollections = res
    },
    ALL_COLLECTIONS(state, res) {
        state.allCollections = res
    },
    CREATE_COLLECTION(state, res) {
        state.MoviePick = res
    },
    GET_COMMENTS(state, payload) {
      state.comments = {...state.comments, ...payload}
    },
    BACK_GROUND(state, url) {
      state.backImg = url
    }
  },
  actions: {
    myCollections({commit}, id) {
        axios({
          url: `${API_URL}/collects/mycollection/${id}/`,
          method: 'get',
          // headers: authHead,
        })
          .then(res => {
            commit('MY_COLLECTIONS', res.data)
            console.log('hi')
          })
          .catch(err => {
            console.log(err)
          })
      },
    AllCollections({commit}, authHead) {
        axios({
          url: `${API_URL}/collects/collection/`,
          method: 'get',
          headers: authHead,
        })
          .then(res => {
            commit('ALL_COLLECTIONS', res.data)
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
    },
    DeleteCollection({dispatch}, payload) {
      axios({
        url: `${API_URL}/collects/update/${payload.id}/`,
        method: 'delete',
        headers: payload.authHead
      })
        .then(res => {
          dispatch('myCollections', payload.user_id)
          console.log(res)
        })
    },
    getComments({commit}, collection_pk) {
      console.log('hi')
      axios({
        url: `${API_URL}/collects/review/${collection_pk}/`,
        method: 'get',
      })
        .then(res => {
          const pk = collection_pk
          const payload = {
            [pk] : res.data
          }
          commit('GET_COMMENTS', payload)
        })  
    },
    actionCreate({dispatch}, payload) {
      axios({
        url: `${API_URL}/collects/review/create/`,
        method: 'POST',
        headers: payload.headers,
        data: {
          "content": payload.content,
          "collection_pk": payload.collection_pk
        }
      })
        .then(res => {
          console.log(res)
          dispatch('getComments', payload.collection_pk)
        })  
    },
    actionDelete({dispatch}, payload) {
      axios({
        url: `${API_URL}/collects/review/delete/${payload.comment_pk}/`,
        method: 'delete',
        headers: payload.headers,
      })
        .then(res => {
          console.log(res)
          dispatch('getComments', payload.collection_pk)
        })  
    },
    backGround({commit}, URL) {
      commit('BACK_GROUND', URL)
    },
    likeCol({dispatch}, payload) {
      axios({
        url: `${API_URL}/collects/like/`,
        method: 'post',
        headers: payload.headers,
        data: {
          collection_pk: payload.collection_pk
        }
      })
        .then(res => {
          console.log(res)
          dispatch('AllCollections', payload.headers)
        })  
    },
    likeColpro({dispatch}, payload) {
      axios({
        url: `${API_URL}/collects/like/`,
        method: 'post',
        headers: payload.headers,
        data: {
          collection_pk: payload.collection_pk
        }
      })
        .then(res => {
          console.log(res)
          dispatch('myCollections', payload.id)
        })  
    }
  }
}

export default collection

