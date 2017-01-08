<template>
  <div id="app" class="row">
    <news_wraper v-for='cat in cats' :cat='cat'></news_wraper>
  </div>
</template>

<script>
import news_wraper from './components/new_wraper'

export default {
  name: 'app',
  data(){
    return {}
  },
  computed:{
    cats(){
      return this.$store.state.cats
    }
  },
  components: { news_wraper }
}
</script>

<style>

@media screen and (max-width: 768px) {
  .form-control {
    font-size: 20px
  }
}

html, body {
    height: 100%;
    overflow-y: hidden;
    color: #000;
    font-family: 微软雅黑细体;
    background-color: #7D7DA5;
}

#app {
  height: 100%
}
</style>

