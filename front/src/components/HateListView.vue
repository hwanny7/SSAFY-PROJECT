<template>
<div>
    <h1>LikeList</h1>
    <div class="modal fade" id="exampleModal_hate" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
            <div @click="reverse('hate')">
              <button type="button" class="btn btn-danger" v-if="hate" @click="postlikemovie(movieModal?.id, 'hate')">싫어요 취소</button>
              <button type="button" class="btn btn-danger" v-else  @click="postlikemovie(movieModal?.id, 'hate')">싫어요</button>
            </div>
            <div @click="reverse('like')">
              <button type="button" class="btn btn-primary" v-if="like" @click="postlikemovie(movieModal?.id, 'like')">좋아요 취소</button>
              <button type="button" class="btn btn-primary" v-else @click="postlikemovie(movieModal?.id, 'like')">좋아요</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <span 
    v-for="HMovie in GET_HATE_MOVIES"
    :key="HMovie.id">
      <img :src="'https://themoviedb.org/t/p/original'+HMovie.poster_path" alt="" 
      style="width: 100px; height: 100px" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal_hate"
      @click="movieDetail(HMovie.id)"
      >
    </span>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import MovieReview from '@/components/MovieReview'
import ReviewInput from '@/components/ReviewInput'

export default {
    name: 'HateListView',
    components:{
      MovieReview, 
      ReviewInput,
    },
    props: {
      userPk:Number,
    },
    data() {
      return {
        like : false,
        hate : true,
      }
    },
    methods:{
      movieDetail(movie_pk) {
        this.like = false
        this.hate = true
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
      },
      reverse(msg) {
        if (msg === 'hate'){
          this.like = false
          this.hate = !this.hate
        } else {
          this.like = !this.like
          this.hate = false
        }
      },
      postlikemovie(movie_pk, url){
        
        const data = {
          'moviePk':movie_pk,
          'userPk': this.userPk,
          url
        }
        this.$store.dispatch('postLikeMovie', data)
      },
    },
    computed: {
      ...mapGetters(['GET_HATE_MOVIES','GET_DETAIL_MOVIE']),
      movieModal() {
      return this.GET_DETAIL_MOVIE
    },
    },
    created() {
      const data2 = {userPk:this.$route.params.id, url:'hate'}
      this.$store.dispatch('getLikeMovie', data2)
    },

}
</script>

<style>

</style>