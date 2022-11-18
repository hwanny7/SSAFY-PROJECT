<template>
  <div id="app">
    <h1>Collection</h1>
    <router-link :to="{name: 'CollectionCreate'}">생성하기</router-link> <br>
    <button @click='send'>collection 클릭</button> <br>
    <button @click='update'>update 클릭</button>
    <form @submit.prevent="del">
      <input type="number" v-model="pk">
      <input type="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters} from 'vuex'

export default {
  name: 'CollectionView',
  components: {
  },
  data(){
    return {
      pk: null
    }
  },
  computed: {
    ...mapGetters('login', [
        'user', 'authHead'
    ]),
  },
  methods: {
    send() {
        axios({
          url: 'http://127.0.0.1:8000/collects/collection/',
          method: 'post',
          headers: this.authHead,
          data: {
            title: '첫번째',
            content: '첫번째',
            movies: [597, 671, 808]
          }
        })
          .then(res => {
            console.log(res)
          })
    },
    update() {
      axios({
        url: 'http://127.0.0.1:8000/collects/update/',
        method: 'put',
        data: {
          title: '첫번째가 아닌',
          content: '두번째가 아닌',
          movies: [12444, 19995],
          collection_pk: 1,
        }
      })
        .then(res => {
          console.log(res)
        })      
    },
    del() {
      axios({
        url: 'http://127.0.0.1:8000/collects/update/',
        method: 'delete',
        data: {
          collection_pk: this.pk,
        }        
      })
    }
  }
}
</script>

<style>

</style>
