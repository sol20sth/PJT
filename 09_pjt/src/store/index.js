import Vue from 'vue'
import Vuex from 'vuex'
// import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie_list : [],
    randommovie : null,
    watchList: []
  },
  getters: {

  },
  mutations: {
    GETMOVIE(state, movies){
      state.movie_list = movies
    },
    GETINPUT(state, input_list){
      state.watchList.push(input_list)
    },
    CHECKMOVIE(state, content){
      state.watchList.forEach(watch => {
        if (content.data===watch.data) {
          watch.select = !watch.select
        }
      })
      }
    },

  actions: {
    get_movie(context, movies){
      context.commit('GETMOVIE', movies)
    },
    get_input(context, input_list) {
      context.commit('GETINPUT', input_list)
    },
    checkMovie(context, content) {
      context.commit('CHECKMOVIE', content)
      console.log(content)
    }
  },
  modules: {
  }
})
