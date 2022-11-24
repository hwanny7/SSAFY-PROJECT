<template>
  <div>
    <div v-if="!collection.open_public | user.pk === profilePk">
      <div>
        <div class="d-flex flex-column align-items-center border rounded-4 mb-3 border border-secondary">
        <h3 class="text-center mt-2">{{collection.title}} </h3> 
        <swiper class="swiper" :options="swiperOption" v-if="collection.movies.length < 4 ? swiperOption = swiperOption : swiperOption['loop'] = true">
          <swiper-slide v-for="(movie) in collection.movies" :key="movie.id" class="bg-dark">
            <div class="box-wrap">
              <div class="box">
                <div class="img">
                  <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt=""
                  :data-bs-target="`#o${collection.id}${movie.id}`" data-bs-whatever="@getbootstrap"
                  :class="{'glowing-border':movie.content}"
                  data-bs-toggle="modal"
                  class="rounded-4"
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

      <div class="mb-2">
        <!-- <p>{{collection.like_count ? collection.like_count:''}}</p> -->
        <span class="hex-icon-heart" @click="likeCollection(collection.id, collection.user)">
          <svg class="mt-3">
            <path d="M19,1 Q21,0,23,1 L39,10 Q41.5,11,42,14 L42,36 Q41.5,39,39,40 L23,49 Q21,50,19,49 L3,40 Q0.5,39,0,36 L0,14 Q0.5,11,3,10 L19,1" />
            <path :style="{fill: MYcolor}" d="M11,17 Q16,14,21,20 Q26,14,31,17 Q35,22,31,27 L21,36 L11,27 Q7,22,11,17" />
            </svg>
          </span>
        <button class="btn btn-secondary m-2" data-bs-toggle="modal" :data-bs-target="`#o${collection.id}`" data-bs-whatever="@getbootstrap"
        @click="getComment"
        >댓글 보기</button>
        <span  v-if="user.pk === profilePk">
          <button class="btn btn-info m-2"><router-link :to="{name: 'CollectionRevise', params: {pk: collection.id}}" style ="text-decoration: none;" class="text-white">수정하기</router-link></button>
          <button class="btn btn-danger m-2" @click="delCollection">삭제하기</button>
        </span>
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
  </div>


</template>

<script>
import CollectionComment from '@/components/Collection/CollectionComment'
import {mapGetters} from 'vuex'

import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
    name: 'ProfileCollectionView',
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
        SwiperSlide,
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
      likeCollection(collection_pk, id) {
        const payload = {
          collection_pk : collection_pk,
          headers: this.authHead,
          id: id,
        }
        this.$store.dispatch('collection/likeColpro', payload)
      }
    },
}
</script>

<style>

</style>