<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login({username, password})">
        <div>
            <label for="id">아이디: </label>
            <input type="text" v-model="username">
        </div>
        <div>
            <label for="password">비밀번호: </label>
            <input type="password" v-model="password">
        </div>
        <input type="submit" value="로그인">
    </form>

    <img src="@/assets/kakao_start.png" @click="kakaoLogin"> <!-- 카카오 로그인-->
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
    name: 'LoginView',
    data() {
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      ...mapActions('login', [
        'login', 'kakaoLogin' 
      ])
    }
}
</script>

<style>

</style>