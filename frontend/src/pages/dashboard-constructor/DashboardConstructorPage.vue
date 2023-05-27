<template>
  <v-container fluid class="mw-100 pt-0">
    <v-row class="h-100">
      <v-col class="h-100" ref="content">
        <vue-draggable-resizable
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
        <v-text-field :value="dashboardTitle" placeholder="Введите название"/>
        <v-btn tile block @click="onClickSaveDashboard">Сохранить</v-btn>
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
      widgets: [
        {
          id: 1,
          component: 'MorbidityCChartWidget',
          title: 'График гепатит C',
          cols: 10,
          x: 0,
          y: 0,
        },
        {
          id: 2,
          component: 'MorbidityBChartWidget',
          title: 'График гепатит B',
          cols: 10,
          x: 0,
          y: 0,
        },
        {
          id: 3,
          component: 'TestChar',
          title: 'График гепатит A',
          cols: 10,
          x: 0,
          y: 0,
        }
      ],
      activeWidgets: [],
      isShowWidgetsList: false,
      dashboardTitle: "",
      grid: null
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
    onClickSaveDashboard() {
      DashboardApi.saveDashboard({
        title: this.dashboardTitle,
        widgets: this.activeWidgets
      })
    },
  },
  mounted() {
    const pl = parseInt(window.getComputedStyle(this.$refs.content, null).paddingLeft.split('px')[0], 10)
    const pr = parseInt(window.getComputedStyle(this.$refs.content, null).paddingRight.split('px')[0], 10)
    const width = this.$refs.content.getBoundingClientRect().width

    const innerWidth = width - pl - pr

    this.grid = innerWidth / 32
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
