<template>
  <div>
    <!-- {{ GET_ALL_MOVIES }} -->
    <h1>MovieList</h1>
    <select class="form-select" aria-label="Default select example1" v-model="genre">
      <option value="all">ALL</option>
      <option 
      v-for="genre in genres"
      :key="genre.id"
      :value="genre.id">{{ genre.name }}</option>
    </select>

    <div>
      <button @click="beforeMovie">-</button>
      <button @click="afterMovie">+</button>
    </div>

    <span 
    v-for="mmovie in movieSlice"
    :key="mmovie.id">
      <img :src="'https://themoviedb.org/t/p/original'+mmovie.poster_path" alt="" 
      style="width: 100px; height: 100px" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"
      @click="movieDetail(mmovie.id)"
      >
    </span>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
  name: 'ALLMovieList',
  components: {},
  props:{
    userPk: Number,
  },
  data() {
    return {
      genre: 'all',
      movieNum: 0,
    }
  },
  methods: {
    beforeMovie() {
      if ((this.movieNum) > 1 ){
        this.movieNum -= 15
      }
    },
    afterMovie() {
      if (this.movieNum+15 < this.GET_ALL_MOVIES.length){
        this.movieNum += 15
      }
    },
    movieDetail(movie_pk) {
      this.$store.dispatch('getDetailMovie', movie_pk)
      this.$store.dispatch('getReview', movie_pk)
    },
  },
  computed: {
    ...mapGetters(['GET_ALL_MOVIES', 'GET_GENRES']),
    ...mapGetters('login' ,['user','authHead']),
    movieModal() {
      return this.GET_DETAIL_MOVIE
    },
    genreMovie() {
      return this.GET_ALL_MOVIES.filter(movie => {
        if (this.genre === 'all') {
          return true
        }
        let flag = false
        // console.log(movie.genres)
        movie.genres.forEach(genre => {
          if (genre.id === this.genre) {
            flag = true
            return
          }
        })
        return flag
      })
    },
    movieSlice() {
      return this.genreMovie.slice(this.movieNum, this.movieNum + 15)
    },
    genres() {
      return this.GET_GENRES
    }
  },
}
</script>

<style>

</style>

