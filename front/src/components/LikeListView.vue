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
            <div v-if="movieModal?.poster_path">
              <div class="row">
                <div class="col">
                    <iframe :src="'https://www.youtube.com/embed/'+ `${movieModal.youtube_key}`" frameborder="1"></iframe>
                </div>
                <div class="col">
                  <div>
                    {{ movieModal?.overview }}
                  </div>
                  <span v-for="genre in movieModal?.genres" :key="genre.id" >{{ genre.name+" " }}</span>
                </div>
              </div>
            </div>

            <div>
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
    <!-- <swiper class="swiper" :options="swiperOption" v-if="GET_LIKE_MOIVES.length < 6 ? swiperOption = swiperOption : swiperOption['loop'] = true">
          <swiper-slide v-for="movie in GET_LIKE_MOIVES" :key="movie.id" class="bg-dark">
            <div class="box-wrap">
              <div class="box">
                <div class="img">
                  <img :src="'https://themoviedb.org/t/p/original'+movie.poster_path" alt="" 
                   data-bs-toggle="modal"
                  data-bs-target="#exampleModal_like"
                  class="rounded-4"
                  @click="movieDetail(movie.id)"
                  >
                </div>
                
              </div>
            </div>
          </swiper-slide>
        </swiper> -->


    <swiper
    class="swiper"
    :options="swiperOption"
     >

    <swiper-slide
     v-for="movie in GET_LIKE_MOIVES"
    :key="movie.id"
    
    >
    <div class="box-wrap"> 
      <div class='box mt-0 mp-0' style="width:400px; height:610px;">
        <div class="img">
          <img :src="'https://themoviedb.org/t/p/original'+movie.poster_path" alt="" 
            class="rounded-4"
            style="width:400px; height:610px;"
            @click="movieDetail(movie.id)"
            data-bs-target="#exampleModal_like" 
            type="button" 
            data-bs-toggle="modal"
            >
        </div>
      </div>
    </div>
    </swiper-slide>
  </swiper>
  <div v-show="true">
    <button id="BTS">
            상세보기
          </button>
  </div>
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
        showedmovie: null,
        like : true,
        hate : false,
        swiperOption: { 
        slidesPerView: 5, 
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
      showMovie(){
        // const divTag = document.querySelector('#exampleModal_like')
        // divTag.show()
        const btnTag = document.querySelector('#BTS')
        btnTag.onclick()
       
        
      }
    
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
    mounted() {
      
    }
    
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

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}


</style>