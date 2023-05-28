<template>
  <contollable-card
      class="root"
      title="Импортировать протокол"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-form
        @submit.prevent="onSubmitForm"
        ref="form"
        v-model="isValidForm"
        lazy-validation
    >
      <v-text-field
          v-model="title"
          label="Введите название набора"
          :rules="titleRules"
          required
          clearable
      >
        <template v-slot:prepend>
          <v-icon>
            mdi-format-text-variant
          </v-icon>
        </template>
      </v-text-field>

      <v-file-input
          v-model="file"
          label="Выберите файл"
          :rules="fileRules"
          required
          clearable
      />
      <v-btn type="submit">Импортировать</v-btn>
    </v-form>
  </contollable-card>

</template>

<script>
import ProtocolApi from "@/entities/protocol/api";
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "CreateProtocolForm",
  components: {ContollableCard},
  data() {
    return {
      isValidForm: true,

      fileRules: [
        value => !!value || 'Поле обязательное.',
        value => value?.name.endsWith('.xls') || value?.name.endsWith('.xlsx') || 'Файл должен быть excel формата',
      ],
      titleRules: [value => !!value || 'Поле обязательное.'],

      title: null,
      file: null,
    }
  },

  methods: {
    showSnackbar(message) {
      this.isShowSnackbar = true
      this.message = message
      setTimeout(() => this.isShowSnackbar = false, 1500)
    },

    validate() {
      this.isValidForm = this.$refs.form.validate()
    },

    async onSubmitForm() {

      this.validate()

      if (this.isValidForm) {
        const response = await ProtocolApi.importProtocol(this.title, this.file)

        if (response.status === 200) {
          this.$emit('click-close-button')
        }
      }
    },
  }


}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
}
</style>
