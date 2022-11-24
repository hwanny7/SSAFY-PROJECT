<template>
  <div class="my-5">
    <h4>Recommend Movie</h4>
    <div>
    <button class="btn btn-secondary" @click='renew()'>추천영화 새로 고침</button>
    </div>
    
    <div v-if="GET_LIKE_MOIVES.length >= 3">
      <div class ="d-flex flex-row justify-content-center flex-wrap">
        <div class="card rounded d-flex justify-content-center align-items-center m-2 radius sample_image" style="width: 12rem;"
        v-for="rmovie in recommend_movies"
        :key="rmovie.id">
          <img :src="'https://themoviedb.org/t/p/original'+rmovie.poster_path" alt="" 
            class="card-img-top" style="height: 300px;"
          @dblclick="movieDetail(rmovie.id), btclick()"
          >
          <button id="rbtn" v-show="false" data-bs-toggle="modal" data-bs-target="#exampleModal"></button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>좋아하는 영화를 3개 이상 선택해주세요</p>
    </div>
  </div>
</template>



<script>
import {mapGetters} from 'vuex'

export default {
  name: 'RecommendMovie',
  methods: {
    renew() {
      this.$store.dispatch('getRecommendMovie', this.authHead)
    },
    btclick() {
      const btnTag = document.querySelector('#rbtn')
      btnTag.click()
    },
    movieDetail(movie_pk) {
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
      },
  },
  computed: {
    ...mapGetters('login' ,['user','authHead']),
    ...mapGetters(['GET_REOCOMMEND_MOVIES','GET_LIKE_MOIVES']),
      recommend_movies () {
        return this.GET_REOCOMMEND_MOVIES
      }
  },
  
}
</script>

<style>

</style>