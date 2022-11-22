<template>
  <div>
    <h1>LikeView</h1>

    <!-- 좋아요, 싫어요, 좋아요 누르러 가기 -->
    <select class="form-select" aria-label="Default select example" v-model="likehate">
      <option value="like">LIKE</option>
      <option value="hate">HATE</option>
      <option value="all">ALL</option>
    </select>
  
    <div v-show="likehate === 'like'">
      <LikeListView
      :user-pk="user_pk"
       />
    </div>
    <div v-show="likehate === 'hate'">
      <HateListView
      :user-pk="user_pk"
       />
    </div>
    <div v-show="likehate === 'all'">
      <MovieList
      :user-pk="user_pk"
       />
    </div>

  </div>
</template>

<script>
import HateListView from '@/components/HateListView'
import LikeListView from '@/components/LikeListView'
import MovieList from '@/components/MovieList'

export default {
    name: 'LikeView',
    components: {
      HateListView,
      LikeListView,
      MovieList,
    },
    data () {
      return {
        likehate: 'like',
        user_pk : Number(this.$route.params.id)
      }
    },
    
}
</script>

<style>

</style>