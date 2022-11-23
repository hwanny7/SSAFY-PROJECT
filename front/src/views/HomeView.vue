<template>
  <div>
    <h1>HomeView</h1>
    <UpcommingMovie />
    <RecommendMovie />
  </div>
</template>

<script>
import RecommendMovie from '@/components/RecommendMovie'
import UpcommingMovie from '@/components/UpcommingMovie'
import {mapGetters} from 'vuex'

export default {
    name: 'HomeView',
    components: {
      RecommendMovie,
      UpcommingMovie,
    },
    computed: {
      ...mapGetters('login', [
            'authHead', 'user'
        ]),
      
    },
    created() {
      this.$store.dispatch('getRecommendMovie',this.authHead)
      this.$store.dispatch('getUpcomingMovie')
    }

}
</script>

<style>

</style>