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
      <LikeListView />
    </div>
    <div v-show="likehate === 'hate'">
      <HateListView />
    </div>
    <div v-show="likehate === 'all'">
      이거는 아직
    </div>

  </div>
</template>

<script>
import HateListView from '@/components/HateListView'
import LikeListView from '@/components/LikeListView'

export default {
    name: 'LikeView',
    components: {
      HateListView,
      LikeListView,
    },
    data () {
      return {
        likehate: 'like',
      }
    },
    
}
</script>

<style>

</style>