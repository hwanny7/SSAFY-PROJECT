import Vue from 'vue'
import Vuex from 'vuex'
import login from '@/store/modules/login.js'
import collection from '@/store/modules/collection.js'
import createPersistedState from 'vuex-persistedstate' // locali storage 에 저장



const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)
import axios from 'axios'

export default new Vuex.Store({
  state: {
    like_movies : Array,
    hate_movies : Array,
    all_movies : Array,
    detail_movie: Object,
    all_reviews : Array,
    recommend_movies : Array,
    upcoming_movies: Array,
  },
  getters: {
    GET_LIKE_MOIVES: (state) => state.like_movies,
    GET_HATE_MOVIES: (state) => state.hate_movies,
    GET_ALL_MOVIES: (state) => state.all_movies,
    GET_DETAIL_MOVIE: (state) => state.detail_movie,
    GET_ALL_REVIEWS: (state) => state.all_reviews,
    GET_REOCOMMEND_MOVIES : (state) => state.recommend_movies,
    GET_UPCOMING_MOVIES : (state) => state.upcoming_movies
  },
  mutations: {
    LIKEMOVIES(state, movies) {
      if (movies[0] != '없음') {
        state.like_movies = movies
      } else {
        state.like_movies = []
      }
    },
    HATEMOVIES(state, movies) {
      if (movies[0] != '없음') {
        state.hate_movies = movies
      } else {
        state.hate_movies = []
      }
      
    },
    ALLMOVIES(state, movies) {
      state.all_movies = movies
    },
    DETAILMOVIE(state, movie){
      state.detail_movie = movie
    },
    ALLREVIEWS(state, review) {
      state.all_reviews = review
    },
    RECOMMENDMOVIES(state, movies) {
      state.recommend_movies = movies
    },
    UPCOMINGMOVIE(state,movies) {
      state.upcoming_movies = movies
    }
  },
  actions: {
    getLikeMovie(context,data){
      axios({
        url: `${API_URL}/movies/${data.userPk}/${data.url}`,
        method: 'get',
      })
        .then(res => {
          if (data.url === 'like') {
            context.commit('LIKEMOVIES', res.data)
          } else {
            context.commit('HATEMOVIES', res.data)
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    getAllMovie(context){
      axios({
        url: `${API_URL}/movies/select/`,
        method: 'get',
      })
        .then(res => {
          context.commit('ALLMOVIES', res.data)
        })
        .catch(err => {
          console.log(err)
        })

    },
    getDetailMovie(context,movie_pk){
      axios({
        url: `${API_URL}/movies/${movie_pk}/moviedetail/`,
        method: 'get',
      })
        .then(res => {
          context.commit('DETAILMOVIE', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    postLikeMovie(context, info){
      axios({
        url: `${API_URL}/movies/${info.userPk}/${info.url}/`,
        method: 'post',
        data: {
          'movie': info.moviePk
        }
      })
        .then(res => {
          const info1 = {
            'userPk' : info.userPk,
            'url': 'like',
          }
          const info2 = {
            'userPk' : info.userPk,
            'url': 'hate',
          }
          context.dispatch('getLikeMovie', info1)
          context.dispatch('getLikeMovie', info2)
          res
        })
        .catch(err => {
          console.log(err)
        })
    },
    getReview(context, movie_pk){
      axios({
        url: `${API_URL}/movies/${movie_pk}/review_create/`,
        method: 'get',
      })
        .then(res => {
          context.commit('ALLREVIEWS',res.data)
        })
    },
    postReview(context, info){
      
      axios({
        url: `${API_URL}/movies/${info.movie_pk}/review_create/`,
        method: 'post',
        headers: info.authHead,
        data: {
          'content': info.content,
          'vote': info.vote
        }
      })
        .then(res => {
          res
          context.dispatch('getReview', info.movie_pk)
          return
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReview(context, info){
      axios({
        url: `${API_URL}/movies/${info.review_id}/review_update/`,
        method: 'delete',
        headers: info.headers,
      })
        .then(res => {
          res
          context.dispatch('getReview', info.movie_pk)
          return
        })
        .catch(err => {
          console.log(err)
        })
    },
    blockReview(context, info){
      axios({
        url: `${API_URL}/movies/${info.review_id}/review_block/`,
        method: 'post',
        headers: info.headers,
      })
        .then(res => {
          res
          context.dispatch('getReview', info.movie_pk)
          return
        })
        .catch(err => {
          console.log(err)
        })
    },
    getRecommendMovie(context,headers){
      context
      axios({
        url: `${API_URL}/movies/recommend/`,
        method : 'get',
        headers: headers,
      })
        .then (res => {
          context.commit('RECOMMENDMOVIES', res.data)
        })
        .catch (err => {
          console.log(err.data)
        })
    },
    getUpcomingMovie(context){
      context
      axios({
        url: `${API_URL}/movies/upcoming/`,
        method: 'get'
      })
        .then(res => {
          context.commit('UPCOMINGMOVIE', res.data)
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
