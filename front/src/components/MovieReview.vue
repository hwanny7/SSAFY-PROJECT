<template>
  <div>
    <div v-for="review in movieReviews" :key="review.id">
      <div v-if="review.block_users.includes(user.pk)">
        <span> 차단한 메세지입니다. </span>
      </div>
      <div v-else-if="review.block_users.count>5 & block">
        <span @click='reverseblock()'> 다수의 이용자가 차단한 메세지 입니다. 그래도 보시겠습니까? (클릭) </span>
      </div>
        
      <div id='here' v-else>
        
        <div class="d-flex justify-content-between mt-3">
          <div class="d-flex flex-row">
            <div class="boxx">
              <img :src="'http://127.0.0.1:8000' + review.user.image" alt=""  class="profile">
            </div>
            <div class="d-flex flex-column justify-content-center align-items-ceneter text-dark">
              {{review?.user.nickname}}: {{review?.content}}
            </div>
          </div>

          <div class="d-flex flex-row">
            <star-rating id=setstar  class="mx-3"
            :star-size="30" :increment="0.5" v-model="review.vote"
            :read-only="true"  :border-width="5" border-color="#d8d8d8" 
            :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
            </star-rating>
            <button class="btn btn-warning p-1" @click="deleteReview(review.id)" v-if="user.pk === review.user.pk">삭제</button>
            <button class="btn btn-warning p-1" @click="blockReview(review.id)" v-if="user.pk != review.user.pk">삭제</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import StarRating from 'vue-star-rating'


export default {
  name: 'MovieReview',
  components:{
    StarRating,
  },
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
    },
    setRating: function(){
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
  mounted() {
    
  }
  }
  
</script>

<style>

</style>