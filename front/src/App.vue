<template>
  <div id="app" class="text-white">
    <nav>
      <div v-if="!isLogin">
        <router-link :to="{name : 'LoginView'}">Login</router-link>
      </div>
      <div v-else>
        <router-link :to="{name : 'AllCollection' }">Collection</router-link> |
        <router-link :to="{name : 'ProfileView', params: { id: user?.pk } }">Profile</router-link> |
        <button @click="logout">로그아웃</button>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default {
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
        const url = 'https://image.tmdb.org/t/p/original' + _.sample(this.getMoviePick).poster_path
        console.log(url)
        this.backGround(url)
        // document.getElementById('background').style.backgroundImage=url
        // document.body.style.backgroundImage = 'url(' + this.getBackImg + ')'
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.box {
    width: 50px;
    height: 50px; 
}
.profile {
    width: 100%;
    height: 100%;
    border-radius: 30%;
    object-fit: cover;
}
</style>
