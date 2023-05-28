<template>
  <contollable-card
      class="root"
      title="Импортировать протокол"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-form @submit.prevent="onSubmitForm" ref="form">
      <v-file-input
          v-model="file"
          :rules="[
              value => !!value || 'Поле обязательное.',
              value => value.name.endsWith('.xls') || value.name.endsWith('.xlsx') || 'Файл должен быть excel формата',
              ]"
          clearable
      />
      <v-btn type="submit">Импортировать</v-btn>
    </v-form>

    <v-snackbar
        v-model="isShowSnackbar"
    >
      {{ message }}

      <template v-slot:action="{ attrs }">
        <v-btn
            color="pink"
            text
            v-bind="attrs"
            @click="isShowSnackbar = false"
        >
          Закрыть
        </v-btn>
      </template>
    </v-snackbar>
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
      isShowSnackbar: false,
      message: null,

      file: null,
    }
  },

  methods: {
    showSnackbar(message) {
      this.isShowSnackbar = true
      this.message = message
      setTimeout(() => this.isShowSnackbar = false, 1500)
    },

    async onSubmitForm() {

      if (!this.file) {
        this.showSnackbar('Поле файла обязательное')
        return
      }

      const response = await ProtocolApi.importProtocol(this.file)

      if (response.status === 200) {
        this.showSnackbar('Файл успешно импортирован')
      } else {
        this.showSnackbar('Произошла ошибка при импорте')
        this.file = null
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
