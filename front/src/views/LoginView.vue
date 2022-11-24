<template>
  <div class="d-flex flex-column align-items-center">
    <h1>Login</h1>
    <form @submit.prevent="login({username, password})" style="width:18rem;">
        <div>
            <label for="id">아이디: </label>
            <input class="form-control" type="text" v-model="username">
        </div>
        <div>
          <div>
            <label for="password">비밀번호: </label>
          </div>
            <input class="form-control" type="password" v-model="password">
        </div>
        <input type="submit" class="btn btn-primary mt-3" value="로그인">
    </form>
    <router-link :to="{name : 'SignUpView'}">회원가입</router-link>


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
    },
}







</script>

<style>

</style>

