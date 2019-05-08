<template>
  <div class="home" :style="`margin-top: ${margin}px`">
    <v-header @addMargin="addMargin"></v-header>
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
  },

  data() {
    return {
      margin: 0
    };
  },

  methods: {
    addMargin(margin) {
      this.margin = margin;
    }
  }
}
</script>

<style lang="scss" scoped>
  .home {
    text-align: center;
  }
</style>
