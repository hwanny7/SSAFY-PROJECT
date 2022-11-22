<template>
  <div>
    <div class="card rounded d-flex justify-content-center align-items-center m-2 radius">
    <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" style="height:150px;" data-bs-toggle="modal" :data-bs-target="`#o${collectionId}${movie.id}`" data-bs-whatever="@getbootstrap">
    </div>

  <!-- <div class="box-wrap">
    <div class="box">
      <div class="img">
        <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" style="height:150px;" data-bs-toggle="modal" :data-bs-target="`#o${collectionId}${movie.id}`" data-bs-whatever="@getbootstrap" alt="Hover Effect">
      </div>
      <div class="info">
        <h3>Design</h3>
        <p>일러스트를 이용한 디자인입니다.</p>
      </div>
    </div>
  </div> -->

    <div class="modal fade text-dark" :id="'o'+collectionId+movie.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">내용</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
              <div class="mb-3">
                  <!-- <div class="embed-responsive embed-responsive-16by9">
                    <iframe class="embed-responsive-item iframe" :src="'https://www.youtube.com/embed/'+ `${movie.youtube_key}`" frameborder="1"></iframe>
                  </div> -->
                {{movie.content}}
              </div>
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
      }
    },
    props: {
      movie: Object,
      collectionId: Number,
    },
    methods: {
    },
}
</script>

<style>
/* .existContent{
  border-style: solid;
  border-width: 5px;
  border-color: mediumaquamarine;
      :class="{'existContent':movie.content}"
} */

/* .box-wrap {
  width: 100vw; ss
  height: 100vh; ss
  display: flex;
  justify-content: center;
  align-items: center
}
.box {
  position: relative;
  max-height: 100%;
  max-width: 100%;
  width: 100px; height: 150px; ss
  border: 7px solid #283593; ss 
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4)
}
.box img {
  max-height: 100%;
  max-width: 100%;
}

.box .info {
  color: #fff;
  position: absolute; left: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  width: 100%;
  padding: 15px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.35s ease-in-out;
}
.box:hover .info {
  opacity: 1;
}
.box .info h3 {
  font-size: 24px;
  padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}
.box .info p {
  font-size: 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
} */
</style>