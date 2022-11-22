<template>
  <div v-if="!collection.open_public">
    <button v-if="user.pk === profilePk" @click="delCollection">Delete</button>
    <router-link v-if="user.pk === profilePk" :to="{name: 'CollectionRevise', params: {pk: collection.id}}">수정하기</router-link>

      <div>
        <div class='d-flex flex-row justify-content-center'>
          <div class="d-flex flex-column align-items-center" v-if="$route.name != 'ProfileView'"> <!--닉네임, 사진-->
            <div class="box">
              <img :src="'http://127.0.0.1:8000'+ collection.user.image" alt="" class="profile">
            </div>
            <div>
              <router-link :to="{name: 'ProfileView', params: {id: collection.user.pk}}">{{collection.user.nickname}}</router-link>
            </div>
        </div>
        <h3 class="text-center">{{collection.title}} </h3> 
      </div>

      <div class="d-flex flex-column align-items-center">
        <div class ="d-flex flex-row justify-content-center flex-wrap">
          <CollectionMovie
          v-for="(movie) in collection.movies"
          :key="movie.id"
          :movie="movie"
          :collection-id="collection.id"
          />
        </div>
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
    <hr>
  </div>


</template>

<script>
import CollectionComment from '@/components/Collection/CollectionComment'
import CollectionMovie from '@/components/Collection/CollectionMovie'
import {mapGetters} from 'vuex'

export default {
    name: 'CollectionView',
    data() {
      return {
        content: ''
      }
    },
    components: {
        CollectionComment,
        CollectionMovie,
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
      }
    },
}
</script>

<style>

</style>