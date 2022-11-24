<template>
  <div id='moviemodal'>
    <div d-flex flex-column mb-3>
      <div class="modal fade text-dark" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">제목 : {{ movieModal?.title }}</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div v-if="movieModal?.poster_path">
                <div class="d-flex flex-column">
                  <div>
                      <iframe :src="'https://www.youtube.com/embed/'+ `${movieModal.youtube_key}`" frameborder="1" style="width:50%; height:50vh"></iframe>
                  </div>
                  <div class="text-start">
                    <p>{{ movieModal.overview }}</p>
                    <div v-if="movieModal.directors.length>=1">
                      <h4>감독</h4>
                      <div v-for="director in movieModal.directors" :key="director.name"><p>{{ director.name }},</p></div>
                    </div>
                    <div v-if="movieModal.actors.length>=1">
                      <h4>배우</h4>
                      <p v-for="actor in movieModal.actors" :key="actor.name">{{ actor.name }},</p>
                    </div>
                    <h4>장르</h4>
                    <p v-for="genre in movieModal?.genres" :key="genre.id" >{{ genre.name+" " }}</p>
                  </div>

                </div>
              </div>
              
              <div class="my-5">
              <h4>Review</h4>
              </div>
              <div>
                <div style="heigth:500px" class="mb-4">
                  <MovieReview
                  :movie-id="movieModal?.id"
                  />
                </div>
                <ReviewInput 
                :movie-id="movieModal?.id"
                />
              </div>
            </div>
            <div class="modal-footer">
              <div>
                <button type="button" class="btn btn-danger" v-if="hate" @click="postlikemovie(movieModal?.id, 'hate')">싫어요 취소</button>
                <button type="button" class="btn btn-danger" v-else  @click="postlikemovie(movieModal?.id, 'hate')">싫어요</button>
              </div>
              <div>
                <button type="button" class="btn btn-primary" v-if="like" @click="postlikemovie(movieModal?.id, 'like')">좋아요 취소</button>
                <button type="button" class="btn btn-primary" v-else @click="postlikemovie(movieModal?.id, 'like')">좋아요</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview'
import ReviewInput from '@/components/ReviewInput'
import {mapGetters} from 'vuex'

export default {
  name:'MovieModal',
  components: {
    MovieReview,
    ReviewInput,
  },
  computed: {
    ...mapGetters(['GET_DETAIL_MOVIE','GET_LIKE_MOIVES','GET_HATE_MOVIES']),
    ...mapGetters('login' ,['user','authHead']),
      movieModal() {
      return this.GET_DETAIL_MOVIE
    },
    like(){
      return this.movieModal.like_users.includes(this.user.pk)
    },
    hate(){
      return this.movieModal.hate_users.includes(this.user.pk)
    }
  },
  methods: {
    postlikemovie(movie_pk, url){
        const data = {
          'moviePk':movie_pk,
          'userPk': this.user.pk,
          url
        }
        this.$store.dispatch('postLikeMovie', data)
    },
    
  },
  
}
</script>

<style>

</style>