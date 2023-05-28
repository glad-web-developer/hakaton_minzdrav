<template>

  <contollable-card
      title="Информация о протоколе"
      @click-close-button="$emit('close')"
  >
    <v-container class="d-flex flex-column gap-2">
      <v-row>
        Дата составления: {{ $store.getters.getCurrentProtocol.dateService }}
      </v-row>
      <v-row>
        ФИО пациента: {{ $store.getters.getCurrentProtocol.patientSourceFio }}
      </v-row>
      <v-row>
        Дата рождения: {{ $store.getters.getCurrentProtocol.patientDateBirth }}
      </v-row>
      <v-row>
        Пол: {{ $store.getters.getCurrentProtocol.patientSex === 1 ? 'Мужской' : 'Женский' }}
      </v-row>
    </v-container>
  </contollable-card>
</template>

<script>
import {ContollableCard} from "@/share/ui/";

export default {
  name: "ShortProtocolInfoWidget",
  components: {ContollableCard}
}
</script>

<style scoped>

</style>
