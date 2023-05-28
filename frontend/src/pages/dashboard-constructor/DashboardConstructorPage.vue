<template>
  <v-container fluid class="mw-100 pt-0">
    <v-row class="h-100">
      <v-col class="h-100" ref="content">

        <v-overlay v-if="isLoading">
          <v-progress-circular indeterminate/>
        </v-overlay>

        <vue-draggable-resizable
            v-else
            class="border-0 cursor-pointer"
            w="auto"
            h="auto"
            v-for="widget in activeWidgets"
            :key="widget.id"
            :x="widget.x"
            :y="widget.y"
            :grid="[grid,grid]"
            :parent="true"
            :resizable="false"
            @dragging="(x, y) => onDragging(x, y, widget.id)"
        >
          <div :style="{width: `${widget.cols * grid}px`}">
            <contollable-card
                :title="widget.title"
                @click-close-button="onCloseWidget(widget.id)"
            >
              <component :is="widget.component"/>
            </contollable-card>
          </div>
        </vue-draggable-resizable>
      </v-col>

      <v-navigation-drawer absolute v-model="isShowWidgetsList" right temporary>
        <v-form v-model="isValidForm" ref="form" @submit.prevent="onSubmit">
          <v-text-field
              v-model="dashboardTitle"
              placeholder="Введите название"
              :rules="[value => !!value || 'Обязательное поле.']"
          />
          <v-btn tile block type="submit">Сохранить</v-btn>
        </v-form>
        <v-list two-line flat>
          <v-list-item-group
              v-model="activeWidgets"
              multiple
          >
            <template v-for="widget in widgets">
              <v-list-item :key="widget.id" :value="widget">
                <template v-slot:default="{active}">
                  <v-list-item-action>
                    <v-checkbox
                        :input-value="active"
                        color="primary"
                    ></v-checkbox>
                  </v-list-item-action>

                  <v-list-item-content>
                    <v-list-item-title>{{ widget.title }}</v-list-item-title>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </template>

          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>

      <v-btn elevation="2" color="white" fab icon class="widgets-fab-on" @click="onClickShowWidgetsList">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
    </v-row>
    <v-snackbar
        v-model="isShowSnackbar"
    >
      {{ message }}
    </v-snackbar>

  </v-container>

</template>

<script>
import DashboardApi from "@/entities/dashboard/api";
import {MorbidityBChartWidget, MorbidityCChartWidget, TestChar} from '@/widgets/'
import {ContollableCard} from "@/share/ui";

export default {
  name: "DashboardConstructorPage",
  components: {MorbidityCChartWidget, MorbidityBChartWidget, ContollableCard, TestChar},
  data() {
    return {
      widgets: [],
      isShowWidgetsList: false,
      grid: null,

      dashboardTitle: null,
      activeWidgets: [],


      isValidForm: true,
      isLoading: true,
      isShowSnackbar: false,
      message: null
    }
  },
  methods: {
    onCloseWidget(widgetId) {
      this.activeWidgets = this.activeWidgets.filter(widget => widget.id !== widgetId)
    },

    onDragging(x, y, widgetId) {
      this.activeWidgets.forEach(widget => {
        if (widget.id === widgetId) {
          widget.x = x
          widget.y = y
        }
      })
    },

    onClickShowWidgetsList() {
      this.isShowWidgetsList = true
    },

    onSubmit() {
      this.validateForm()
      this.createDashboard()
    },

    validateForm() {
      this.isValidForm = this.$refs.form.validate()
    },
    setWidgetRequirementProperties(widget) {
      if (!widget.x) {
        widget.x = 0
      }

      if (!widget.y) {
        widget.y = 0
      }

      return widget
    },
    showMessage(message) {
      this.message = message
      this.isShowSnackbar = true
      setTimeout(() => this.isShowSnackbar = false, 1500)
    },

    async fetchWidgets() {
      this.widgets = await DashboardApi.getAllWidgets()
      this.isLoading = false
    },

    async createDashboard() {
      if (this.isValidForm) {
        const response = await DashboardApi.createDashboard(
            this.dashboardTitle,
            this.activeWidgets.map(this.setWidgetRequirementProperties)
        )

        if (response.status === 201) {
          this.showMessage('Доска успешно создана')
        } else {
          this.showMessage('Произошла ошибка')
        }
      }
    },

    calculateGrid() {
      const pl = parseInt(window.getComputedStyle(this.$refs.content, null).paddingLeft.split('px')[0], 10)
      const pr = parseInt(window.getComputedStyle(this.$refs.content, null).paddingRight.split('px')[0], 10)
      const width = this.$refs.content.getBoundingClientRect().width

      const innerWidth = width - pl - pr

      this.grid = innerWidth / 32
    }
  },
  mounted() {
    this.calculateGrid()
    this.fetchWidgets()
  }
}
</script>

<style scoped lang="scss">
.cursor-pointer {
  cursor: pointer !important;
}

.widgets-fab-on {
  position: absolute;
  top: 50%;
  right: 0%;
  transform: translate(-25%, 50%);
  background-color: black;
}
</style>
