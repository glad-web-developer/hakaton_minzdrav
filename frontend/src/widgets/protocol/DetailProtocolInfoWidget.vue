<template>
  <contollable-card
      :title="`Протокол ${$store.getters.getCurrentProtocol.innerNumber}`"
      @click-close-button="$emit('close')"
  >
    <v-expansion-panels accordion>
      <v-expansion-panel>
        <v-expansion-panel-header>Диагноз</v-expansion-panel-header>
        <v-expansion-panel-content class="grey lighten-4">Контент</v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Обследования</v-expansion-panel-header>
        <v-expansion-panel-content>Контент</v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Лечение</v-expansion-panel-header>
        <v-expansion-panel-content>Контент</v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </contollable-card>
</template>

<script>
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "DetailProtocolInfoWidget",
  components: {ContollableCard},
  protocolId: Number
}
</script>

<style scoped>

</style>
