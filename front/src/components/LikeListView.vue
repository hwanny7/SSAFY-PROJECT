<template>
  <div>
    <h1>LikeList</h1>
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
            @dblclick="movieDetail(movie.id), clickbtn()"
            >
        </div>
      </div>
    </div>
      <div v-show="false">
        <button id="BTS" data-bs-target="#exampleModal" 
            type="button" 
            data-bs-toggle="modal">상세보기</button>
      </div>
    </swiper-slide>
  </swiper>
  
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
import {mapGetters} from 'vuex'

export default {
    name: 'LikeListView',
    components:{
      Swiper,
      SwiperSlide,
    },

    props: {
      userPk:Number,
    },
    data() {
      return {
        showedmovie: null,
        swiperOption: { 
        slidesPerView: 3, 
        spaceBetween: 30, 
        loop: false, 
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
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
      },
      clickbtn(){
        // const divTag = document.querySelector('#exampleModal_like')
        // divTag.show()
        const btnTag = document.querySelector('#BTS')
        btnTag.click()
      }
    
    },
    computed: {
      ...mapGetters(['GET_LIKE_MOIVES','GET_DETAIL_MOVIE']),
      ...mapGetters('login', ['user'])
    },
    created() {
      const data1 = {userPk:this.user.pk, url:'like'}
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