<template>
  <div>
    <CollectionView
    v-for="(collection, index) in getAllCollections"
    :key="index"
    :collection="collection"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import CollectionView from '@/components/Collection/CollectionView'



export default {
    name: 'AllCollection',
    components: {
      CollectionView, 
    },
    computed: {
      ...mapGetters('login', [
        'user', 'authHead'
      ]),
      ...mapGetters('collection', [
        'getAllCollections'
      ])
    },
    methods: {
      ...mapActions('collection', [
        'AllCollections'
      ])
    },
    created() {
      this.AllCollections(this.authHead)
    }
}
</script>

<style>

</style>