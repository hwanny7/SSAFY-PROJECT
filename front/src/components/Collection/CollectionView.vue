<template>
  <div>
    <p>제목: {{collection.title}}</p>
    <p>내용: {{collection.content}}</p>
    <h3>댓글</h3>
    <CollectionComment
    v-for="(comment, index) in collection.collection_review_set"
    :key="`o-${index}`"
    :comment="comment"
    />
    <h3>MovieChoice</h3>
    <CollectionMovie
    v-for="(movie, index) in collection.movies"
    :key="index"
    :movie="movie"
    />

    <hr>
  </div>
</template>

<script>
import CollectionComment from '@/components/Collection/CollectionComment'
import CollectionMovie from '@/components/Collection/CollectionMovie'


export default {
    name: 'CollectionView',
    components: {
        CollectionComment,
        CollectionMovie,
    },
    props: {
        collection: Object,
    }
}
</script>

<style>

</style>