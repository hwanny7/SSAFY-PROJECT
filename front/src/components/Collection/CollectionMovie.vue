<template>
  <div>
    <p>{{movie.title}}</p>
    <p>{{movie.content}}</p>
  </div>
</template>

<script>
export default {
    name: 'CollectionMovie',
    props: {
      movie: Object
    }
}
</script>

<style>

</style>