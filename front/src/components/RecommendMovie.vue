<template>
  <div class="mt-5">
    <h4>Recommend Movie</h4>
    <div>
    <button @click='renew()'>추천영화 새로 고침</button>
    </div>

    <div class ="d-flex flex-row justify-content-center flex-wrap">
      <div class="card rounded d-flex justify-content-center align-items-center m-2 radius sample_image" style="width: 12rem;"
      v-for="mmovie in recommend_movies"
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
  name: 'RecommendMovie',
  methods: {
    renew() {
      this.$store.dispatch('getRecommendMovie', this.authHead)
    },
  },
  computed: {
    ...mapGetters('login' ,['user','authHead']),
    ...mapGetters(['GET_REOCOMMEND_MOVIES',]),
      recommend_movies () {
        return this.GET_REOCOMMEND_MOVIES
      }
  }

  
}
</script>

<style>

</style>