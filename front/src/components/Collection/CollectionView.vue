<template>
  <div v-if="!collection.open_public" class="container border rounded-4 mb-3">
    <div class="row align-items-center">
      <div class="d-flex flex-column align-items-center mb-5 col-3 mt-3">
        <div class="card bg-dark rounded-3" style="width: 18rem;">
          <img :src="'http://127.0.0.1:8000' + collection.user.image" class="card-img-top" alt="" style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">{{collection.user.nickname}}</h5>
            <p>{{collection.user.followers_count ? `팔로워: ${collection.user.followers_count}명`: ''}}</p>
            <p>{{collection.like_count ? `좋아요: ${collection.like_count}명`: ''}}</p>
            <p class="card-text">{{collection.user.content}}</p>
            <div class="d-flex flex-row justify-content-center align-items-center">
              <router-link :to="{name: 'ProfileView', params: {id: collection.user.pk}}"><button class="btn btn-primary">Profile</button></router-link>
              <span class="hex-icon-heart" @click="likeCollection(collection.id)">
                <svg>
                  <path d="M19,1 Q21,0,23,1 L39,10 Q41.5,11,42,14 L42,36 Q41.5,39,39,40 L23,49 Q21,50,19,49 L3,40 Q0.5,39,0,36 L0,14 Q0.5,11,3,10 L19,1" />
                  <path :style="{fill: MYcolor}" d="M11,17 Q16,14,21,20 Q26,14,31,17 Q35,22,31,27 L21,36 L11,27 Q7,22,11,17" />
                </svg>
              </span>
              <button class="btn btn-info" data-bs-toggle="modal" :data-bs-target="`#o${collection.id}`" data-bs-whatever="@getbootstrap"
              @click="getComment"
              >Comment</button>
              </div>
            </div>
          </div>
        </div>
        
        <div class="col-9">
          <div class="d-flex flex-column align-items-center">
            <h3 class="text-center">{{collection.title}}</h3> 
            <swiper class="swiper" :options="swiperOption" v-if="collection.movies.length < 6 ? swiperOption = swiperOption : swiperOption['loop'] = true">
              <swiper-slide v-for="(movie) in collection.movies" :key="movie.id" class="bg-dark" >
                <button v-show="false" data-bs-target="#exampleModal" 
            type="button" id="cbtn"
            data-bs-toggle="modal"></button>
                <div class="box-wrap">
                  <div class="box">
                    <div class="img">
                      <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt=""
                      :data-bs-target="`#o${collection.id}${movie.id}`" data-bs-whatever="@getbootstrap"
                      data-bs-toggle="modal"
                      class="rounded-4"
                      @dblclick="movieDetail(movie.id), cbtnclick()"
                      >
                    </div>
                    <div class="info">
                      <!-- <div><h3>{{movie.title}}</h3></div> -->
                      <div><h5>{{movie.content}}</h5></div>
                    </div>
                  </div>
                </div>
              </swiper-slide>
            </swiper>
          </div>
        </div>
    </div>
    
      <div class="modal fade" :id="'o'+ collection.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">내용</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                  <CollectionComment
                  v-for="(comment, index) in getComments[collection.id]"
                  :key="`o-${index}`"
                  :comment="comment"
                  :collection-pk="collection.id"
                  />
                </div>
                <textarea class="form-control" id="message-text" v-model="content"></textarea>
            </div>
              <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">나가기</button>
              <button type="button" class="btn btn-primary" @click="createComment">댓글 작성</button>
              </div>
            </div>
          </div>
        </div>
   </div>



</template>

<script>


import CollectionComment from '@/components/Collection/CollectionComment'
import {mapGetters} from 'vuex'


import { Swiper, SwiperSlide } from "vue-awesome-swiper";

export default {
    name: 'CollectionView',
    data() {
      return {
        content: '',
        swiperOption: { 
        slidesPerView: 5, 
        spaceBetween: 30, 
        effect:'coverflow',
        grabCursor:"true",
        centeredSlides:"true",
        coverflowEffect:{
          rotate: 30,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: true,
        },
        pagination:"true",
        modules:"modules",
        class:"mySwiper",
      },
      }
    },
    components: {
        CollectionComment,
        Swiper,
        SwiperSlide
    },
    computed: {
      ...mapGetters('login', [
        'user', 'authHead'
      ]),
      ...mapGetters('collection', [
        'getComments',
      ]),
      MYcolor() {
        return this.collection.like_users.includes(this.user.pk) ? "red" : "white"
      }
    },
    props: {
        collection: Object,
        profilePk: Number,
    },
    methods: {
      cbtnclick(){
        const btn = document.querySelector('#cbtn')
        btn.click()
      },
      movieDetail(movie_pk) {
        this.$store.dispatch('getDetailMovie', movie_pk)
        this.$store.dispatch('getReview', movie_pk)
      },
      delCollection() {
        const payload = {"id":this.collection.id, "authHead" : this.authHead, "user_id" : this.user.pk}
        this.$store.dispatch('collection/DeleteCollection', payload)
      },
      getComment() {
        this.$store.dispatch('collection/getComments', this.collection.id)
      },
      createComment() {
        if (!this.content){
          alert('내용을 입력해 주세요')
        } else {
          const payload = {
            collection_pk : this.collection.id,
            headers: this.authHead,
            content: this.content
          }
          this.$store.dispatch('collection/actionCreate', payload)
          this.content= ''
        }
      },
      likeCollection(collection_pk) {
        const payload = {
          collection_pk : collection_pk,
          headers: this.authHead,
        }
        this.$store.dispatch('collection/likeCol', payload)
      },
    },
}
</script>

<style>
.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}




.box-wrap {
  /* width: 100vw;
  height: 100vh; */
  display: flex;
  justify-content: center;
  align-items: center
}
.box {
  position: relative;
  /* width: 400px; height: 300px;
  border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4)
}
.box img {
  width: 100%;
}

.box .info {
  color: #fff;
  position: absolute; left: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  width: 100%;
  padding: 15px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.35s ease-in-out;
}
.box:hover .info {
  opacity: 1;
}
.box .info h3 {
  font-size: 24px;
  padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}
.box .info p {
  font-size: 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}


/* 좋아요 버튼 */


</style>