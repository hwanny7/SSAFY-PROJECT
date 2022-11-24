<template>
  <div class="d-flex flex-column align-items-center">
    <h1>회원가입</h1>
    <!-- <form @submit.prevent="signUp" enctype="multipart/form-data">
        <label for="id">아이디: </label>
        <input type="text" v-model.trim ="username"> <br>
        <label for="password1">비밀번호: </label>
        <input type="password" v-model.trim ="password1"> <br>
        <label for="password2">비밀번호 확인: </label>
        <input type="password" v-model.trim ="password2"> <br>
        <label for="nickname">별명: </label>
        <input type="text" v-model.trim ="nickname"> <br>
        <label for="img">프로필 URL: </label>
        <input type="file" accept="image/gif, image/jpeg, image/png" v-on:change="imgFile" /> <br>
        <input type="submit" value ="가입하기">
    </form> -->

    <form @submit.prevent="signUp" enctype="multipart/form-data" style="width:18rem;">
        <div class="mb-1">
          <label for="ID" class="form-label">ID</label>
          <input type="text" class="form-control" id="ID" placeholder="ID" v-model.trim ="username">
        </div>
        <div class="mb-1">
          <label for="password1" class="form-label">Password</label>
          <input type="password" class="form-control" id="password1" placeholder="Password" v-model.trim ="password1">
        </div>
        <div class="mb-1">
          <label for="password2" class="form-label">Password</label>
          <input type="password" class="form-control" id="password2" placeholder="Password" v-model.trim ="password2">
        </div>
        <div class="mb-1">
          <label for="nickname" class="form-label">Nick Name</label>
          <input type="text" class="form-control" id="nickname" placeholder="Nickname" v-model.trim ="nickname">
        </div>
        <div class="mb-1">
          <label for="content" class="form-label">Profile</label>
          <textarea class="form-control" id="content" rows="3" placeholder="Profile" v-model="content"></textarea>
        </div>
        <div class="mb-1">
          <label for="formFileMultiple" class="form-label">Profile image</label>
          <input class="form-control" type="file" accept="image/gif, image/jpeg, image/png" v-on:change="imgFile" id="formFileMultiple" multiple>
        </div>
        <input type="submit" class="btn btn-primary mt-3" value ="Sign Up">
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
            image: '',
            content: '',
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
            formData.append("content", this.content)
            this.signUpAction(formData)
        }
    }
}
</script>

<style>

</style>
