<template>
  <div>
    <div>
      <star-rating
      id=setstar :star-size="30" v-model="rating" 
      :increment="0.5" :border-width="5" border-color="#d8d8d8"
      
      :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
      </star-rating>
      <div></div>
      <input type="text" v-model.trim="content" @keyup.enter='postreview' class="col-6">
      <div></div>
      <button @click="postreview">작성</button>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewInput',
  props:{
    movieId: Number,
  },
  components: {
    StarRating
  },
  data() {
    return {
      content: null,
      rating: 0,
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
        'vote' : this.rating,
        'content': this.content,
        'authHead': this.authHead,
        'movie_pk': this.movieId,
      }
      if (this.content){
        this.$store.dispatch('postReview', data)
        this.vote = null
      }
      this.content = ""
      this.rating = 0
    },
    setRating: function(rating){
      this.rating= rating;
    }

  }

}
</script>

<style>

</style>