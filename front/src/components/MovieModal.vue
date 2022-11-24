<template>
  <div id='moviemodal'>
    <div d-flex flex-column mb-3>
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header">
              <!-- <h4>{{ movieModal }}</h4> -->
              <h1 class="modal-title fs-5" id="exampleModalLabel">제목 : {{ movieModal?.title }}</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div v-if="movieModal?.poster_path">
                <div class="row" style='height:300px'>
                  <div class="col">
                      <iframe :src="'https://www.youtube.com/embed/'+ `${movieModal.youtube_key}`" frameborder="1" style="width:100%; height:100%"></iframe>
                  </div>
                  <div class="col">
                    <span>{{ movieModal.overview }}</span>
                    <div v-if="movieModal.directors.length>=1">
                      <h4>감독</h4>
                      <span v-for="director in movieModal.directors" :key="director.name">{{ director.name }},</span>
                    </div>
                    <div v-if="movieModal.actors.length>=1">
                      <h4>배우</h4>
                      <span v-for="actor in movieModal.actors" :key="actor.name">{{ actor.name }},</span>
                    </div>
                    <h4>장르</h4>
                    <span v-for="genre in movieModal?.genres" :key="genre.id" >{{ genre.name+" " }}</span>
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
                <button type="button" class="btn btn-danger" v-if="FindHate" @click="postlikemovie(movieModal?.id, 'hate')">싫어요 취소</button>
                <button type="button" class="btn btn-danger" v-else  @click="postlikemovie(movieModal?.id, 'hate')">싫어요</button>
              </div>
              <div>
                <button type="button" class="btn btn-primary" v-if="FindLike" @click="postlikemovie(movieModal?.id, 'like')">좋아요 취소</button>
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
    FindHate() {
      let hate = false
      this.GET_HATE_MOVIES.forEach(movie => {
        if (movie.id === this.movieModal.id){
          hate = true
        }}
      );
      return hate
    },
    FindLike() {
      let like = false
      this.GET_LIKE_MOIVES.forEach(movie => {
        if (movie.id === this?.movieModal.id){
         like = true
        }}
      );
      return like
    },
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