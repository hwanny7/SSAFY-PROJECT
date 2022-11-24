<template>
  <div>
    <h4>UpcomingMovie</h4>
        <div class ="d-flex flex-row justify-content-center flex-wrap">
      <div class="card rounded d-flex justify-content-center align-items-center m-2 radius sample_image" style="width: 12rem;"
      v-for="mmovie in GET_UPCOMING_MOVIES.slice(0, 6)"
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
  name: 'UpcommingMovie',
  computed: {
    ...mapGetters(['GET_UPCOMING_MOVIES',]),
    
      recommend_movies () {
        return this.GET_UPCOMING_MOVIES
      }
  }

}
</script>

<style>

</style>