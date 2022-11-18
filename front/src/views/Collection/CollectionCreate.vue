<template>
    <div>
        <form @submit.prevent="create">
            <label for="title">title: </label>
            <input type="text" id="title" v-model="title">
            <label for="content">content: </label>
            <input type="text" id="content" v-model="content">
            <input type="submit">
        </form>
        <h1>영화를 선택하세요.</h1>
        <CollectionCreateMovie
        v-for="(movie, index) in getMoviePick"
        :key="`o-${index}`"
        :movie="movie"
        @pick="pick"
        />
    </div>

</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from 'axios'
import CollectionCreateMovie from '@/components/Collection/CollectionCreateMovie'

export default {
    components: {
        CollectionCreateMovie
    },
    data() {
        return {
            title: null,
            content: null,
            moviePick: [],
        }
    },
    name : "CollectionCreate",
    computed: {
        ...mapGetters('login', [
            'authHead',
        ]),
        ...mapGetters('collection', [
            'getMoviePick'
        ])
    },
    methods: {
        ...mapActions('collection', [
          'CreateCollection',
        ]),
        // title 공백 작성 막기
        create() {
            axios({
              url: 'http://127.0.0.1:8000/collects/collection/',
              method: 'post',
              headers: this.authHead,
              data: {
                title: this.title,
                content: this.content,
                movies: this.moviePick
              }
            })
              .then(res => {
                console.log(res)
              })
        },
        pick(data) {
            this.moviePick.push(data)
        }
    },
    created() {
        this.CreateCollection()
    }
}
</script>

<style>

</style>