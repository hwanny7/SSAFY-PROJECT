<template>
  <div>
    <h1>ReviewInput</h1>
    <input type="number" v-model.trim="vote">
    <input type="text" v-model.trim="content">
    <button @click="postreview">댓글달기</button>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'ReviewInput',
  props:{
    movieId: Number,
  },
  data() {
    return {
      vote : null,
      content: null,
    }
  },
  computed: {
    ...mapGetters('login', [
            'authHead', 'user'
        ]),
  },
  methods:{
    postreview() {
      const data = {
        'vote' : this.vote,
        'content': this.content,
        'authHead': this.authHead,
        'movie_pk': this.movieId,
      }
      if (this.content){
        this.$store.dispatch('postReview', data)
        this.vote = null
        this.content = ""
      }
    }

  }

}
</script>

<style>

</style>