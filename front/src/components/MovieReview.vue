<template>
  <div>
    <div v-for="review in movieReviews" :key="review.id">
      <div v-if="review.block_users.includes(user.pk)">
        <span> 차단한 메세지입니다. </span>
      </div>
      <div v-else-if="review.block_users.count>5 & block">
        <span @click='reverseblock()'> 다수의 이용자가 차단한 메세지 입니다. 그래도 보시겠습니까? (클릭) </span>
      </div>
      <div v-else>
        {{ review }}
        <button @click="deleteReview(review.id)" v-if="user.pk === review.user">X</button>
        <button @click="blockReview(review.id)" v-if="user.pk != review.user">차단</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'MovieReview',
  props: {
    movieId: Number,
  },
  data() {
    return{
      block : true
    }
  },
  methods: {
    deleteReview(review_id) {
      const data = {
        'movie_pk': this.movieId,
        'review_id':review_id,
        'headers': this.authHead
      }
      this.$store.dispatch('deleteReview', data)
    },
    blockReview(review_id) {
      const data = {
        'review_id': review_id,
        'headers': this.authHead,
        'movie_pk': this.movieId
      }
      this.$store.dispatch('blockReview', data)
    },
    reverseblock() {
      this.block = false
    }
  },
  computed: {
    ...mapGetters(['GET_ALL_REVIEWS']),
    ...mapGetters('login', [
            'authHead', 'user'
        ]),
    movieReviews() {
      return this.GET_ALL_REVIEWS
    }
  },
  }
  
</script>

<style>

</style>