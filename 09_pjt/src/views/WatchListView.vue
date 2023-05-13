<template>
  <div class="container">
    <WatchListForm/>
    <div>
        <div v-for="(content, index) in watchList" :key="index">
            <WatchListItem :content="content"/>
        </div>
    </div>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'
import WatchListItem from '@/components/WatchListItem.vue'
export default {
    name : 'WatchListView',
    components : {
        WatchListForm,
        WatchListItem,
    },
    data(){
        return {
            InputData : null,
            input_list : [],
        }
    },
    computed:  {
        watchList() {
            return this.$store.state.watchList
        }
    },  
    methods : {
        // checkMovie: function (content) {
        //     console.log(content)
        //     content.select = !content.select
        // }
    }
}
</script>

<style>
.lined {
    text-decoration-line: line-through;
}

</style>