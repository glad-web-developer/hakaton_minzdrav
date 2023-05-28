<template>
  <v-btn
      class="text-white"
      text
      link
      @click="clickHandler"
  >
    Выйти из системы
  </v-btn>
</template>

<script>
export default {
  name: "LogoutButton",
  methods: {
    clickHandler() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scoped>

</style>
