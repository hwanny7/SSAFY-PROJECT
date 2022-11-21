<template>
  <div>
    <!-- {{$route.params.id}} -->
    <h1>프로필</h1>
    <div>
      <!-- <p>{{profile}}</p> -->
      <p>별명: {{profile.nickname}}</p>
      <img :src="'http://127.0.0.1:8000' + profile.image" alt="" style="width:100px; heigh:80px;"> <!--user가 로그인 했을 경우에만-->
      <div v-if="profile.pk != user.pk">
        <div v-if="profile.followers.includes(user.pk)">
          <button @click="fixFollower(profile.pk)">언팔로우</button>
        </div>
        <div v-else>
          <button @click="fixFollower(profile.pk)">팔로우</button>
        </div>
      </div>
      <p>가입일: {{profile.date_joined.slice(0, 10)}}</p>
      <p>팔로워: {{profile.followers_count}}명</p>
      <div class="d-flex justify-content-center">
        <div v-for="(follower, index) in profile.followers_info"
        :key="index"
        >
          <div class="box">
            <img :src="'http://127.0.0.1:8000' + follower.image" alt="" class="profile">
          </div>
        </div>
      </div>
      <p>포인트: {{profile.point}}</p>
    </div>
    <div v-if="user.pk == profile.pk">
      <router-link :to="{name : 'CollectionCreate'}">Create</router-link>
    </div>
    <hr>
    <CollectionView
    v-for="(collection) in getMyCollections"
    :key="collection.id"
    :collection="collection"
    :profilePk="profile.pk"
    />
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import CollectionView from '@/components/Collection/CollectionView'



export default {
    name: 'ProfileView',
    components: {
      CollectionView, 
    },
    data() {
      return {
        id: this.$route.params.id
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