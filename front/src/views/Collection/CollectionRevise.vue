<template>
    <div>
        <form @submit.prevent="revise">
            <label for="title" >title: </label>
            <input type="text" id="title" :value="collection.title" @input="collection.title=$event.target.value">
            <input type="submit" value="수정하기">
        </form>
        <ReviseForm
        v-for="(movie, index) in collection.movies"
        :key="index"
        :movie="movie"
        @reviseContent="reviseContent"
        @reviseDelete="reviseDelete"
        />

        <h1>영화를 선택하세요.</h1>
        <input type="text" :value="search" @input="search=$event.target.value">
        <div class="d-flex flex-row flex-wrap">
            <CollectionCreateMovie
            v-for="(movie, index) in inputChange"  
            :key="`o-${index}`"
            :movie="movie"
            @pick="pick"
            />
        </div>
    </div>

</template>

@update="update"
@del="del"

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import CollectionCreateMovie from '@/components/Collection/CollectionCreateMovie'
import ReviseForm from '@/components/Collection/ReviseForm'


export default {
    components: {
        CollectionCreateMovie,
        ReviseForm
    },
    data() {
        return {
            title: '',
            moviePick: [],
            search: '',
            collection: {},
        }
    },
    name : "CollectionRevise",
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
        revise() {
            if (this.collection.title){
                axios({
                  url: 'http://127.0.0.1:8000/collects/collection/',
                  method: 'put',
                  headers: this.authHead,
                  data: this.collection
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
          this.collection.movies.forEach(movies => {
            if (movies.id == data.id){
              alert('이미 추가된 영화입니다.')
              // return >>> foreach로 하면 for문 말고 다른 걸로 해야함.
            }
          })
          this.collection.movies.push(data)
        },
        reviseContent(data, id){
          let index
          let movie
          for (let idx in this.collection.movies){
            if (this.collection.movies[idx].id === id){
              index = idx
              movie = this.collection.movies[idx]
              break
            }
          }
          movie.content = data
          console.log(movie.content)
          this.collection.movies.splice(index, 1, movie)

          // this.collection.movies.forEach(movie => {
          //   if (movie.id == id){
          //     movie.content = data
          //     console.log(movie)
          //     return
          //   }
          // })
          // this.collection.movies = [...this.collection.movies]
        },
        reviseDelete(id){
          let index
          for (let idx in this.collection.movies){
            if (this.collection.movies[idx].id == id){
              index = idx
              break
            }
          }
          this.collection.movies.splice(index, 1)
        }
    },
    created() {
      axios({
        url: `http://127.0.0.1:8000/collects/revise/${this.$route.params.pk}`,
        method: 'get',
      })
        .then(res => {
          this.collection = res.data
        })
    }
} 
// 라우터 막기 
</script>

<style>

</style>