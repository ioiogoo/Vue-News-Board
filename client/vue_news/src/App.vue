<template>
  <div id="app" class="row">
    <div id="github" class="col-md-1 col-md-offset-11 col-xs-2 col-xs-offset-10">
      <a href="https://github.com/ioiogoo/Vue-News-Board" target="__blank"><img src="./assets/github.png"></a>
    </div>
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
  #github {
    height: 5vw;
  }
  div #wraper {
  height: 95%;
  }
  div #t {
    height: 95%;
  }
  #update img {
    height: 3vw;
    align-items: center
  }

}

@media screen and (min-width: 992px) {
  html, body {
    background-color: #7D7DA5;
  }
  #item-box {
    border-radius: 5px
  }
  #github {
    height: 3vw;
  }
  div #wraper {
  height: 90%;
  }
  div #t {
    height: 90%;
  }
  #update img {
    height: 18px;
    align-items: center
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

#github img {
  height: 100%;
}

#github {
  margin-top: 20px;
}


</style>

