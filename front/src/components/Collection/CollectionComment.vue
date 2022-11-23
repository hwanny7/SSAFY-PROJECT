<template>
  <div class="d-flex">
    <!-- <p>{{comment.user.}}</p> -->
    <div class="boxx">
    <img :src="'http://127.0.0.1:8000' + comment.user.image" alt="" class="profile">
    </div>
    <p class="text-black">{{comment.user.nickname}}: {{comment.content}}</p>
    <button v-if="user.pk === comment.user.id"
    @click="commentDelete"
    >delete</button>
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