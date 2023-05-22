<template>
  <v-container class="grey lighten-4 mw-100 d-flex flex-column">
    <v-row class="flex-grow-0">
      <v-col v-if="isShowShortInfoProtocol" cols="3">
        <short-protocol-info-widget @close="isShowShortInfoProtocol = false"/>
      </v-col>

      <v-col v-if="isShowDetailInfoProtocol">
        <detail-protocol-info-widget @close="isShowDetailInfoProtocol = false"/>
      </v-col>

      <v-col v-if="isShowOtherSpecialistProtocols || isShowErrorsProtocolInfo" class="d-flex flex-column gap-4">
        <other-specialist-protocols
            v-if="isShowOtherSpecialistProtocols"
            @close="isShowOtherSpecialistProtocols = false"
        />
        <errors-protocol-info-widget
            v-if="isShowErrorsProtocolInfo"
            @close="isShowErrorsProtocolInfo = false"
        />
      </v-col>
    </v-row>

    <v-spacer/>

    <v-row class="flex-grow-0">
      <change-protocol-tabs/>
    </v-row>
  </v-container>
</template>

<script>

import {
  DetailProtocolInfoWidget,
  ErrorsProtocolInfoWidget,
  navigationBus,
  OtherSpecialistProtocols,
  ShortProtocolInfoWidget,
} from "@/widgets/";
import {ChangeProtocolTabs} from "@/features/protocol/";

export default {
  name: "HomePage",
  components: {
    ChangeProtocolTabs,
    OtherSpecialistProtocols,
    ErrorsProtocolInfoWidget,
    DetailProtocolInfoWidget,
    ShortProtocolInfoWidget
  },
  data() {
    return {
      protocols: [],
      currentProtocolId: 1,
      isShowShortInfoProtocol: true,
      isShowDetailInfoProtocol: true,
      isShowOtherSpecialistProtocols: true,
      isShowErrorsProtocolInfo: true,
    }
  },
  mounted() {
    navigationBus.$on('click-show-short-protocol-info', () => this.isShowShortInfoProtocol = true)
    navigationBus.$on('click-show-detail-protocol-info', () => this.isShowDetailInfoProtocol = true)
    navigationBus.$on('click-show-other-specialist-protocols', () => this.isShowOtherSpecialistProtocols = true)
    navigationBus.$on('click-show-errors-protocol', () => this.isShowErrorsProtocolInfo = true)
  }
}
</script>

<style scoped>

</style>
