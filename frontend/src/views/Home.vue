<template>
  <div class="home">
    <v-header></v-header>
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import VHeader from '@/components/header/VHeader.vue';
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'home',
  components: {
    HelloWorld,
    VHeader
  }
}
</script>

<style lang="scss" scoped>
  .home {
    text-align: center;
  }
</style>
