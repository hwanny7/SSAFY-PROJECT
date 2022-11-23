<template>
  <div>
<swiper
    class="swiper"
    :options="swiperOption"
>
    <swiper-slide><img src="https://image.tmdb.org/t/p/original/v2nvvwbWOAEPQeq8wsvUkhb1HI1.jpg" alt="" ></swiper-slide>     
    <swiper-slide><img src="https://image.tmdb.org/t/p/original/v2nvvwbWOAEPQeq8wsvUkhb1HI1.jpg" alt="" ></swiper-slide>     
    <swiper-slide><img src="https://image.tmdb.org/t/p/original/v2nvvwbWOAEPQeq8wsvUkhb1HI1.jpg" alt="" ></swiper-slide>     
    <swiper-slide><img src="https://image.tmdb.org/t/p/original/v2nvvwbWOAEPQeq8wsvUkhb1HI1.jpg" alt="" ></swiper-slide>     
    <swiper-slide><img src="https://image.tmdb.org/t/p/original/v2nvvwbWOAEPQeq8wsvUkhb1HI1.jpg" alt="" ></swiper-slide>
    <!-- <div
    class="swiper-pagination"
    slot="pagination"
    >
    </div> -->
    <!-- <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div> -->
</swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'testView',
  components: {
    Swiper,
    SwiperSlide,
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
    };
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