<template>

  <v-overlay v-if="isLoading">
    <v-progress-circular indeterminate/>
  </v-overlay>

  <contollable-card
      v-else
      class="root"
      title="Рецепт форма №107"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-form @submit.prevent="submitHandler" ref="form" v-model="isValidForm">
      <v-autocomplete
          label="Выберите препарат"
          multiple
          v-model="selectMedications"
          item-value="id"
          item-text="title"
          :rules="medicationRules"
          :items="medications"
          clearable
      />

      <v-btn type="submit">Сформировать рецепт</v-btn>
    </v-form>
  </contollable-card>
</template>

<script>
import {RecipeApi} from "@/entities/recipe/api";
import {MedicationApi} from '@/entities/medication/api'
import {ContollableCard} from "@/share/ui/";

export default {
  name: "CreateRecipe107",
  components: {ContollableCard},
  data() {
    return {
      isLoading: true,
      isValidForm: true,
      medicationRules: [
        value => !!value || 'Обязательное поле.',
        value => value.length > 0 || 'Необходимо выбрать хотя бы один препарат.'
      ],
      medications: null,

      selectMedications: [],
    }
  },
  methods: {
    async fetchData() {
      this.medications = await MedicationApi.getAllMedication()
    },

    validate() {
      this.isValidForm = this.$refs.form.validate()
    },

    clearForm() {
      this.selectMedications = []
    },

    async submitHandler() {
      this.validate()
      if (this.isValidForm) {
        this.isLoading = true
        const recipe = await RecipeApi.createRecipe(107, this.selectMedications)
        const a = document.createElement('a')
        a.href = recipe.src
        a.download = true
        a.click()
        this.clearForm()
        this.isLoading = false
      }
    }
  },
  mounted() {
    this.fetchData()
    this.isLoading = false
  }
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
}
</style>
