<template>
  <div id="app" class="text-white">
    <nav>
    <ul>
      <li v-if="!isLogin">
        <router-link :to="{name : 'LoginView'}">Login</router-link>
      </li>
      <span v-else>
      <li>
        <router-link :to="{name : 'Home' }">Home</router-link>
      </li>
      <li>
        <router-link :to="{name : 'Like', params: { id: user?.pk } }">Like</router-link>
      </li>
      <li>
        <router-link :to="{name : 'AllCollection' }">Collection</router-link>
      </li>
      <li>
        <router-link :to="{name : 'ProfileView', params: { id: user?.pk } }">Profile</router-link>
      </li>
      <li>
        <a @click="logout">로그아웃</a>
      </li>
      </span>
    </ul>
    </nav>
    <router-view/>
    <MovieModal />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieModal from '@/components/MovieModal'
// import _ from 'lodash'  

export default {
    components:{
      MovieModal,
    },
    computed: {
      ...mapGetters('login', [
        'user', 'isLogin'
      ]),
      ...mapGetters('collection', [
        'getMoviePick', 'getBackImg'
      ])

    },
    methods: {
      ...mapActions('login', [
        'logout'
      ]),
      ...mapActions('collection', [
        'CreateCollection', 'backGround'
      ]),
    },
    created() {
        this.CreateCollection()
        this.$store.dispatch('getGenre')
        this.$store.dispatch('getUpcomingMovie')
        
//         const url = 'https://image.tmdb.org/t/p/original' + _.sample(this.getMoviePick).poster_path
//         console.log(url)
//         this.backGround(url)
//         document.body.style.backgroundImage = 'url(https://image.tmdb.org/t/p/original/iKIqdg57IPFChuZioKUAZnreH1W.jpg)'
//         document.body.style.backgroundImage = 'url(' + url + ')'

// var bg = document.getElementById("bg");

// setInterval(function(){
//   var color = Math.random()*0xffffff;
//   color = parseInt(color);
//   color = color.toString(16);
  
//   bg.style.background = "#" + color;
  
// },3000);
    }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


/* 프로필 이미지 */
.boxx {
    width: 50px;
    height: 50px; 
}
.profile {
    width: 100%;
    height: 100%;
    border-radius: 30%;
    object-fit: cover;
}


/* 영화 이미지 호버 */
.sample_image  img {
	-webkit-transform:scale(1);
	-moz-transform:scale(1);
	-ms-transform:scale(1);	
	-o-transform:scale(1);	
	transform:scale(1);
	-webkit-transition:.3s;
	-moz-transition:.3s;
	-ms-transition:.3s;
	-o-transition:.3s;
	transition:.3s;
}
.sample_image:hover img {
	-webkit-transform:scale(1.2);
	-moz-transform:scale(1.2);
	-ms-transform:scale(1.2);	
	-o-transform:scale(1.2);
	transform:scale(1.2);
}

/* 좋아요 버튼 */
[class^="hex-icon"] { width: 42px; height: 50px; margin: 0 10px; display: inline-block; transition: all 0.2s cubic-bezier(0.215, 0.610, 0.355, 1.000); -webkit-transition: all 0.2s cubic-bezier(0.215, 0.610, 0.355, 1.000); }
[class^="hex-icon"]:hover { transform: scale3d(1.2, 1.2, 1); -webkit-transform: scale3d(1.2, 1.2, 1); transition: all 0.35s cubic-bezier(0.000, 1.270, 0.460, 1.650); -webkit-transition: all 0.35s cubic-bezier(0.000, 1.270, 0.460, 1.650); }
[class^="hex-icon"] svg { width: 100%; height: 100%; display: block; }

.hex-icon-heart path:first-of-type { fill: #7b5af7; }
.hex-icon-heart path:last-of-type { fill: #fff; transform-origin: 21px 25px; -webkit-transform-origin: 21px 25px;
  animation: hex-icon-heart-beat 1s linear infinite;
  -webkit-animation: hex-icon-heart-beat 1s linear infinite;
}
@keyframes hex-icon-heart-beat { 0% { transform: scale3d(1, 1, 1); } 30% { transform: scale3d(0.75, 0.75, 1); } 60% { transform: scale3d(1, 1, 1); } }
@-webkit-keyframes hex-icon-heart-beat { 0% { -webkit-transform: scale3d(1, 1, 1); } 30% { -webkit-transform: scale3d(0.75, 0.75, 1); } 60% { -webkit-transform: scale3d(1, 1, 1); } }




/* nav bar */
@import url(https://fonts.googleapis.com/css?family=Open+Sans);

nav a.router-link-exact-active {
  color: #42b983;
}

nav {
  max-width: 960px;
  mask-image: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #ffffff 25%, #ffffff 75%, rgba(255, 255, 255, 0) 100%);
  margin: 0 auto;
  padding: 20px 0;
}

nav ul {
  text-align: center;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.2) 25%, rgba(255, 255, 255, 0.2) 75%, rgba(255, 255, 255, 0) 100%);
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.1), inset 0 0 1px rgba(255, 255, 255, 0.6);
}

nav ul li {
  display: inline-block;
}

nav ul li a {
  padding: 18px;
  font-family: "Open Sans";
  text-transform:uppercase;
  color: rgba(246, 255, 0, 0.5);
  font-size: 18px;
  text-decoration: none;
  display: block;
}

nav ul li a:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1), inset 0 0 1px rgba(255, 255, 255, 0.6);
  background: #42b983;
  color: black;
}

</style>






