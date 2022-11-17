<template>
  <div>
    <h1>프로필</h1>
    <img :src="user?.image" alt=""> <!--user가 로그인 했을 경우에만-->
    <p>별명: {{user?.nickname}}</p>
    <p>가입일: {{user?.date_joined}}</p>
    <p>래이팅: {{user?.point}}</p>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'ProfileView',
    computed: {
      ...mapGetters('login', [
        'user'
      ])
    }
}
</script>

<style>

</style>