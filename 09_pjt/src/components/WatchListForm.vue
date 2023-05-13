<template>
  <div class="container watchDiv">
    <h1>보고싶은 영화</h1>
    <input type="text" v-model="InputData">
    <button class="WatchBtn" @click="get_input">Add</button>
  </div>
</template>

<script>
export default {
    name: 'WatchListForm',
    data(){
        return {
            InputData : null,
            input_list : [],
        }
    },
    methods : {
        get_input() {
            this.$store.dispatch('get_input', {data: this.InputData, select : false})
            this.InputData = null
        },
    }
}
</script>

<style>
.WatchBtn {
    border-radius: 8px;
    color: rgb(78, 72, 72);
    background-color: white;
    border: 0.5px solid black;
}
.watchDiv {
    color: rgb(168, 165, 165);
    background-color: rgb(78, 83, 85);
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding-bottom: 40px;
    padding-top: 40px;
}
</style>