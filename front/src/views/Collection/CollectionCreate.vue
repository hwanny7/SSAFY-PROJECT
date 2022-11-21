<template>
    <div>
        <form @submit.prevent="create">
            <label for="title">title: </label>
            <input type="text" id="title" v-model="title">
            <input type="submit">
        </form>
        <h1>영화를 선택하세요.</h1>
        <input type="text" :value="search" @input="search=$event.target.value">
        <div class="d-flex flex-row flex-wrap">
            <CollectionCreateMovie
            v-for="(movie, index) in inputChange"  
            :key="`o-${index}`"
            :movie="movie"
            @pick="pick"
            @update="update"
            @del="del"
            />
        </div>
    </div>

</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import CollectionCreateMovie from '@/components/Collection/CollectionCreateMovie'

export default {
    components: {
        CollectionCreateMovie
    },
    data() {
        return {
            title: '',
            moviePick: [],
            search: '',
        }
    },
    name : "CollectionCreate",
    computed: {
        ...mapGetters('login', [
            'authHead', 'user'
        ]),
        ...mapGetters('collection', [
            'getMoviePick'
        ]),
        inputChange() { // 공백여부 판단하기, 장르 필터도 같이 걸기, 양이 많으면 다음 페이지로 넘어가는 거
                        // 한글이라서 한칸 더 띄어쓰기 해야 인식이 되는 거 개선하기
            if (this.search === ''){
                return 0
            } else {
                const searchMovie = this.getMoviePick.filter( movie => {
                    return movie.title.split(' ').join('').includes(this.search.split(' ').join(''))
                    // 문자열 공백 제거를 위해 넣었음
                })
                return searchMovie
            }
        }
    },
    methods: {
        // title 공백 작성 막기
        create() {
            if (this.title){
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
                    this.$router.push({name: "ProfileView", params: {id: this.user.pk}})
                  })
            } else {
                alert('제목을 작성해 주세요.')
            }
        },
        pick(data) {
            this.moviePick.push(data)
        },
        update(data) { // 가능하면 dictionary 번호로 찾기
            let index
            for (let idx in this.moviePick){
                if (this.moviePick[idx].id === data.id){
                    index = idx
                    break
                }
            }
            this.moviePick.splice(index, 1, data)
        },
        del(id) {
            let index
            for (let idx in this.moviePick){
                if (this.moviePick[idx].id === id){
                    index = idx
                    break
                }
            }
            this.moviePick.splice(index, 1)
        },
    },
}
</script>

<style>

</style>