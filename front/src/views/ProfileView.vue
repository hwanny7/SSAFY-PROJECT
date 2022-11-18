<template>
  <div>
    <h1>프로필</h1>
    <img :src="user?.image" alt=""> <!--user가 로그인 했을 경우에만-->
    <p>별명: {{user?.nickname}}</p>
    <p>가입일: {{user?.date_joined}}</p>
    <p>래이팅: {{user?.point}}</p>
    <router-link :to="{name : 'CollectionCreate'}">Create</router-link>
    <h1>Collection</h1>
    <CollectionView
    v-for="(collection, index) in getMyCollections"
    :key="index"
    :collection="collection"
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
    computed: {
      ...mapGetters('login', [
        'user', 'authHead'
      ]),
      ...mapGetters('collection', [
        'getMyCollections'
      ])
    },
    methods: {
      ...mapActions('collection', [
        'myCollections'
      ])
    },
    created() {
      this.myCollections(this.authHead)
    }
}
</script>

<style>

</style>