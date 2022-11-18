<template>
  <div>
    <p>{{comment.user}}</p>
    <p>{{comment.content}}</p>
    <!-- <hr> -->
  </div>
</template>

<script>
export default {
    name: 'CollectionComment',
    props: {
        comment: Object
    }
}
</script>

<style>

</style>