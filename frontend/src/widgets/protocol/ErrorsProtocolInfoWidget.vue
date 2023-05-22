<template>
  <contollable-card
      title="Ошибки в протоколе"
      @click-close-button="$emit('close')"
  >
    <v-container class="d-flex flex-column gap-2">
        <span class="red--text">
          Превышение дозировки для препарата
        </span>
      <span class="red--text">
          Не совпадает номер заболевание с фактическим наименованием
        </span>
    </v-container>
  </contollable-card>

</template>

<script>
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "ErrorsProtocolInfoWidget",
  components: {ContollableCard}
}
</script>

<style scoped>

</style>
