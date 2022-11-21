<template>
  <div>
      <div class="card rounded d-flex justify-content-center align-items-center m-2 radius" style="width: 12rem;">
        <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" class="card-img-top" alt="..." data-bs-toggle="modal" :data-bs-target="`#x${movie.id}`" data-bs-whatever="@getbootstrap"
        style="height: 300px;">
      </div>
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
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="moviePick">추가</button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>


<script>


export default {
    data() {
        return {
            content: '', // 사용자는 공백을 입력할수도 있음
        }
    },
    name: 'CollectionCreateMovie',
    props: {
        movie: Object
    },
    methods: {
        moviePick() {
            const movie = {...this.movie, ...{"content":this.content}}
            this.$emit('pick', movie)
            this.content =''
        },
    }
}
</script>

<style>

</style>