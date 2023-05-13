<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-body-tertiary nav-color">
      <div class="container-fluid">
      <img src="./assets/ssafy-logo.png" style="height:60px" alt="">
      <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button> -->
      <div class="mx-3">
        <router-link :to="{name:'MovieView'}" class="mx-3">Movie</router-link>
        <router-link :to="{name:'RandomView'}" class="mx-3">Random</router-link>
        <router-link :to="{name:'WatchListView'}" class="mx-3">WatchList</router-link>
      </div>

      </div>
    </nav>
    <nav>
      
      
      
    </nav>
    <router-view/>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'App',
  methods: {
        getMovieList() {
            axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${process.env.VUE_APP_SOME_API_KEY}&language=ko-KR&page=1/`,
            
        })
        .then((res) => {
            console.log(res.data.results)
            this.$store.dispatch('get_movie', res.data.results)
        })
        .catch((err) => {
            console.log(err)
        })
        }
    },
    created() {
      this.getMovieList()
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
  color: #f7f8f8;
}

nav a.router-link-exact-active {
  color: #a8735a;
}

.nav-color {
  background-color : rgb(41, 37, 37);
}
body{
  background-image: url('./assets/넷플.jpg');
  background-size: 100%;
}
</style>
