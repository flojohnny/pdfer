<template>
  <div id="pdf-container">
    <embed src="" width="100%" height="100%" alt="pdf" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
    };
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

<style>

</style>
