<template>
  <div>ent-center alig
    <div class="card rounded d-flex justify-contn-items-center m-2 radius sample_image">
    <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" style="height:150px;" data-bs-toggle="modal" :data-bs-target="`#o${collectionId}${movie.id}`" data-bs-whatever="@getbootstrap"
    :class="{'glowing-border':movie.content}"
    >
    </div>


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
// import { SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
    name: 'CollectionMovie',
    components: {
      // SwiperSlide,
    },
    data() {
      return {
        swiperOption: { 
          slidesPerView: 4, 
          spaceBetween: 10, 
          effect:'coverflow',
          grabCursor:"true",
          centeredSlides:"true",
          // slidesPerView:'auto',
          coverflowEffect:{
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows: true,
          },
          pagination:"true",
          modules:"modules",
          class:"mySwiper",
        },
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
.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>