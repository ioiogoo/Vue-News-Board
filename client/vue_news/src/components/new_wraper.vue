<template>
<div id="t-box" class="col-md-3 col-xs-12">
<div id="t" >

	<div id="select" class="input-group col-md-10 col-md-offset-1 col-xs-5 col-xs-offset-6">
		<span id="label" class="input-group-addon">
			<a href='#' id='update' @click='updateNews'>
				<img src="../assets/loading.gif" v-show='updating'>
				<img src="../assets/pic.png" title="update" v-show='!updating'>
			</a>
			{{label}}:
		</span>
		<select class='form-control' v-model='c_cat'>
		  <option v-for='c in cats'>{{c}}</option>
		</select>


	</div>
	<div id='wraper'>

			<ul>
				<div id="item-box" v-for='n in news' class="col-md-10 col-md-offset-1 col-xs-10 col-xs-offset-1">
					<div id="item-name"><a :href="n.url" target="__blank">{{n.title}}</a></div>
					<div id="item-intro" v-if='n.intro'>{{n.intro}}</div>
					<div id="item-time" v-if='n.time'>{{n.time}}</div>
				</div>
			</ul>
	</div>
</div>
</div>
</template>

<script>
	export default {
		data(){
			return {
				c_cat: '',
				labelmap: {
					'hacker': 'hacker_new',
					'jobbole': '伯乐在线',
					'freebuf': 'Freebuf',
					'bobao': '安全客'
				},
				updating: false
			}
		},
		props: ['cat'],
		created(){
			this.c_cat = this.cat
		},
		computed:{
			cats(){
				return this.$store.state.cats
			},
			news(){
				return this.$store.state.news[this.c_cat]
			},
			label(){
				return this.labelmap[this.c_cat]
			}
		},
		watch: {
			c_cat(){
				this.$store.dispatch('getNews',{'cat': this.c_cat})
			}
		},
		methods:{
			updateNews(){
				this.$http({
					// url: 'http://127.0.0.1:5000/api/updateNews',
					url: '/api/updateNews',
					method: 'POST',
					before: ()=>{this.updating = true},
				}).then(res=>{
					this.updating=false
					this.$store.dispatch('getNews',{'cat': this.c_cat})
					return
				})
			}
		}
	}
</script>

<style>
div #wraper {
	overflow-y: auto;
}

div #t-box {
	height: 100%;
	padding: 0.5%
}

div #t {
	background-color: #e2e4e6;
	border-radius: 5px;
}

#item-box {
	background-color: #fff;
	margin-bottom: 10px;
	box-shadow:1px 1px 1px rgba(0,0,0,.3)
}

#item-box:hover {
	background-color: #f7f7f7;
}

ul {
	padding: 0;
	margin-top: 10px
}

#item-name {
	border-bottom: 1px solid #dbdbdb;
	padding: 5px 10px
}

#item-intro {
	padding: 10px;
	border-bottom: 1px solid #dbdbdb;
}

#item-time {
	padding: 5px 10px
}

a:hover {
	text-decoration: none;
}

#select {
	padding-top: 10px;
	padding-bottom: 5px
}

</style>
