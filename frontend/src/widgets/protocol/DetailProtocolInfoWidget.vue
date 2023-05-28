<template>
  <contollable-card
      :title="`Протокол ${$store.getters.getCurrentProtocol.id}`"
      @click-close-button="$emit('close')"
  >
    <v-expansion-panels accordion>
      <v-expansion-panel>
        <v-expansion-panel-header>Лечащий врач</v-expansion-panel-header>
        <v-expansion-panel-content class="grey lighten-4">
          <v-container>
            <v-row>
              <div>ФИО: {{ `${$store.getters.getCurrentProtocol.doctorSourceFio}` }}</div>
            </v-row>
            <v-row>
              <div>Специализация: {{ `${$store.getters.getCurrentProtocol.doctorSourceSpecialization}` }}</div>
            </v-row>
          </v-container>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Результаты обследования</v-expansion-panel-header>
        <v-expansion-panel-content class="grey lighten-4">
          <v-container>
            <v-row>
              {{ `${$store.getters.getCurrentProtocol.assignmentString}` }}
            </v-row>
          </v-container>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Лечение</v-expansion-panel-header>
        <v-expansion-panel-content class="grey lighten-4">
          <v-container>
            <v-row>
              {{ `${$store.getters.getCurrentProtocol.assignmentString}` }}
            </v-row>
          </v-container>
        </v-expansion-panel-content>
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
