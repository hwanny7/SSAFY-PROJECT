<template>
  <div>
    <div v-for="review in movieReviews" :key="review.id">
      <div v-if="review.block_users.includes(user.pk)">
        <span> 차단한 메세지입니다. </span>
      </div>
      <div v-else>
        {{ review }}
        <button @click="deleteReview(review.id)" v-if="user.pk === review.user">X</button>
        <button @click="blockReview(review.id, user.pk)" v-if="user.pk != review.user">차단</button>
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
        'headers': this.authHead
      }
      this.$store.dispatch('blockReview', data)
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