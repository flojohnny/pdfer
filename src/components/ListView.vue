<template>
  <div class="list-container">
    <ul class="main-list" v-if="Object.keys(matches).length > 0">
      <ul class="sub-list" v-for="[pdf, pages] in Object.entries(matches)" :key="pdf">
        <h1 id="pdf_title">{{ pdf }}</h1>
        <li v-for="page in pages" :key="page.page">
          <div class="pdf-object">
            <button class="select-btn" @click="selectPdf(index)">
              <h2>
                {{ page.page }}
              </h2>
              <span class="icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                >
                  <line
                    x1="0"
                    y1="0"
                    x2="24"
                    y2="24"
                    stroke="#000"
                    stroke-width="3"
                  />
                  <line
                    x1="0"
                    y1="24"
                    x2="24"
                    y2="0"
                    stroke="#000"
                    stroke-width="3"
                  />
                </svg>
              </span>
            </button>
          </div>
        </li>
      </ul>
    </ul>
  </div>
</template>
<script>
export default {
  props: {
    matches: {
      type: Object,
      required: true,
    },
  },
  watch: {
    matches() {
      
    },
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {
    selectPdf(index) {
      this.$emit("select-pdf", index);
    },
  },
};
</script>

<style>

h1 {
  margin: 0;
  padding: 10px;
  font-size: 0.8rem;
  font-weight: bold;
  text-align:left;
}

ul {
  text-align: center;
  margin: 0;
  padding: 0;
}

li {
  display: inline;
  vertical-align: top;
}

.pdf-object {
  align-items: start;
  margin-left: 20px;
  padding: 1px;
}

.select-btn {
  width: 100px;
  height: 25px;
  cursor: pointer;
  display: flex;
  align-items: center;
  border: none;
  border-radius: 5px;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
  background: #767676;
}

.select-btn .text {
  transform: translateX(5px);
  color: rgb(0, 0, 0);
  font-weight: bold;
}

.select-btn .icon {
  position: relative;
  margin-left: auto;
  margin-right: 0px;
  height: 24px;
  width: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.select-btn svg {
  width: 15px;
  fill: #000000;
}

.select-btn:hover {
  background: #b33e3e;
}

.select-btn:focus {
  outline: none;
}

.select-btn:active .icon svg {
  transform: scale(0.8);
}
</style>
