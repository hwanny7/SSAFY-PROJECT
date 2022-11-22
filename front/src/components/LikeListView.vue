<template>
  <div>
    <h1>LikeList</h1>
    <div>{{ GET_LIKE_MOIVES }}</div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    name: 'LikeListView',
    props: {
      userPk:Number,
    },
    data() {
      return {

      }
    },
    computed: {
      ...mapGetters(['GET_LIKE_MOIVES']),
    },
    created() {
      const data = {userPk:this.userPk, url:'like'}
      this.$store.dispatch('getLikeMovie', data)
    },
}
</script>

<style>

</style>