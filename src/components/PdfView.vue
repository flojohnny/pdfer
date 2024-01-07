<template>
  <div id="pdf-container">
    <a ref="pdf" :href="selectedPagePath" target="_blank" rel="noopener noreferrer">
      <embed
        :src="selectedPagePath"
        type="application/pdf"
        width="100%"
        height="100%"
      />
    </a>
  </div>
</template>

<script>
export default {
  props: {
    selectedPage: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      selectedPagePath: "",
    };
  },
  watch: {
    selectedPage() {
      this.selectedPagePath = this.selectedPage.pdf // + "#page=" + this.selectedPage.page
    },

  },
  mounted() {},
  methods: {
    updatePDF(pdf) {
      const embed = document.querySelector("embed");
      embed.setAttribute("src", pdf);
    },
  },
};
</script>

<style></style>
