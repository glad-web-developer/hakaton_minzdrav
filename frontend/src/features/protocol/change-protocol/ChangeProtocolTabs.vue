<template>
  <div class="text-center d-flex align-center">
    <v-btn
        v-for="protocol in $store.state.protocol.protocols"
        @click="onClickHandler($event, protocol.id)"
        tile
        :key="protocol.id"
        :dark="protocol.id === $store.state.protocol.currentProtocolId"
    >
      {{ protocol.innerNumber }}
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "ChangeProtocolTabs",
  methods: {
    onClickHandler(event, protocolId) {
      this.$store.commit('changeCurrentProtocol', {id: protocolId})
    }
  }
}
</script>

<style scoped>

</style>
