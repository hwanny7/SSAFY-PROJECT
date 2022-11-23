<template>
  <div>
    <div class="card bg-dark rounded-3" style="width: 18rem;">
      <img :src="'http://127.0.0.1:8000' + profile.image" class="card-img-top" alt="">
      <div class="card-body">
        <h5 class="card-title">{{profile.nickname}}</h5>
        <p>{{profile.date_joined.slice(0, 10)}}</p>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <button class="btn btn-primary" 
        v-if="profile.pk != user.pk" @click="fixFollower(profile.pk)"
        >{{profile.followers.includes(user.pk) ? "Unfollow" : "follow"}}</button>
        <button class="btn btn-primary" v-if="profile.pk == user.pk">
          <router-link :to="{name : 'CollectionCreate'}" style ="text-decoration: none;" class="text-white">Create</router-link></button>
      </div>
    </div>
    <div>

    <!-- <swiper
    :effect="'cards'"
    :grabCursor="true"
    :modules="modules"
    class="mySwiper"
    >
    <swiper-slide>Slide 1</swiper-slide><swiper-slide>Slide 2</swiper-slide
    ><swiper-slide>Slide 3</swiper-slide><swiper-slide>Slide 4</swiper-slide
    ><swiper-slide>Slide 5</swiper-slide><swiper-slide>Slide 6</swiper-slide
    ><swiper-slide>Slide 7</swiper-slide><swiper-slide>Slide 8</swiper-slide
    ><swiper-slide>Slide 9</swiper-slide>
    </swiper> -->


      <!-- <p>가입일: {{profile.date_joined.slice(0, 10)}}</p>
      <p>팔로워: {{profile.followers_count}}명</p> -->
    <div class="d-flex justify-content-center">
      <div v-for="(follower, index) in profile.followers_info"
      :key="index"
      >
        <div class="boxx">
            <img :src="'http://127.0.0.1:8000' + follower.image" alt="" class="profile">
          </div>
        </div>
      </div>
      </div>
      <div v-if="user.pk == profile.pk">
    </div>

    <ProfileCollectionView
    v-for="(collection) in getMyCollections"
    :key="collection.id"
    :collection="collection"
    :profilePk="profile.pk"
    />


  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import ProfileCollectionView from '@/components/Collection/ProfileCollectionView'

// import { Swiper, SwiperSlide } from "vue-awesome-swiper";
// import { EffectCards } from "swiper";


export default {
    name: 'ProfileView',
    components: {
      ProfileCollectionView,
      // Swiper,
      // SwiperSlide,
    },
    // setup() {
    //   return {
    //     modules: [EffectCards],
    //   }
    // },
    data() {
      return {
        id: this.$route.params.id,
        swiperOption: { 
        slidesPerView: 5, 
        spaceBetween: 30, 
        effect:'coverflow',
        grabCursor:"true",
        centeredSlides:"true",
        coverflowEffect:{
          rotate: 30,
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
    computed: {
      ...mapGetters('login', [
        'user', 'authHead', 'profile'
      ]),
      ...mapGetters('collection', [
        'getMyCollections'
      ])
    },
    methods: {
      ...mapActions('collection', [
        'myCollections',
      ]),
      ...mapActions('login', [
        'profileInfo', 'fixFollower'
      ]),
    setRating: function(rating){
      this.rating= rating;
    },
    },
    created() {
      const id = this.$route.params.id
      this.myCollections(id)
      this.profileInfo(id)
    },
    beforeRouteUpdate(to, from, next){ // 라우터에 다시 들어가면 처음 컴포넌트를 재사용해서 url만 바뀌고 내용은 안 바뀌기 때문에 페이지로 넘어가기 전에 mycollections에 id 값을 넘겨준다.
      this.myCollections(to.params.id)
      this.profileInfo(to.params.id)
      next()
    }
}
</script>

<style>
.swiper {
  width: 240px;
  height: 320px;
}

.swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 18px;
  font-size: 22px;
  font-weight: bold;
  color: #fff;
}

.swiper-slide:nth-child(1n) {
  background-color: rgb(206, 17, 17);
}

.swiper-slide:nth-child(2n) {
  background-color: rgb(0, 140, 255);
}

.swiper-slide:nth-child(3n) {
  background-color: rgb(10, 184, 111);
}

.swiper-slide:nth-child(4n) {
  background-color: rgb(211, 122, 7);
}

.swiper-slide:nth-child(5n) {
  background-color: rgb(118, 163, 12);
}

.swiper-slide:nth-child(6n) {
  background-color: rgb(180, 10, 47);
}

.swiper-slide:nth-child(7n) {
  background-color: rgb(35, 99, 19);
}

.swiper-slide:nth-child(8n) {
  background-color: rgb(0, 68, 255);
}

.swiper-slide:nth-child(9n) {
  background-color: rgb(218, 12, 218);
}

.swiper-slide:nth-child(10n) {
  background-color: rgb(54, 94, 77);
}
</style>