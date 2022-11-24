<template>
  <div>
    <h1>HomeView</h1>
      <ALLMovieList
      :user-pk="user.pk"
      />
    <UpcommingMovie />
    <RecommendMovie />
  </div>
</template>

<script>
import ALLMovieList from '@/components/ALLMovieList'
import RecommendMovie from '@/components/RecommendMovie'
import UpcommingMovie from '@/components/UpcommingMovie'
import {mapGetters} from 'vuex'

export default {
    name: 'HomeView',
    data(){
      return {
        
      }
    },
    components: {
      RecommendMovie,
      UpcommingMovie,
      ALLMovieList,
    },
    computed: {
      ...mapGetters('login', [
            'authHead', 'user'
        ]),
    },
    created() {
      this.$store.dispatch('getRecommendMovie',this.authHead)
      
    }

}
</script>

<style>

</style>