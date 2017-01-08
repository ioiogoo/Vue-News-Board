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

@media screen and (max-width: 992px) {
  html, body {
    background-color: #e2e4e6;
    font-size: 3vw
  }
  .form-control {
    height: 100%;
    font-size: 4vw
  }
  #label {
    font-size: 3vw
  }
  #item-box {
    border-radius: 15px
  }
}

@media screen and (min-width: 992px) {
  html, body {
    background-color: #7D7DA5;
  }
  #item-box {
    border-radius: 10px
  }
}


html, body {
    height: 100%;
    overflow-y: hidden;
    color: #000;
    font-family: 微软雅黑细体;
}

#app {
  height: 100%
}
</style>

