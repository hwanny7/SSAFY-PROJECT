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
    <router-link :to="{name : 'SignUpView'}">회원가입</router-link>
    <!-- <img src="@/assets/kakao_start.png" @click="kakaoLogin"> 카카오 로그인 -->

<!-- <div class="container">
  <div class="move">
    <div class="p-button normal signin animated pulse">SIGN IN</div>
  </div>
  <div class="welcome">
    <h4 class="bold welcome-text">Welcome Back!</h4>
    <p class="normal text">To keep connected with us please login with your personal info</p>
  </div>
  <div class="hello">
    <h4 class="bold welcome-text">Hello Friend</h4>
    <p class="normal text">Enter your personal details and start journey with us</p>
  </div>
  <div class="form">
    <h4 class="bold title">Create Account</h4>
    <div class="icons">
      <div class="icon"><i class="fab fa-facebook-f"></i></div>
      <div class="icon"><i class="fab fa-github"></i></div>
      <div class="icon"><i class="fab fa-twitter"></i></div>
    </div>
    <br>
    <input type="text" placeholder="ID" class="normal name">
    <input type="text" placeholder="Email" class="normal">
    <br/>
    <input type="password" placeholder="Password" class="normal"><br>
    <p class="normal forgot">Forgot your password?</p>
    <button class="b-button normal">SIGN UP</button>
  </div>
</div> -->

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

/* Fonts
@import url('https://fonts.googleapis.com/css?family=Montserrat:500,700&display=swap');

@import url('https://fonts.googleapis.com/css?family=Darker+Grotesque&display=swap');

body{
  background: #4d4d4d;
  margin:0;
}

.bold{
  font-family: 'Montserrat', sans-serif;
  font-weight:700;
  font-size:25px;
}

.normal{
  font-family: 'Darker Grotesque', sans-serif;
  font-weight:500;
  font-size:17px;
}

.welcome-text{
  color:#fff;
}

.welcome{
  text-align:center;
  color:#fff;
  position:absolute;
  height:50%;
  width:400px;
  z-index:30;
}

.hello{
  text-align:center;
  color:#fff;
  position:absolute;
  height:50%;
  right:0;
  width:400px;
  z-index:30;
  display:none;
}

.welcome-text{
  margin-top:100px;
}

.move{
  height:100%;
  position:absolute;
  width:400px;
  text-align:center;
  z-index:20;
  background-color:#2ecc71;
  background-image:url("http://www.pixmy.tech/Projects/Codepen/SlideForm/bg.jpg");
  background-size:cover;
  background-position:left;
  transition:all .4s ease;
  border-radius: 10px 0px 0px 10px;
}

@keyframes moving{
  0%{width:400px;transform:translate(0px);}
  50%{width:550px;transform:translate(200px);}
  100%{width:400px;transform:translate(500px);}
}

@keyframes start{
  0%{width:400px;transform:translate(500px);}
  50%{width:550px;transform:translate(200px);}
  100%{width:400px;transform:translate(0px);}
}

@keyframes startForm{
  0%{width:500px;transform:translate(0px);}
  50%{width:650px;transform:translate(200px);}
  100%{width:500px;transform:translate(400px);}
}

@keyframes movingForm{
  0%{width:500px;transform:translate(400px);}
  50%{width:650px;transform:translate(200px);}
  100%{width:500px;transform:translate(0px);}
}

.moving{
  animation: moving .4s linear forwards;
  transition:all .4s ease-out;
}

.movingForm{
  animation: movingForm .4s linear forwards;
  transition:all .4s ease-out;
}

.start{
  animation: start .4s linear forwards;
  transition:all .4s ease-out;
}

.startForm{
  animation: startForm .4s linear forwards;
  transition:all .4s ease-out;
}

.p-button{
    animation-iteration-count:5;
  color:white;
  padding:12px 60px;
  color:#fff;
  font-size:14px;
  border-radius:25px;
  border:1px solid #fff;
  width:40%;
  position:absolute;
  left:0;
  right:0;
  margin: auto;
  top:60%;
  text-align:center;
  cursor:pointer;
  transition:all .4s ease;
}

.p-button:hover{
  transition:all .4s ease;
  background-color:rgba(0,0,0,.7);
}

h4{
  font-size:22px;
}

p{
  font-size:14px;
}

.container{
  height:450px;
  width:900px;
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%, -50%);
}

.text{
  width:60%;
  line-height:20px;
  margin:0 auto;
}

.icon{
  width:30px;
  height:30px;
  border:1px solid lightgray;
  border-radius:50%;
  text-align:center;
  cursor:pointer;
  line-height:30px;
  display:inline-block;
}

.icon:hover{
  background-color:#000;
  color:white;
}

.light{
  color:#b2bec3;
}

.icons{
  text-align:center;
  margin-bottom:20px;
}

.forgot{
  display:none;
}

.form{
  text-align:center;
  position:absolute;
  height:100%;
  transform:translate(400px);
  width:500px;
  background-color:#fff;
  border-radius:0px 10px 10px 0px;
}

input{
  border:0px;
  border-bottom:1px solid lightgray;
  margin-bottom:15px;
  padding: 8px 5px;
  width:60%;
}

.b-button{
  background-color:#079992;
  color:white;
  padding:12px 60px;
  color:#fff;
  font-size:14px;
  border-radius:25px;
} */

</style>

