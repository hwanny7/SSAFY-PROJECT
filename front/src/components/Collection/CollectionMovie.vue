<template>
  <div>
    <div>
    <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" style="width:80px; height:80px;" data-bs-toggle="modal" :data-bs-target="`#o${movie.id}`" data-bs-whatever="@getbootstrap"
    :class="{'existContent':movie.content}"
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
              <div class="mb-3" v-if="!onoff">
                {{content}}
              </div>
              <!-- <label for="message-text" class="col-form-label">댓글 작성: </label> -->
              <textarea class="form-control" id="message-text" v-if="onoff" v-model="content"></textarea>
          </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
            v-if="onoff" @click="changeOnOff"
            >취소</button>
            <button type="button" class="btn btn-primary" @click="changeOnOff">수정</button>
            </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

export default {
    name: 'CollectionMovie',
    data() {
      return {
        content: this.movie.content,
        onoff: 0,
      }
    },
    props: {
      movie: Object,
    },
    methods: {
      changeOnOff() {
        this.onoff = !this.onoff
      }
    },
}
</script>

<style>
.existContent{
  border-style: solid;
  border-width: 5px;
  border-color: mediumaquamarine;
}


</style>