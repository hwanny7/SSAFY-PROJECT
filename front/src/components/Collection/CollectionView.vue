<template>
  <div v-if="!collection.open_public">
    <button v-if="user.pk === profilePk" @click="delCollection">Delete</button>
    <router-link v-if="user.pk === profilePk" :to="{name: 'CollectionRevise', params: {pk: collection.id}}">수정하기</router-link>

      <div>
        <div class='d-flex flex-row justify-content-center'>
          <div class="d-flex flex-column align-items-center" v-if="$route.name != 'ProfileView'"> <!--닉네임, 사진-->
            <div class="boxx">
              <img :src="'http://127.0.0.1:8000'+ collection.user.image" alt="" class="profile">
            </div>
            <div>
              <router-link :to="{name: 'ProfileView', params: {id: collection.user.pk}}">{{collection.user.nickname}}</router-link>
            </div>
        </div>
        <h3 class="text-center">{{collection.title}} </h3> 
      </div>

      <div class="d-flex flex-column align-items-center">

        <swiper class="swiper" :options="swiperOption" v-if="collection.movies.length < 6 ? swiperOption = swiperOption : swiperOption['loop'] = true">
          <swiper-slide v-for="(movie) in collection.movies" :key="movie.id" class="bg-dark">
            <div class="box-wrap">
              <div class="box">
                <div class="img">
                  <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt=""
                  :data-bs-target="`#o${collection.id}${movie.id}`" data-bs-whatever="@getbootstrap"
                  data-bs-toggle="modal"
                  class="rounded-4"
                  >
                </div>
                <div class="info">
                  <div><h3>{{movie.title}}</h3></div>
                  <div><h5>{{movie.content}}</h5></div>
                </div>
              </div>
            </div>
          </swiper-slide>
        </swiper>

        <div class="d-flex">
          <div v-if="user.pk != collection.user">
            <button v-if="collection.like_users.includes(user.pk)" @click="likeCollection(collection.id)" class="btn btn-danger">{{collection.like_count ? collection.like_count:''}} 좋아요 취소</button>
            <button v-else @click="likeCollection(collection.id)" class="btn btn-danger">{{collection.like_count ? collection.like_count:''}} 좋아요</button>
          </div>
          <button class="btn btn-info" data-bs-toggle="modal" :data-bs-target="`#o${collection.id}`" data-bs-whatever="@getbootstrap"
          @click="getComment"
          >댓글 보기</button>
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

// const swiper = new Swiper('.swiper', {
//    onAny(click, event) {
//      console.log('hi');
//    }
//  });

import CollectionComment from '@/components/Collection/CollectionComment'
import {mapGetters} from 'vuex'


import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
    name: 'CollectionView',
    data() {
      return {
        // content: '',
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
      ])
    },
    props: {
        collection: Object,
        profilePk: Number,
    },
    methods: {
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

</style>