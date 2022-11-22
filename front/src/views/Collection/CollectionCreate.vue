<template>
    <div>
      <div>
        <form @submit.prevent="create" class="d-flex justify-content-center">
          <div class="d-flex flex-row">
            <input class="form-control me-2" type="search" placeholder="Collection Title" aria-label="Search" style="width: 20rem;" v-model="title">
            <button class="btn btn-outline-success" type="submit">생성</button>
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked @click="open_public = !open_public">
              <label class="form-check-label" for="flexSwitchCheckChecked">공개여부</label>
            </div>
          </div>
        </form>
        <div class="d-flex justify-content-center align-items-center mt-3">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" :value="search" @input="search=$event.target.value" style="width: 50rem;">
        </div>
      </div>
      
      <div class ="d-flex flex-row justify-content-center flex-wrap">
        <ReviseForm
        v-for="(movie, index) in moviePick"
        :key="index"
        :movie="movie"
        @reviseContent="reviseContent"
        @reviseDelete="reviseDelete"
        />
      </div>

      <div class ="d-flex flex-row justify-content-center flex-wrap">
        <CollectionCreateMovie
        v-for="(movie, index) in inputChange"  
        :key="`o-${index}`"
        :movie="movie"
        @pick="pick"
        />
      </div>
    </div>

</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import CollectionCreateMovie from '@/components/Collection/CollectionCreateMovie'
import ReviseForm from '@/components/Collection/ReviseForm'


export default {
    components: {
        CollectionCreateMovie,
        ReviseForm,
    },
    data() {
        return {
            title: '',
            moviePick: [],
            search: '',
            open_public: false,
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
                    movies: this.moviePick,
                    open_public: this.open_public
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
          for (let idx in this.moviePick){
            if (data.id == this.moviePick[idx].id){
              alert('이미 추가된 영화입니다.')
              return
            }
          }
          this.moviePick.push(data)
        },
        reviseContent(data, id){
          let index
          let movie
          for (let idx in this.moviePick){
            if (this.moviePick[idx].id === id){
              index = idx
              movie = this.moviePick[idx]
              break
            }
          }
          movie.content = data
          this.moviePick.splice(index, 1, movie)
        },
        reviseDelete(id){
          let index
          for (let idx in this.moviePick){
            console.log(this.moviePick[idx])
            if (this.moviePick[idx].id == id){
              index = idx
              break
            }
          }
          this.moviePick.splice(index, 1)
        }
    },
}
</script>

<style>

</style>