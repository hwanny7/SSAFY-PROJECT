<template>
  <div>
        <div>
            <p>{{movie.title}}</p>
            <div>
                <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="안보일때~" style = 'width:100px; height:100px;'
                data-bs-toggle="modal" :data-bs-target="`#x${movie.id}`" data-bs-whatever="@getbootstrap"
                >
            </div>
<!--모달-->
<div class="modal fade" :id="'x'+movie.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">New message</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Message:</label>
            <textarea class="form-control" id="message-text" v-model="content"></textarea>
          </div>
      </div>
      <div class="modal-footer">
        <button v-if="cnt" type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="movieDelete">삭제</button>
        <button v-if="!cnt" type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="moviePick">추가</button>
        <button v-if="cnt" type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="movieUpdate">변경</button>
        
      </div>
    </div>
  </div>
</div>

        </div>
  </div>
</template>


<script>

collectionCreatemovie

export default {
    data() {
        return {
            content: '', // 사용자는 공백을 입력할수도 있음
            cnt: 0,
        }
    },
    name: 'CollectionCreateMovie',
    props: {
        movie: Object
    },
    methods: {
        moviePick() {
            const movie = {...this.movie, ...{"content":this.content}}
            this.cnt += 1
            this.$emit('pick', movie)
            
        },
        movieUpdate() {
            
            const movie = {...this.movie, ...{"content":this.content}}
            this.$emit('update', movie)
        },
        movieDelete() {
          
          this.$emit('del', this.movie.id)
          this.cnt = 0
          this.content = ''
        }
    }
}
</script>

<style>

</style>