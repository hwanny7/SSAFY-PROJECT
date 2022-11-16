<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp({username, password1, password2, nickname, img_url})">
        <label for="id">아이디: </label>
        <input type="text" v-model.trim ="username"> <br>
        <label for="password1">비밀번호: </label>
        <input type="password" v-model.trim ="password1"> <br>
        <label for="password2">비밀번호 확인: </label>
        <input type="password" v-model.trim ="password2"> <br>
        <label for="nickname">별명: </label>
        <input type="text" v-model.trim ="nickname"> <br>
        <label for="nickname">프로필 URL: </label>
        <input type="text" v-model.trim ="img_url"> <br>
        <input type="submit" value ="가입하기">
    </form>

  </div>
</template>




<script>
import {mapActions} from 'vuex'

export default {
    name: 'SignUpView',
    data() {
        return {
            username: null,
            password1: null,
            password2: null,
            nickname: null,
            img_url: null,
        }
    },
    methods: {
        ...mapActions('login', [
            'signUp'
        ])
    }
}
</script>

<style>

</style>