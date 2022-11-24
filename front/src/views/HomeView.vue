<template>
  <div>
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
      this.$store.dispatch('getUpcomingMovie')
      const data1 = {userPk:this.user.pk, url:'like'}
      this.$store.dispatch('getLikeMovie', data1)
      const data2 = {userPk:this.user.pk, url:'hate'}
      this.$store.dispatch('getLikeMovie', data2)
      
    }

}
</script>

<style>

</style>