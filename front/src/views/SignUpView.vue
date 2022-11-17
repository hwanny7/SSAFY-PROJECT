<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" enctype="multipart/form-data">
        <label for="id">아이디: </label>
        <input type="text" v-model.trim ="username"> <br>
        <label for="password1">비밀번호: </label>
        <input type="password" v-model.trim ="password1"> <br>
        <label for="password2">비밀번호 확인: </label>
        <input type="password" v-model.trim ="password2"> <br>
        <label for="nickname">별명: </label>
        <input type="text" v-model.trim ="nickname"> <br>
        <label for="img">프로필 URL: </label>
        <input type="file" accept=".jpg, .jpeg, .png" v-on:change="imgFile" /> <br>
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
            image: null,
        }
    },
    methods: {
        ...mapActions('login', [
            'signUpAction' // signUp 메소드랑 이름 충돌 일으키지 않게 action 붙임
        ]),
        imgFile(event) {
            this.image = event.target.files[0]
        },
        signUp() {
            const formData = new FormData()
            formData.append("username", this.username)
            formData.append("password1", this.password1)
            formData.append("password2", this.password2)
            formData.append("nickname", this.nickname)
            formData.append("image", this.image)
            this.signUpAction(formData)
        }
    }
}
</script>

<style>

</style>
