<template>
  <div id="pdf-container">
    <iframe
      :src="pdfUrl"
      type="application/pdf"
      width="100%"
      height="100%"
    ></iframe>
  </div>
</template>

<script>
import tempPDF from "../assets/output.pdf";

export default {
  data() {
    return {
      selectedPagePath: tempPDF,
    };
  },
  computed: {
    pdfUrl() {
      return this.selectedPagePath + "#toolbar=0";
    },
  },
  watch: {
    selectedPage() {
      this.selectedPagePath = tempPDF; // Update the PDF path as needed
    },
  },
  mounted() {
    this.loadPDF();
  },
  methods: {
    loadPDF() {
      // You may load the PDF content using fetch or another method
    },
    updatePDF(pdf) {
      this.selectedPagePath = pdf;
    },
  },
};
</script>

<style></style>
