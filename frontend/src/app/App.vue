<template>
  <v-app id="app">
    <router-view class="background"/>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  mounted() {
    this.$store.dispatch('relogin')
  }
}
</script>

<style>
:root {
  --gradient-1: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%)
}

.background {
  background-image: var(--gradient-1);
}
</style>
