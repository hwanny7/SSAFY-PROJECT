<template>
  <div>
    <select class="form-select" aria-label="Default select example1" v-model="genre">
      <option value="None">None</option>
      <option value="all">ALL</option>
      <option 
      v-for="genre in genres"
      :key="genre.id"
      :value="genre.id">{{ genre.name }}</option>
    </select>

    <div class="mt-3">
      <button class="btn btn-secondary mx-1" @click="beforeMovie">이전 페이지</button>
      <button class="btn btn-secondary mx-1" @click="afterMovie">다음 페이지</button>
    </div>

    <div class ="d-flex flex-row justify-content-center flex-wrap">
      <div class="card rounded d-flex justify-content-center align-items-center m-2 radius sample_image" style="width: 12rem;"
      v-for="mmovie in movieSlice"
      :key="mmovie.id">
        <img :src="'https://themoviedb.org/t/p/original'+mmovie.poster_path" alt="" 
        type="button" data-bs-toggle="modal" data-bs-target="#exampleModal" class="card-img-top" style="height: 300px;"
        @click="movieDetail(mmovie.id)"
        >
      </div>
    </div>
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
      genre: 'None',
      movieNum: 0,
    }
  },
  methods: {
    beforeMovie() {
      if ((this.movieNum) > 1 ){
        this.movieNum -= 12
      }
    },
    afterMovie() {
      if (this.movieNum+12 < this.genreMovie.length){
        this.movieNum += 12
      }
    },
    movieDetail(movie_pk) {
      this.$store.dispatch('getDetailMovie', movie_pk)
      this.$store.dispatch('getReview', movie_pk)
    },
  },
  computed: {
    ...mapGetters('collection', ['getMoviePick',]),
    ...mapGetters(['GET_GENRES']),
    ...mapGetters('login' ,['user','authHead']),
    movieModal() {
      return this.GET_DETAIL_MOVIE
    },
    genreMovie() {
      return this.getMoviePick.filter(movie => {
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
      return this.genreMovie.slice(this.movieNum, this.movieNum + 12)
    },
    genres() {
      return this.GET_GENRES
    }
  },
}
</script>

<style>

</style>

