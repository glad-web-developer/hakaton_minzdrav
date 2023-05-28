<template>
  <contollable-card
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
        :open="initiallyOpen"
        :items="items"
        activatable
        item-key="name"
        open-on-click
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
  </contollable-card>
</template>

<script>
import ContollableCard from "@/share/ui/ContollableCard";

export default {
  name: "OpenProtocolForm",
  components: {ContollableCard},
  data: () => ({
    search: '',
    initiallyOpen: ['public'],
    files: {
      html: 'mdi-language-html5',
      js: 'mdi-nodejs',
      json: 'mdi-code-json',
      md: 'mdi-language-markdown',
      pdf: 'mdi-file-pdf',
      png: 'mdi-file-image',
      txt: 'mdi-file-document-outline',
      xls: 'mdi-file-excel',
    },
    tree: [],
    items: [
      {
        name: '.git',
      },
      {
        name: 'node_modules',
      },
      {
        name: 'public',
        children: [
          {
            name: 'static',
            children: [
              {
                name: 'logo.png',
                file: 'png',
              },
              {
                name: 'logo1.png',
                file: 'png',
              },
              {
                name: 'logo2.png',
                file: 'png',
              },
              {
                name: 'logo3.png',
                file: 'png',
              },
            ],
          },
          {
            name: 'favicon.ico',
            file: 'png',
          },
          {
            name: 'index.html',
            file: 'html',
          },
        ],
      },
      {
        name: '.gitignore',
        file: 'txt',
      },
      {
        name: 'babel.config.js',
        file: 'js',
      },
      {
        name: 'package.json',
        file: 'json',
      },
      {
        name: 'README.md',
        file: 'md',
      },
      {
        name: 'vue.config.js',
        file: 'js',
      },
      {
        name: 'yarn.lock',
        file: 'txt',
      },
    ],
  }),
  computed: {
    filter() {
      return this.caseSensitive
          ? (item, search, textKey) => item[textKey].indexOf(search) > -1
          : undefined
    },
  },
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
