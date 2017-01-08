// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import VueResource from 'vue-resource'

Vue.use(Vuex)
Vue.use(VueResource)

const store = new Vuex.Store({
	state: {
		news: {},
		cats: ['jobbole', 'freebuf', 'bobao', 'hacker']
	},
	mutations: {
		getNews (state, payload){
			Vue.set(state.news, payload.cat ,payload.data['data'])
		}
	},
	actions: {
		getNews (context, payload){
			Vue.http({
					// url: 'http://127.0.0.1:5000/api/getNews',
				    url: '/api/getNews',
				    method: 'get',
				    params: {
				    	'cat': payload.cat
				    }}).then(res => res.json().then(data=>{context.commit('getNews', {'data': data, 'cat': payload.cat})}))

		}
	}
})

new Vue({
  el: '#app',
  store,
  template: '<App/>',
  components: { App }
})
