<template>
  <div   @click="checkMovie" :class="{'lined' : content.select, 'ListDiv' : content.select}" class="watchSpan">
    <span>{{ content.data }}</span>
    <span v-if="content.select">: 취소완료</span>
    <button @click.stop="deleteWatch">삭제</button>
  </div>
</template>

<script>
export default {
    name: 'WatchListItem',
    props: {
        content: Object,
        index: Number
    },
    methods : {
        checkMovie() {
            this.$store.dispatch('checkMovie', {content: this.content, index:this.index})
        },
        deleteWatch() {
            this.$store.dispatch('deleteWatch', {content:this.content, index:this.index})
        }
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