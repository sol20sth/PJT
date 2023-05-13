<template>
  <div class="album py-5 bg-body-tertiary">
    <img src="" alt="">
    <div class = "container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-3">
        <div v-for="(movie, index) in movielist" :key="index">
          <div class="col">
            <MovieCard :movie="movie"/>
          </div> 
        </div>
      </div>
    </div>
    
  </div> 
  
</template>

<script>

import MovieCard from '@/components/MovieCard.vue'

export default {
    name: 'MovieView',
    components : {
        MovieCard
    },
    data() {
        return {
            MovieList: null
        }
    },

    computed :{
        movielist(){
            return this.$store.state.movie_list
        }
    },

}
</script>

<style>

</style>