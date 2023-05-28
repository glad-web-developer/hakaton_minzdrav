<template>
  <v-card light>
    <v-toolbar dense max-height="0">
      <v-spacer/>
      <v-btn v-show="hasRollup" icon small @click="$emit('click-rollup-button')">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-btn icon small @click="$emit('click-close-button')">
        <v-icon>mdi-window-close</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-text class="h-100">
      <slot/>
    </v-card-text>
  </v-card>
</template>

<script>

export default {
  name: "ContollableCard",
  props: {
    title: String,
    hasRollup: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    }
  },
}
</script>

<style scoped lang="scss">
</style>
