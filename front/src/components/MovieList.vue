<template>
  <div>
    <h1>MovieList</h1>
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
            <img :src="'https://themoviedb.org/t/p/original'+movieModal?.poster_path" alt="" style="width:200px; height:300px">
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
              <button type="button" class="btn btn-danger" v-if="FindHate" @click="postlikemovie(movieModal?.id, 'hate'), reverse('hate')">싫어요 취소</button>
              <button type="button" class="btn btn-danger" v-else  @click="postlikemovie(movieModal?.id, 'hate'), reverse('hate')">싫어요</button>
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
    v-for="movie in movieSlice"
    :key="movie.id">
      <img :src="'https://themoviedb.org/t/p/original'+movie.poster_path" alt="" 
      style="width: 100px; height: 100px" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"
      @click="movieDetail(movie.id)"
      >
    </span>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import MovieReview from '@/components/MovieReview'
import ReviewInput from '@/components/ReviewInput'

export default {
  name: 'MovieList',
  components: {MovieReview, ReviewInput,},
  props:{
    userPk: Number,
  },
  data() {
    return {
      movieNum: 1,
      hate: false,
      like: false,
    }
  },
  methods: {
    
    beforeMovie() {
      if ((this.movieNum) > 1 ){
        this.movieNum -= 1
      }
    },
    afterMovie() {
      if (this.GET_ALL_MOVIES[String(this.movieNum + 1)].length>0){
        this.movieNum += 1
      }
    },
    movieDetail(movie_pk) {
      this.$store.dispatch('getDetailMovie', movie_pk)
      this.$store.dispatch('getReview', movie_pk)
    },
    postlikemovie(movie_pk, url){
      console.log(movie_pk, url)
      const data = {
        'moviePk':movie_pk,
        'userPk': this.userPk,
        url
      }
      this.$store.dispatch('postLikeMovie', data)
    },

  },
  computed: {
    ...mapGetters(['GET_ALL_MOVIES', 'GET_DETAIL_MOVIE', 'GET_HATE_MOVIES', 'GET_LIKE_MOIVES']),
    ...mapGetters('login' ,['user','authHead']),
    movieModal() {
      return this.GET_DETAIL_MOVIE
    },
    movieSlice() {
      const newMovie = this.GET_ALL_MOVIES[String(this.movieNum)]
      return newMovie
    },
    FindHate() {
      let hate = false
      const arr = []
      arr.forEach(movie => {
        console.log('호잇', movie)
      })
      // this.GET_HATE_MOVIES.forEach(movie => {
      //   if (movie.id === this.movieModal.id){
      //     hate = true
      //   }}
      // );
      return hate
    },
    FindLike() {
      let like = false
      console.log(this.GET_LIKE_MOIVES)
      this.GET_LIKE_MOIVES.forEach(movie => {
        if (movie.id === this?.movieModal.id){
         like = true
        }}
      );
      return like
    },
  },
  created () {
    const data1 = {
      'url': 'like',
      'userPk': this.user.pk
    }
    const data2 = {
      'url': 'hate',
      'userPk': this.user.pk
    }
    this.$store.dispatch('getAllMovie')
    this.$store.dispatch('getLikeMovie', data1 )
    this.$store.dispatch('getAllMovie', data2)
  }
}
</script>

<style>

</style>

