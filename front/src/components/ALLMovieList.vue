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
    
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-xl modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">{{ movieModal?.title }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div> {{ movieModal?.id }} </div>
            <div v-if="movieModal?.poster_path">
              <img :src="'https://themoviedb.org/t/p/original'+movieModal?.poster_path" alt="" style="width:200px; height:300px">
            </div>
            <div>{{ movieModal?.overview }}</div>
            <div>{{ movieModal?.genres }}</div>
            <div>
              <h4>Review</h4>
              <MovieReview
              :movie-id="movieModal?.id"
              />
              <ReviewInput 
              :movie-id="movieModal?.id"
              />
            </div>
          </div>
          <div class="modal-footer">
            <div>
              <button type="button" class="btn btn-danger" v-if="FindHate" @click="postlikemovie(movieModal?.id, 'hate')">싫어요 취소</button>
              <button type="button" class="btn btn-danger" v-else  @click="postlikemovie(movieModal?.id, 'hate')">싫어요</button>
            </div>
            <div>
              <button type="button" class="btn btn-primary" v-if="FindLike" @click="postlikemovie(movieModal?.id, 'like')">좋아요 취소</button>
              <button type="button" class="btn btn-primary" v-else @click="postlikemovie(movieModal?.id, 'like')">좋아요</button>
            </div>
          </div>
        </div>
      </div>
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
import MovieReview from '@/components/MovieReview'
import ReviewInput from '@/components/ReviewInput'

export default {
  name: 'ALLMovieList',
  components: {MovieReview, ReviewInput,},
  props:{
    userPk: Number,
  },
  data() {
    return {
      genre: 'all',
      movieNum: 0,
      hate: false,
      like: false,
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
    postlikemovie(movie_pk, url){
      const data = {
        'moviePk':movie_pk,
        'userPk': this.userPk,
        'headers': this.authHead,
        url
      }
      this.$store.dispatch('postLikeMovie', data)
    },
  },
  computed: {
    ...mapGetters(['GET_ALL_MOVIES', 'GET_DETAIL_MOVIE', 'GET_HATE_MOVIES', 'GET_LIKE_MOIVES', 'GET_GENRES']),
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
    FindHate() {
      let hate = false
      this.GET_HATE_MOVIES.forEach(movie => {
        if (movie.id === this.movieModal.id){
          hate = true
        }}
      );
      return hate
    },
    FindLike() {
      let like = false
      this.GET_LIKE_MOIVES.forEach(movie => {
        if (movie.id === this?.movieModal.id){
         like = true
        }}
      );
      return like
    },
    genres() {
      return this.GET_GENRES
    }
  },
}
</script>

<style>

</style>

