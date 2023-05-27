<template>
  <contollable-card
      class="root"
      title="Создать шаблон отчета"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-overlay v-if="isLoading">
      <v-progress-circular indeterminate/>
    </v-overlay>

    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step
            :complete="step > 1"
            step="1"
        >
          Конфигурация шаблона
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
            :complete="step > 2"
            step="2"
        >
          Выборка данных
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <v-form>
            <v-text-field
                label="Введите название шаблона"
                v-model="title"
                clearable
                required
            />

            <v-autocomplete
                label="Выберите тип отчета"
                v-model="selectType"
                :items="types"
                item-text="title"
                item-value="id"
            />
          </v-form>

          <v-btn
              color="primary"
              @click="step = 2"
          >
            Продолжить
          </v-btn>

          <v-btn text @click="$emit('click-close-button')">
            Отменить
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-form>
            <v-autocomplete
                v-model="selectTable"
                :items="tables"
                item-text="title"
                label="Выберите таблицу"
                return-object
                clearable
            />

            <v-dialog
                ref="dialog"
                v-model="isShowModal"
                :return-value.sync="selectDateRange"
                persistent
                width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="selectDateRange"
                    label="Выберите отчетный период"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                  v-model="selectDateRange"
                  scrollable
                  range
              >
                <v-spacer></v-spacer>
                <v-btn
                    text
                    color="primary"
                    @click="isShowModal = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                    text
                    color="primary"
                    @click="$refs.dialog.save(selectDateRange)"
                >
                  OK
                </v-btn>
              </v-date-picker>
            </v-dialog>

            <v-treeview
                class="overflow-scroll overflow-x-hidden treeview"
                selectable
                v-model="selectFields"
                :items="viewtreeFields"
                return-object
            />

          </v-form>

          <v-btn
              color="primary"
              @click="fetchCreate"
          >
            Сохранить
          </v-btn>

          <v-btn text @click="step=1">
            Назад
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </contollable-card>
</template>

<script>
import ReportApi from "@/entities/report/api";
import {ContollableCard} from "@/share/ui/";

export default {
  name: "CreateReportTemplate",
  components: {ContollableCard},
  data() {
    return {
      step: 1,
      isLoading: true,
      isShowModal: false,

      title: '',
      selectTable: null,
      selectFields: [],
      selectType: null,
      selectDateRange: null,

      tables: [],
      types: [],
    }
  },
  computed: {
    viewtreeFields() {
      return this.selectTable?.fields.map(field => ({
        id: field.id,
        name: field.title,
        fieldId: field.id,
        children: field?.availableAggregateFunctions.map(fn => ({
          id: `field_${field.id}_fn_${fn.id}`,
          name: fn.title,
          fieldId: field.id,
          fnId: fn.id,
        }))
      }))
    },
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.tables = await ReportApi.getAllTables()
      this.types = await ReportApi.getAllTemplateTypes()
      this.isLoading = false
    },

    async fetchCreate() {
      // eslint-disable-next-line no-unused-vars
      const response = await ReportApi.createTemplate({
        type: this.selectType,
        title: this.title,
        fields: this.parseFields(this.selectFields)
      })

      this.$emit('click-close-button')
    },

    parseFields(fields) {
      const result = []

      fields.forEach(field => {
        const resField = result.find(rf => rf.field_id === field.fieldId)

        if (resField) {
          resField.aggregateFunctions.push(field.fnId)
        } else {
          result.push({
            field_id: field.fieldId,
            aggregateFunctions: [field.fnId]
          })
        }
      })

      return result
    }

  }
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
}

.treeview {
  max-height: 500px;
}
</style>
