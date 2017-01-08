<template>
<div id="t-box" class="col-md-3 col-xs-12">
<div id="t" >

	<div id="select">
		<span id="label">{{label}}:</span>
		<select class="form-control" v-model='c_cat'>
		  <option v-for='c in cats'>{{c}}</option>
		</select>
	</div>
	<div id='wraper'>

			<ul>
				<div id="item-box" v-for='n in news'>
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
				}
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
		}
	}
</script>

<style>
div #wraper {
	height: 100%;
	overflow-y: auto;
}

div #t-box {
	height: 100%;
	padding: 0.5%
}

div #t {
	height: 95%;
	background-color: #e2e4e6;
	margin-top: 40px;
	border-radius: 5px;
}

#item-box {
	width: 90%;
	background-color: #fff;
	margin: 0 auto 10px;
	border-radius: 10px;
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
	margin: 0 5% 0 60%;
	padding-top: 2%
}

.form-control {
	height: 100%;
}

#label {
	margin-left: -100%;
	float: left;
	padding: 6px 0

}
</style>
