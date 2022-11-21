<template>
  <div>
    <div class="card rounded d-flex justify-content-center align-items-center m-2 radius">
      <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" style="height:150px;" data-bs-toggle="modal" :data-bs-target="`#o${movie.id}`" data-bs-whatever="@getbootstrap"
      :class="{'glowing-border':movie.content}"
      >
    </div>

    <div class="modal fade" :id="'o'+movie.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">내용</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
              <div class="mb-3">
              </div>
              <textarea class="form-control" id="message-text" v-model="content"></textarea>
          </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
            @click="reviseDelete"
            >삭제</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="reviseContent">수정</button>
            </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

export default {
    name: 'ReviseForm',
    data() {
      return {
        content: this.movie.content
      }
    },
    props: {
      movie: Object,
    },
    methods: {
      reviseContent() {
        this.$emit('reviseContent', this.content, this.movie.id)
      },
      reviseDelete() {
        this.$emit('reviseDelete', this.movie.id)
      }
    },
}
</script>

<style>
.existContent{
  border-style: solid;
  border-width: 3px;
  border-color: mediumaquamarine;
}
.glowing-border {
    border: 2px solid #9ecaed;
    border-radius: 7px;
}

.glowing-border:focus {
    outline: none;
    border-color: #9ecaed;
    box-shadow: 0 0 10px #9ecaed;
}



</style>