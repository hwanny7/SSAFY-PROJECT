<template>
  <div>
    <h4>UpcomingMovie</h4>
    {{ GET_UPCOMING_MOVIES }}
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