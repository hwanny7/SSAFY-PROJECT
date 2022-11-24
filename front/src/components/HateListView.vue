<template>
<div>
    <span 
    v-for="HMovie in GET_HATE_MOVIES"
    :key="HMovie.id">
      <img :src="'https://themoviedb.org/t/p/original'+HMovie.poster_path" alt="" 
      style="width: 100px; height: 100px" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"
      @click="movieDetail(HMovie.id)"
      >
    </span>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
    name: 'HateListView',
    components:{
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
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
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
      ...mapGetters('login', ['user',]),
      ...mapGetters(['GET_HATE_MOVIES',]),

    },
    created() {
      const data2 = {userPk:this.user.pk, url:'hate'}
      this.$store.dispatch('getLikeMovie', data2)
    },

}
</script>

<style>

</style>