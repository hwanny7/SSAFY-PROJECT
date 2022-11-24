<template>
  <div>
    <h4>RecommendMovie</h4>
    <div>
    <button @click='renew()'>추천영화 새로 고침</button>
    </div>
    {{ recommend_movies }}
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