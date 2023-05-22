<template>
  <div id="app">
    <v-app class="w-100">
      <v-main>
        <router-view/>
      </v-main>
    </v-app>

  </div>
</template>

<script>

export default {
  name: 'App',
  mounted() {
    this.$store.dispatch('relogin')
  }
}
</script>
