<template>
  <v-overlay v-if="isLoading">
    <v-progress-circular indeterminate/>
  </v-overlay>
  <contollable-card
      v-else
      title="Открыть файл"
      class="root"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-text-field
        v-model="search"
        label="Поиск..."
        light
        hide-details
        clearable
        clear-icon="mdi-close-circle-outline"
    ></v-text-field>

    <v-treeview
        class="treeview"
        dense
        v-model="tree"
        :search="search"
        :filter="filter"
        :items="items"
        activatable
        item-key="id"
        open-on-click
        return-object
    >
      <template v-slot:prepend="{ item, open }">
        <v-icon v-if="!item.file">
          {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
        </v-icon>

        <v-icon v-else>
          {{ files[item.file] }}
        </v-icon>
      </template>
    </v-treeview>
    <v-pagination
        v-if="pages > 1"
        v-model="page"
        :length="pages"
        circle
    ></v-pagination>
  </contollable-card>
</template>

<script>
import ContollableCard from "@/share/ui/ContollableCard";
import ProtocolApi from "@/entities/protocol/api";

export default {
  name: "OpenProtocolForm",
  components: {ContollableCard},
  data: () => ({
    search: '',
    files: {
      js: 'mdi-nodejs',
      json: 'mdi-code-json',
      md: 'mdi-language-markdown',
      pdf: 'mdi-file-pdf',
      png: 'mdi-file-image',
      txt: 'mdi-file-document-outline',
      xls: 'mdi-file-excel',
    },
    tree: [],
    items: [],

    isLoading: true,
    pages: null,
    page: 1,
  }),
  computed: {
    filter() {
      return this.caseSensitive
          ? (item, search, textKey) => item[textKey].indexOf(search) > -1
          : undefined
    },
  },
  methods: {
    async fetchPacks() {
      const response = await ProtocolApi.getAllPackProtocols(this.page)
      this.items = response.data
      this.pages = response.pageCount
      this.isLoading = false
    }
  },
  watch: {
    page() {
      this.fetchPacks()
    }
  },
  mounted() {
    this.fetchPacks()
  }
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
  height: 80vh;
}

.treeview {
  max-height: 500px;
  overflow-y: scroll;
}
</style>
