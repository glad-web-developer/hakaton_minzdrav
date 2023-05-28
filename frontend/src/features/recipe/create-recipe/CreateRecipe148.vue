<template>
  <contollable-card
      class="root"
      title="Рецепт форма №148"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    Форма 148
  </contollable-card>
</template>

<script>
import {ContollableCard} from "@/share/ui/";

export default {
  name: "CreateRecipe148",
  components: {ContollableCard}
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
  min-height: 80vh;
}
</style>
