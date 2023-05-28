<template>
  <v-menu
      ref="menu"
      v-model="menu"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
          v-model="birthdayDate"
          :label="label"
          readonly
          clearable
          v-bind="attrs"
          v-on="on"
      ></v-text-field>
    </template>
    <v-date-picker
        v-model="birthdayDate"
        :active-picker.sync="activePicker"
        :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
        min="1950-01-01"
        @change="save"
    />
  </v-menu>
</template>

<script>
export default {
  name: "DateField",
  props: ['label'],
  data() {
    return {
      birthdayDate: null,
      activePicker: null,
      menu: false
    }
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = 'YEAR'))
    },
    birthdayDate(val) {
      this.$emit('change-value', val)
    }
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date)
    },
  }
}
</script>

<style scoped>

</style>
