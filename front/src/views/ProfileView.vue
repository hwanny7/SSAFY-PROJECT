<template>
  <div class="container">
    <div class="row">
      <div class="d-flex flex-column align-items-center mb-5 col-3">
        <div class="card bg-dark rounded-3" style="width: 18rem;">
          <img :src="'http://127.0.0.1:8000' + profile.image" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title">{{profile.nickname}}</h5>
            <p>가입일: {{profile.date_joined.slice(0, 10)}}</p>
            <p>팔로워: {{profile.followers_count}}명</p>
            <p class="card-text">{{profile.content}}</p>
            <button class="btn btn-primary" 
            v-if="profile.pk != user.pk" @click="fixFollower(profile.pk)"
            >{{profile.followers.includes(user.pk) ? "Unfollow" : "follow"}}</button>
            <button class="btn btn-primary" v-if="profile.pk == user.pk">
              <router-link :to="{name : 'CollectionCreate'}" style ="text-decoration: none;" class="text-white">Create</router-link></button>
          </div>
          <div class="d-flex justify-content-center mb-2">
            <div v-for="(follower, index) in profile.followers_info"
            :key="index"
            >
              <div class="boxx ms-2 sample_image">
                <router-link :to="{name: 'ProfileView', params: {id: follower.id}}">
                  <img :src="'http://127.0.0.1:8000' + follower.image" alt="" class="profile">
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-9">
        <ProfileCollectionView
        v-for="(collection) in getMyCollections"
        :key="collection.id"
        :collection="collection"
        :profilePk="profile.pk"
        />
      </div>

    </div>


  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import ProfileCollectionView from '@/components/Collection/ProfileCollectionView'



export default {
    name: 'ProfileView',
    components: {
      ProfileCollectionView,
    },
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

</style>