<template>
<div>
    <div class="d-flex flex-column align-items-center">
        <div class="btn btn-danger btn-width my-3" @click="getMovie">PICK</div>
        <div class="card" style="width: 500px;">
            <img :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="">
            <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text">{{ movie.overview}}</p>
            </div>
        </div>
    </div>
</div>
</template>


<script>
import _ from 'lodash'
export default {
    name: 'RandomView',
    data() {
        return {
            movie: null,
            movieList: null
        }
    },
    methods: {
        getMovie() {
            this.movieList = this.$store.state.movie_list
            this.movie = _.sample(this.$store.state.movie_list)
        }
    },

    created() {
        this.getMovie() 
    }
}
</script>

<style scopped>
.btn-width {
    width : 500px;
}
</style>