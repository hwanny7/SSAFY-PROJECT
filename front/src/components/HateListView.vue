<template>
  <div>
    <h1>HateList</h1>
   
    <!-- 여기까지가 modal -->
    {{ GET_HATE_MOVIES }}
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    name: 'HateListView',
    props: {
      userPk:Number,
    },
    data() {
      return {
      }
    },
    computed: {
      ...mapGetters(['GET_HATE_MOVIES']),
    },
    created() {
      const data = {userPk:this.userPk, url:'hate'}
      this.$store.dispatch('getLikeMovie', data)
      return this.GET_HATE_MOVIES
    },

}
</script>

<style>

</style>