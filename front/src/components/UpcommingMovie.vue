<template>
  <div>
    <h4>UpcomingMovie</h4>
        <div class ="d-flex flex-row justify-content-center flex-wrap">
      <div class="card rounded d-flex justify-content-center align-items-center m-2 radius sample_image" style="width: 12rem;"
      v-for="mmovie in GET_UPCOMING_MOVIES.slice(0, 6)"
      :key="mmovie.id">
        <img :src="'https://themoviedb.org/t/p/original'+mmovie.poster_path" alt="" 
        type="button"  class="card-img-top" style="height: 300px;"
        @dblclick="movieDetail(mmovie.id), clickbtn()"
        >
        <button v-show="false" id="ubtn" data-bs-toggle="modal" data-bs-target="#exampleModal"></button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'UpcommingMovie',
  computed: {
    ...mapGetters(['GET_UPCOMING_MOVIES',]),
    
      recommend_movies () {
        return this.GET_UPCOMING_MOVIES
      }
  },
  methods:{
    movieDetail(movie_pk) {
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
      },
      clickbtn(){
        const btnTag = document.querySelector('#ubtn')
        btnTag.click()
      }
  }

}
</script>

<style>

</style>