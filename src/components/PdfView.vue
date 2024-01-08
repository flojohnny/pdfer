<template>
  <div id="pdf-container">
    <embed
      :src="selectedPagePath"
      type="application/pdf"
      width="100%"
      height="100%"
    />
  </div>
</template>

<script>
import tempPDF from "../assets/temp.pdf";

export default {
  props: {
    selectedPage: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      selectedPagePath: tempPDF,
    };
  },
  watch: {
    selectedPage() {
      this.selectedPagePath = tempPDF + "#view=fitH";
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
