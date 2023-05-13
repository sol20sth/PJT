<template>
  <div class="watchSpan" :class="{'ListDiv' : content.select}">
    <span  @click="checkMovie" :class="{'lined' : content.select}">{{ content.data }}</span>
    <span v-if="content.select">: 취소완료</span>
  </div>
</template>

<script>
export default {
    name: 'WatchListItem',
    props: {
        content: Object
    },
    methods : {
        checkMovie() {
            this.$store.dispatch('checkMovie', this.content)
        },

    }

}
</script>

<style>
.watchSpan {
    font-size: 25px;
    background-color: rgb(219, 218, 218);
}
.ListDiv{
    background-color: #ac3b3b;
    border: 0.002rem solid black;
    border-radius: 0px 0px 8px 8px;
}
</style>