<template>
<div class="">
    <div class="card shadow-sm movie-card">
        <img class="img-height" :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="">
        <div class="card-body ">
            <h5 class="card-title">{{ movie.title }}</h5>

            <p class="card-text">{{ movie.overview.slice(0, 110) }}...</p>

            
        </div>
    </div>
</div>
</template>

<script>
export default {
    name : 'MovieCard',
    props : {
        movie : Object
    },
}
</script>

<style>
.img-height {
    height : 500px;
}
</style>