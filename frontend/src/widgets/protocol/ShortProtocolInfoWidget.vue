<template>
  <contollable-card
      title="Информация о протоколе"
      @click-close-button="$emit('close')"
  >
    <v-container class="d-flex flex-column gap-2">
      <v-row>
        Дата: {{ $store.getters.getCurrentProtocol.dateOfAppearance }}
      </v-row>
      <v-row>
        Наличие ЭЛН: Есть
      </v-row>
      <v-row>
        Наличие рецепта: Есть
      </v-row>
      <v-row>
        Наличие ЭЦП: Есть
      </v-row>
      <v-row>
        Наличие повторной явки: Есть
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
