<template>
  <v-container class="mw-100 grey lighten-4">
    <v-row class="h-100">
      <v-col class="h-100">
        <component
            ref="widgets"
            v-for="widget in activeWidgets"
            :is="widget.component"
            :key="widget.id"
            @close="onCloseWidget(widget.id)"
            @dragging="(x, y) => onDragging(x, y, widget.id)"
        />
      </v-col>
      <v-col v-if="isShowWidgetsList" cols="3" class="position-relative white">
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
        <v-btn elevation="2" color="white" fab icon class="widgets-fab-off" @click="onClickTogglerWidgetList">
          <v-icon>mdi-arrow-right</v-icon>
        </v-btn>
      </v-col>
      <v-btn v-else elevation="2" color="white" fab icon class="widgets-fab-on" @click="onClickTogglerWidgetList">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
    </v-row>
  </v-container>

</template>

<script>

import {MorbidityBChartWidget, MorbidityCChartWidget} from '@/widgets/'

export default {
  name: "DashboardConstructorPage",
  components: {MorbidityCChartWidget, MorbidityBChartWidget},
  data() {
    return {
      widgets: [
        {
          id: 1,
          component: 'MorbidityCChartWidget',
          title: 'График гепатит C',
          x: 0,
          y: 0,
        },
        {
          id: 2,
          component: 'MorbidityBChartWidget',
          title: 'График гепатит B',
          x: 0,
          y: 0,
        }
      ],
      activeWidgets: [],
      isShowWidgetsList: true,
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
    onClickTogglerWidgetList() {
      this.isShowWidgetsList = !this.isShowWidgetsList
    },
    onClickSaveDashboard() {

    }
  }
}
</script>

<style scoped lang="scss">
.widgets-fab-off {
  position: absolute;
  top: 50%;
  left: 0%;
  transform: translate(-50%, 50%);
  background-color: black;
}

.widgets-fab-on {
  position: absolute;
  top: 50%;
  right: 0%;
  transform: translate(50%, 50%);
  background-color: black;
}
</style>
