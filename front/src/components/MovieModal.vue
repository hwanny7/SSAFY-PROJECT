<template>
  <div id='moviemodal'>
    <div d-flex flex-column mb-3>
      <div class="modal fade text-dark" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header">
              <!-- <h1 class="modal-title fs-5" id="exampleModalLabel">{{ movieModal?.title }}</h1> -->
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div v-if="movieModal?.poster_path">
                <div class="d-flex flex-column justify-content-center align-items-center">
                  <!-- <div>
                      <iframe :src="'https://www.youtube.com/embed/'+ `${movieModal.youtube_key}`" frameborder="1" style="width:50%; height:50vh"></iframe>
                  </div> -->
                  <!-- <div class="text-start">
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
                  </div> -->
                
    <section class="main-card">
        <div class="card-content">
            <div class="content-left">
                <img class="full-img" src="https://images.unsplash.com/photo-1592431454781-ec4870757ce9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80" alt="Unsplash Image">
            </div>
            <div class="content-right">
                <div class="tag"><h6>{{ movieModal?.title }}</h6></div>
                <p class="text-start mt-2">{{ movieModal.overview }}</p>
                <div class="mini-imgs">
                    <img class="mini-img" :src='"https://themoviedb.org/t/p/original/" + GET_BACKDROP[0].file_path' alt="Unsplash Image" @click="changeImg(1)">
                    <img class="mini-img" :src='"https://themoviedb.org/t/p/original/" + GET_BACKDROP[1].file_path' alt="Unsplash Image" @click="changeImg(2)">
                    <img class="mini-img" :src='"https://themoviedb.org/t/p/original/" + GET_BACKDROP[2].file_path' @click="changeImg(3)">
                </div>
            </div>
        </div>
    </section>

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
    ...mapGetters(['GET_DETAIL_MOVIE','GET_LIKE_MOIVES','GET_HATE_MOVIES', 'GET_BACKDROP']),
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
    changeImg(x) {
      var fullImg = document.querySelector(".full-img");
      var miniImg = document.querySelectorAll(".mini-img");
      var targetImg = miniImg[x - 1];
      var imgAttr = targetImg.getAttribute("src");
  
      fullImg.setAttribute("src", imgAttr);
    }
  },
  
}
</script>

<style>

main {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    /* min-height: 640px; */
    background-color: #d1e8ee;
}

/* h2 {
    margin-top: 20px;
    font-size: 3em;
    font-weight: 700;
    line-height: 1;
}

p {
    margin-top: 20px;
    font-size: 1em;
    color: #7B8591;
} */

::selection {
    color: #fff;
    background-color: #005AEE;
}

/* ======================== */
/* Just Copy The Code Below */

/* ------------- */
/* Content Style */
/* ------------- */

.main-card {
    position: relative;
    width: 100%;
    height: 470px;
    margin: 20px;
    border-radius: 10px;
    font-family: 'neuzeit-grotesk', sans-serif;
    font-weight: 300;
    font-style: normal;
    font-size: 1em;
    line-height: 1.5;
    color: #303336;
    background-color: #fff;
    box-shadow: 0 40px 40px -20px #8fc7d544;
}

.main-card .card-content {
    position: relative;
    display: flex;
    width: 100%;
    height: 100%;
    padding: 30px;
}

.main-card .content-left {
    position: relative;
    width: 500px;
    height: 100%;
    border-radius: 10px;
    overflow: hidden;
    background-color: #f6f6f6;
}

.main-card .content-left img {
    width: inherit;
    height: inherit;
    object-fit: cover;
    object-position: center;
}

.main-card .content-right {
    position: relative;
    width: calc(100% - 300px);
    height: 100%;
    padding-left: 15px;
}

.main-card .tag {
    position: relative;
    left: 100%;
    transform: translateX(-100%);
    width: fit-content;
    padding: 8px 25px;
    border-radius: 10px;
    background-color: #005AEE;
}

.main-card .tag h6 {
    color: #fff;
    font-size: .75em;
    font-weight: 700;
    letter-spacing: 2px;
}

.main-card .mini-imgs {
    position: absolute;
    display: flex;
    bottom: 0;
    height: 105px;
}

.main-card .mini-imgs img {
    width: 105px;
    height: 105px;
    border-radius: 10px;
    object-fit: cover;
    object-position: center;
    cursor: pointer;
    transition: 300ms;
}

.main-card .mini-imgs img:hover {
    opacity: .75;
}

.main-card .mini-imgs img:nth-child(2) {
    margin: 0 10px;
}

/* Display this style when screen-width is lower than 992px */
@media only screen and (max-width: 992px) {

    main {
        display: flex;
        justify-content: center;
        align-items: start;
        height: auto;
        min-height: 100vh;
    }

    .main-card {
        position: relative;
        width: 100%;
        height: auto;
        margin: 80px 20px;
    }

    .main-card .card-content {
        flex-direction: column;
    }

    .main-card .content-left {
        width: 100%;
        height: 300px;
    }

    .main-card .content-right {
        width: 100%;
        height: auto;
        padding: 175px 0 0;
    }

    .main-card .tag {
        left: 0;
        transform: translateX(0);
    }

    .main-card .mini-imgs {
        position: absolute;
        display: flex;
        top: 0;
        margin-top: 35px;
        height: 105px;
    }

}

/* Display this style when screen-width is lower than 500px */
@media only screen and (max-width: 500px) {

    .main-card {
        margin: 120px 20px;
    }

    .main-card .card-content {
        padding: 25px;
    }

    .main-card .content-right {
        width: 100%;
        height: auto;
        padding: 115px 0 0;
    }

    .main-card .mini-imgs {
        margin-top: 20px;
    }

    .main-card .mini-imgs img {
        width: 60px;
        height: 60px;
    }

}

/* Just Copy The Code Above */
/* ======================== */

/* ----------- */
/* UI Designer */
/* ----------- */

.designer {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-weight: 400;
    color: #46a2b9;
    letter-spacing: 1px;
    text-align: center;
    text-transform: uppercase;
}

.designer a {
    text-decoration: none;
    color: #23515d;
}

</style>