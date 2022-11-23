<template>
  <div class="d-flex">
    <div class="boxx mt-3 float-start">
    <img :src="'http://127.0.0.1:8000' + comment.user.image" alt="" class="profile">
    </div>
    <p class="text-black text-center">{{comment.user.nickname}}: {{comment.content}}</p>
    <!-- <div class="d-flex flex-row align-items-center">
      <button v-if="user.pk === comment.user.id"
      class="btn btn-warning p-1"
      @click="commentDelete"
      >delete</button>
    </div> -->
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'CollectionComment',
    props: {
        comment: Object,
        collectionPk: Number
    },
    computed: {
      ...mapGetters('login', [
        'user', 'authHead'
      ])
    },
    methods: {
      ...mapActions('collection', [
        'actionDelete'
      ]),
      commentDelete() {
        const payload = {
          comment_pk: this.comment.id,
          collection_pk: this.collectionPk,
          headers: this.authHead
        }
        this.actionDelete(payload)
      }
    }
}
</script>

<style>
</style>