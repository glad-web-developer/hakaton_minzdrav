<template>
  <contollable-card
      title="Протоколы других специалистов"
      @click-close-button="$emit('close')"
  >
    <v-data-table
        item-key="innerNumber"
        sort-by="innerNumber"
        hide-default-footer
        :headers="headers"
        :items="protocols"
        :loading="isLoading"
        :item-class="getItemClass"
        @click:row="onClickRow"
    />
  </contollable-card>
</template>

<script>

import DoctorApi from "@/entities/doctor/api";
import ProtocolApi from "@/entities/protocol/api";
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "OtherSpecialistProtocols",
  components: {ContollableCard},
  data() {
    return {
      isLoading: true,
      headers: [
        {
          text: 'Номер карты',
          align: 'start',
          value: 'innerNumber',
          class: 'other-specialist-protocols-widget-header-cell'
        },
        {
          text: 'Дата явки',
          value: 'dateOfAppearance',
          class: 'other-specialist-protocols-widget-header-cell',
        },
        {
          text: 'Диагноз',
          value: 'diagnosis',
          class: 'other-specialist-protocols-widget-header-cell'
        },
        {
          text: 'Врач',
          value: 'doctor',
          class: 'other-specialist-protocols-widget-header-cell',
        },
        {
          text: 'Код',
          value: 'code',
          class : 'other-specialist-protocols-widget-header-cell'
        },
      ],
      protocols: []
    }
  },
  mounted() {
    const fetchData = async () => {
      const protocols = await ProtocolApi.getAllProtocolsByPatientId(this.$store.state.patient.id)
      const doctors = await Promise.all(protocols.map(protocol => DoctorApi.getDoctorById(protocol.doctorId)))

      this.protocols = protocols.map(protocol => ({
        id: protocol.id,
        innerNumber: protocol.innerNumber,
        dateOfAppearance: protocol.dateOfAppearance,
        doctor: doctors.find(doctor => doctor.id === protocol.doctorId).firstName,
        diagnosis: protocol.diagnosis.title,
        code: protocol.diagnosis.code,
      }))

      this.isLoading = false
    }

    fetchData()
  },
  methods: {
    getItemClass() {
      return `other-specialist-protocols-widget-row`
    },
    onClickRow(item) {
      if (!this.$store.state.protocol.isLoading) {
        this.$store.dispatch('addProtocol', {protocolId: item.id})
      }
    }
  }
}
</script>

<style lang="scss">
.other-specialist-protocols-widget-header-cell {
  padding: 0;
}

.other-specialist-protocols-widget-row {
  cursor: pointer;
}
</style>
