<template>
  <contollable-card
      class="root"
      title="Создать протокол"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-form @submit.prevent="onSubmitForm">
      <v-autocomplete
          label="Выберите доктора"
          required
          clearable
          :loading="isLoading"
          :value="doctorValue"
          :items="doctorItems"
      />
      <v-text-field
          label="Введите внутренний номер протокола (xxx/xxx)"
          clearable
          required
          v-model="innerNumberValue"
          :error="isInnerNumberError"
          :error-messages="innerNumberErrorMessage"

      />

      <v-text-field
          label="Имя пациента"
          clearable
          required
      />

      <v-text-field
          label="Фамилия пациента"
          clearable
          required
      />

      <v-text-field
          label="Отчество пациента"
          clearable
          required
      />

      <date-field label="Дата рождения пациента" @change-value="birthday=$event"/>

      <date-field label="Дата посещения пациента" @change-value="dateOfAppearance=$event"/>

      <v-textarea
          name="input-7-1"
          label="Примечание"
          auto-grow
          value=""
      />

      <v-btn type="submit">Создать</v-btn>

    </v-form>
  </contollable-card>

</template>

<script>
import DoctorApi from "@/entities/doctor/api";
import ProtocolApi from "@/entities/protocol/api";
import {formatFullName} from "@/share/utils";
import {DateField} from "@/share/ui";
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "CreateProtocolForm",
  components: {ContollableCard, DateField},
  data() {
    return {
      doctorValue: null,
      doctorItems: [],
      isLoading: true,

      isInnerNumberError: false,
      innerNumberErrorMessage: '',
      innerNumberValue: '',

      birthday: null,
      dateOfAppearance: null,
    }
  },
  mounted() {
    const fetchData = async () => {
      this.isLoading = true
      const doctors = await DoctorApi.getAllDoctors()
      this.doctorItems = doctors.map(doctor => formatFullName(doctor))
      this.isLoading = false
    }

    fetchData()
  },
  watch: {
    innerNumberValue: function (val) {
      const reg = /[1-9][1-9][1-9]\/[1-9][1-9][1-9]/gm
      if (!reg.test(val)) {
        this.isInnerNumberError = true
        this.innerNumberErrorMessage = 'Не корректно введен номер'
      } else {
        this.isInnerNumberError = false
        this.innerNumberErrorMessage = ''
      }
    },
  },
  methods: {
    onSubmitForm() {
      ProtocolApi.createProtocol({})
    },
  }


}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
  min-height: 80vh;
}
</style>
