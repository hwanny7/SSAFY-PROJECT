<template>
  <div>
    <h4>RecommendMovie</h4>
    {{ recommend_movies }}
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'RecommendMovie',
  computed: {
    ...mapGetters(['GET_REOCOMMEND_MOVIES',]),
      recommend_movies () {
        return this.GET_REOCOMMEND_MOVIES
      }
  }

  
}
</script>

<style>

</style>