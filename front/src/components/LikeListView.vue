<template>
  <div>
    <h1>LikeList</h1>
    <div class="modal fade" id="exampleModal_like" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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

    <swiper
    class="swiper"
    :options="swiperOption" >

    <swiper-slide
     v-for="movie in GET_LIKE_MOIVES"
    :key="movie.id">
    <div class="box-wrap"> 
      <div class='box' style='width:300px; height:500px;'>
        <div class="img">
          <img :src="'https://themoviedb.org/t/p/original'+movie.poster_path" alt="" 
            type="button" data-bs-toggle="modal"
            data-bs-target="#exampleModal_like"
            class="rounded-4"
            @click="movieDetail(movie.id)"
            >
        </div>
      </div>
    </div>
    </swiper-slide>     
    
    <!-- <div
        class="swiper-pagination"
        slot="pagination"
        >
    </div> -->
</swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

import {mapGetters} from 'vuex'
import MovieReview from '@/components/MovieReview'
import ReviewInput from '@/components/ReviewInput'

export default {
    name: 'LikeListView',
    components:{
      MovieReview, 
      ReviewInput,
      Swiper,
      SwiperSlide,
    },

    props: {
      userPk:Number,
    },
    data() {
      return {
        like : true,
        hate : false,
        swiperOption: { 
        slidesPerView: 1, 
        spaceBetween: 30, 
        loop: true, 
        pagination: { 
            el: '.swiper-pagination', 
            clickable: true 
        }, 
        navigation: { 
            nextEl: '.swiper-button-next', 
            prevEl: '.swiper-button-prev' 
        },
    },
      }
    },
    methods:{
      movieDetail(movie_pk) {
        this.like = true,
        this.hate = false,
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
      ...mapGetters(['GET_LIKE_MOIVES','GET_DETAIL_MOVIE']),
      movieModal() {
      return this.GET_DETAIL_MOVIE
    },
      
    },
    created() {
      const data1 = {userPk:this.$route.params.id, url:'like'}
      this.$store.dispatch('getLikeMovie', data1)
    },
}
</script>

<style>
.box-wrap {
  /* width: 100vw;
  height: 100vh; */
  display: flex;
  justify-content: center;
  align-items: center
}
.box {
  position: relative;
  /* width: 400px; height: 300px;
  border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4)
}
.box img {
  width: 100%;
}


</style>