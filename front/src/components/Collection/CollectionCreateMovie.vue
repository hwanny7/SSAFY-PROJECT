<template>
  <div>
    <form @submit.prevent="moviePick">
        <p>{{movie.title}}</p>
        <input type="text" v-model="content">
        <input type="submit">
    </form>
  </div>
</template>

호버나 모달기능 넣어야함

<script>
export default {
    data() {
        return {
            content: null,
        }
    },
    name: 'CollectionCreateMovie',
    props: {
        movie: Object
    },
    methods: {
        moviePick() {
            const movie = {...this.movie, ...{"content":this.content}}
            this.$emit('pick', movie)
        }
    }
}
</script>

<style>

</style>